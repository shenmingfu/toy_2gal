import numpy as np
from astropy.io import fits

n = np.zeros((3686, 3686))
hdu = fits.PrimaryHDU(n)
hdu.writeto('empty.fits') 
