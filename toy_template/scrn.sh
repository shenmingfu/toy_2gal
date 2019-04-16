#!/bin/bash
#crn: convolve+rescale+noise
#modified @ Sun Aug 20 00:41:57 EDT 2017
#modified @ Sun Aug 20 16:35:52 EDT 2017
#modified @ Sat Nov 18 17:25:34 EST 2017
# Modified @ Sun Jul 22 16:43:01 EDT 2018

#Variales
jedifolder="/users/sfu1/Documents/jedisim5"
jediconv="${jedifolder}/jediconvolve"
#bgfolder="/net/mangrove/export/data/astro/sfu/backup_bg60000_"
#clsfolder="/net/mangrove/export/data/astro/sfu/backup_cls1000_"
psf="${jedifolder}/physics_settings/psf_scalednew_60.fits"
jedipaste="${jedifolder}/jedipaste"
jedirescale="${jedifolder}/jedirescale"
jedinoise="${jedifolder}/jedinoise"
exposure=1           #exposure time
noisemean=0.0077            #mean Poisson noise
add="${HOME}/Documents/analysis_tools/addimg.py"
#group=$1
#group_num=$2
image_tag=$1     #${group}_${group_num}
current_folder=${PWD}
noiseframe=$2

#Functions
#Usage: function_name $arg1 $arg2 ...

#convolve+rescale+noise 
crn () {
    #Variables
    convfolder=$1
    img=${1}.fits
    
    #Script
    echo "crn ${img}..." 

    #1)convolve
    
    #rm -f ${convfolder}/convolved_band_?.fits
    mkdir ${convfolder}
    > ${convfolder}/convolvedlist.txt
    echo "$PWD/${convfolder}/convolved_band_0.fits" >> ${convfolder}/convolvedlist.txt
    echo "$PWD/${convfolder}/convolved_band_1.fits" >> ${convfolder}/convolvedlist.txt
    echo "$PWD/${convfolder}/convolved_band_2.fits" >> ${convfolder}/convolvedlist.txt
    echo "$PWD/${convfolder}/convolved_band_3.fits" >> ${convfolder}/convolvedlist.txt
    echo "$PWD/${convfolder}/convolved_band_4.fits" >> ${convfolder}/convolvedlist.txt
    echo "$PWD/${convfolder}/convolved_band_5.fits" >> ${convfolder}/convolvedlist.txt
    ${jediconv} ${img} ${psf} ${convfolder}/   #is / necessary? YES!

    ${jedipaste} 12288 12288 ${convfolder}/convolvedlist.txt c_${img}     
    rm -f ${convfolder}/convolved_band_?.fits

    #2)rescale
    ${jedirescale} c_${img} 0.06 0.2 0 0 rc_${img}
    rm -f c_${img}
    
    #3)noise
    python ${add} rc_${img} ${noiseframe} nrc_${img}
#    ${jedinoise} rc_${img} ${exposure} ${noisemean} nrc_${img}
    rm -f rc_${img}

    rm -r ${convfolder}
}


#Script 
#if [ ! -d ${image_tag} ]
#then
#    mkdir ${image_tag}
#fi

#cd ${image_tag}
imgname=grid_1gal_${image_tag}
#ln -s ${current_folder}/grid_1gal_${group}.fits ./${imgname}.fits
crn ${imgname} 

imgname=grid_2gal_${image_tag}
#ln -s ${current_folder}/grid_2gal_${image_tag}.fits ./${imgname}.fits
crn ${imgname} 

#cd ${current_folder}
