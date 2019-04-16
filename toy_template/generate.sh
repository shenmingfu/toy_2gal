module load fftw
module load cfitsio

for i in {0..49}
do

/users/sfu1/Documents/jedisim5/jedinoise empty.fits 1 0.0077 noise_${i}.fits
sleep 3s
#/users/sfu1/Documents/jedisim5/jedinoise empty.fits 1 0.0077 noise_b${i}_90.fits
#sleep 3s

done
