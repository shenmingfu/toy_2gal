#put stamps onto grid

import numpy as np
import astropy.io.fits as pyfits
import sys

if (len(sys.argv)!=3):
    print("Usage: python *.py stamp.list outimage.fits")
    print("Algorithm: paste pre-made stamps (on list) to a large image.")
    sys.exit(1)

# grid row & col number 
grid_row_num = 12
grid_col_num = 12

fp = open(sys.argv[1], 'r')
lst = fp.readlines()
fp.close()

if (len(lst)!=grid_row_num*grid_col_num):
    print("Error: number of stamps in list doesn't match grid")
    sys.exit(1)

#width in pixel
stamp_width = 1024  #512
grid_row_width = stamp_width*grid_row_num
grid_col_width = stamp_width*grid_col_num

grid_data = np.zeros((grid_row_width, grid_col_width))
#print(lst)

for i in range(len(lst)):
    #note the last character is '\n'
    stamp = pyfits.getdata(lst[i][:-1])
    item_row_index = i//grid_col_num
    item_col_index = i%grid_col_num
    #print(item_row_index, item_col_index) 
    grid_data[item_row_index*stamp_width:(item_row_index+1)*stamp_width, item_col_index*stamp_width:(item_col_index+1)*stamp_width] = stamp

pyfits.writeto(sys.argv[2], grid_data)

print("finish making grid image!")

