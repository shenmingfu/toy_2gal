#

# ---------------
# Module
import numpy as np
import func
import func2


# *****************************
# =============================
# THINGS NEEDS TO BE MODIFIED

#d_bin = 450
g = 0.199
e_T = (2*g)/(1+g**2)
bg_axis_ratio = np.sqrt((1-e_T)/(1+e_T))
#kappa = 0.229422 
#gamma = 0.153294
mu = 1.75349 
mag_bias = -2.5*np.log10(mu)
r_factor = 1/0.617283

g_new = alice #0.199
e_T_new = (2*g_new)/(1+g_new**2)
bg_axis_ratio_new = np.sqrt((1-e_T_new)/(1+e_T_new))
r_factor_new = r_factor*np.sqrt(bg_axis_ratio/bg_axis_ratio_new)
r_factor = r_factor_new
bg_axis_ratio = bg_axis_ratio_new

#bg_cat_file = "data_bg_480-420.cat" 
#cls_cat_file = "data_cls_480-420.cat"
dmin_cdf_file = "dmin_cdf_480-420.txt"

grid_row_num = 12
grid_col_num = 12
stamp_amount = grid_row_num*grid_col_num
stamp_size = 1024

# =============================
# *****************************


# ---------------
# Script


# 1. read in bg catalog, cls catalog, cdf (py)
# Note: bg, cls: mag-arcsec. cdf: 200mas-cdf
bg_cat = np.array([[25.2, 0.21]]) #np.loadtxt(bg_cat_file)
cls_cat = np.array([[23.3, 0.32]])  #np.loadtxt(cls_cat_file)
dmin_cdf = np.loadtxt(dmin_cdf_file)
# Magnify, arc->pixel
bg_cat[:,0] += mag_bias
bg_cat[:,1] *= (r_factor/0.06)
cls_cat[:,1] /= 0.06
d_2gal_arr = []


for counter in range(stamp_amount):
#2. simulate a stamp: (py)
#   1) write the pf of a bg stamp (py)
    prof_name = "1gal_%d.pf"%(counter)
    index = 0   #np.random.randint(len(bg_cat))
    mag = bg_cat[index, 0]
    r_e = bg_cat[index, 1]
    x = (stamp_size+1)/2.
    y = x
        
    func.write_head(prof_name, stamp_size, stamp_size)
    func.write_info(prof_name, 1, x, y, mag, r_e, 1., bg_axis_ratio, 90.)

#    2) write the pf of a sum (same bg + cls) stamp (py)
    prof_name = "2gal_%d.pf"%(counter)
    index = 0   #np.random.randint(len(cls_cat))
    mag = cls_cat[index, 0]
    r_e = cls_cat[index, 1]
    # 200mas->60mas
    d_2gal = func2.sample_cdf3(dmin_cdf)*0.2/0.06
    x_fits = (counter%grid_col_num)*stamp_size+x
    y_fits = (counter//grid_col_num)*stamp_size+y
    theta = np.random.random_sample()*np.pi*2
    dx, dy = d_2gal*np.cos(theta), d_2gal*np.sin(theta)
    x += dx
    y += dy
    func.write_head(prof_name, stamp_size, stamp_size)
    func.write_info(prof_name, 1, x, y, mag, r_e, 4., 1., 90.)
    d_2gal_arr.append([x_fits*0.06/0.2, y_fits*0.06/0.2, d_2gal*0.06/0.2, (x_fits+dx)*0.06/0.2, (y_fits+dy)*0.06/0.2])

header_in = "fiat 1.0\nttype1 = x_bg\nttype2 = y_bg\nttype3 = d\nttype4 = x_cls\nttype5 = y_cls"    
np.savetxt("d_2gal_arr.txt", d_2gal_arr, header=header_in)
