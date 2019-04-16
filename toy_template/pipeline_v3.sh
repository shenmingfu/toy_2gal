#!/bin/bash

# Request an hour of runtime:
#SBATCH --time=8:00:00

# Default resources are 1 core with 2.8GB of memory per core.

# Use more cores:
#SBATCH -n 32

#SBATCH --mem=80G
# Specify a job name:
#SBATCH -J 2gal

# Specify an output file
#SBATCH -o 2gal-%j.out
#SBATCH -e 2gal-%j.out


module load galfit
module load cfitsio
module load fftw

cpun=32
group=bob
> scrn.cmdf
python empty.py
bash generate.sh

#=============LOOP==============
for group_num in {0..49}
do

    #group_num=0
    image_tag=${group}_${group_num}
    stamp_folder=stamp_${image_tag}
    noiseframe=noise_${group_num}.fits
    
    python pipeline_1.py
    
    > stamp_1gal.list
    > stamp_2gal.list
    > cmdf1
   
    for i in {0..143}
    do
        
        profile_name="1gal_${i}.pf"
        echo "galfit ${profile_name}" >> cmdf1
        echo "1gal_${i}.pf.fits" >> stamp_1gal.list
        
        profile_name="2gal_${i}.pf"
        echo "galfit ${profile_name}" >> cmdf1
        echo "2gal_${i}.pf.fits" >> stamp_2gal.list
    
    done
    
    
    python ~/Documents/analysis_tools/run_process_2.4.py --cpun ${cpun} --cmdfile cmdf1
    
    python grid.py stamp_1gal.list grid_1gal_${image_tag}.fits
    python grid.py stamp_2gal.list grid_2gal_${image_tag}_cls.fits
    
    python ~/Documents/analysis_tools/addimg.py grid_1gal_${image_tag}.fits grid_2gal_${image_tag}_cls.fits grid_2gal_${image_tag}.fits
    
    rm *gal_*.pf.fits
    [ -d ${stamp_folder} ] && rm ${stamp_folder}/*
    [ ! -d ${stamp_folder} ] && mkdir ${stamp_folder}
    mv *gal_*.pf ${stamp_folder}/
    mv d_2gal_arr.txt d_2gal_arr_${group_num}.txt
    
    echo "bash scrn.sh ${image_tag} ${noiseframe}" >> scrn.cmdf

done

python ~/Documents/analysis_tools/run_process_2.4.py --cpun ${cpun} --cmdfile scrn.cmdf
rm grid*fits
rm noise*fits
rm empty.fits
