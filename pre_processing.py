import os
import h5py
import numpy as np

# get original order
original_order = \
    [0, 29, 1, 28, 2, 27, 3, 26, 4, 25, 5, 24, 6, 23, 7, \
     22, 8, 21, 9, 20, 10, 19, 11, 18, 12, 17, 13, 16, 14, 15]

# make paths
base_path = "/data1/rubinov_lab/yantong/project/MIT_dataset"
input_path = os.path.join(base_path, "original_data")
output_path = os.path.join(base_path, "organized_data")
os.makedirs(output_path, exist_ok=True)

# make functions to easily get input and output filenams
get_input_filename = lambda i: os.path.join(input_path, "stitch_layer_{}.hdf5".format(i))
get_output_filename = lambda i: os.path.join(output_path, "timepoint_{:05d}.hdf5".format(i))

# get dimensions using first plane dataset
z_dim = len(original_order)
with h5py.File(get_input_filename(0), "r") as f:
    t_dim, x_dim, y_dim = f["mov"].shape

# loop over time points
for t in range(t_dim):
    print(t)
    
    # generate volume at timepoint t
    vol = np.zeros((z_dim, x_dim, y_dim), dtype=np.uint16)
    for new_z, old_z in enumerate(original_order):
        with h5py.File(get_input_filename(old_z), "r") as f:
            vol[new_z] = f["mov"][t]
    
    # store reorganized volume dataset
    with h5py.File(get_output_filename(t), "w") as f:
        f.create_dataset("vol", data=vol, compression="gzip", compression_opts=9)
    
print("Completed reorganizing HDF5 files.")
