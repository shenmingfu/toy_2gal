#

#===MODIFY THIS ONLY===
# Inputs
tag="q05_g010"        #"cr2_g040"  #"g005" #$1
g="0.10"    #$2
#======================

# Variables
folder="../toy_fix_${tag}"
group="${tag}"

# Scripts
mkdir ${folder}
cp *py ${folder}/
cp *sh ${folder}/
cp *cdf* ${folder}/
rm ${folder}/pipeline_1.py 
rm ${folder}/pipeline_v3.sh 
rm ${folder}/run.sh
sed -e "s/g_new = alice/g_new = ${g}/g" pipeline_1.py > ${folder}/pipeline_1.py
sed -e "s/group=bob/group=${group}/g" pipeline_v3.sh > ${folder}/pipeline_v3.sh
cd ${folder}
sbatch pipeline_v3.sh
