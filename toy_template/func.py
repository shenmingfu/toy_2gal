# 

# Here are the definitions of funtions.

# Write the head of the profile file.
def write_head(filename, xmax, ymax):
    fp = open(filename, 'w')
    
    config = """================================================================================
# IMAGE and GALFIT CONTROL PARAMETERS
A) none       		# Input data image (FITS file)
B) ./%s.fits      	# Output data image block
C) none                # Sigma image name (made from data if blank or "none") 
D) none     #psf_LSST20000.fits         	 # Input PSF image and (optional) diffusion kernel
E) 1                   # PSF fine sampling factor relative to data 
F) none			# Bad pixel mask (FITS image or ASCII coord list)
G) none                # File with parameter constraints (ASCII file) 
H) 1    %d  1    %d  # Image region to fit (xmin xmax ymin ymax)
I) 1    1          # Size of the convolution box (x y)
J) 26.486              # Magnitude photometric zeropoint 
K) 0.06  0.06        # Plate scale (dx dy)   [arcsec per pixel]
O) regular             # Display type (regular, curses, both)
P) 0                   # Choose: 0=optimize, 1=model, 2=imgblock, 3=subcomps

# ------------------------------------------------------------------------------
#   par)    par value(s)    fit toggle(s)    # parameter description 
# ------------------------------------------------------------------------------

""" % (filename, xmax, ymax)

    fp.write(config)
    fp.close()
    return 0



# Write the info of a center galaxy.
def write_info(filename, counter, x, y, mag, r_e, sersic_index, axis_ratio, pos_angle):
    fp = open(filename, 'a')

    config = """# Component number: %d
 0) sersic                 #  Component type
 1) %f %f  1 1  #  Position x, y
 3) %f     1          #  Integrated magnitude 
 4) %f     1          #  R_e (effective radius)   [pix]
 5) %f      1          #  Sersic index n (de Vaucouleurs n=4) 
 6) 0.0000      0          #     ----- 
 7) 0.0000      0          #     ----- 
 8) 0.0000      0          #     ----- 
 9) %f      1          #  Axis ratio (b/a)  
10) %f     1          #  Position angle (PA) [deg: Up=0, Left=90]
 Z) 0                      #  Skip this model in output image?  (yes=1, no=0)

"""%(counter, x, y, mag, r_e, sersic_index, axis_ratio, pos_angle)

    fp.write(config)
    fp.close()
    return 0


