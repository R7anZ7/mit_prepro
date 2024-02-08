import os
import h5py

# get original order
original_order = \
    [0, 29, 1, 28, 2, 27, 3, 26, 4, 25, 5, 24, 6, 23, 7, \
     22, 8, 21, 9, 20, 10, 19, 11, 18, 12, 17, 13, 16, 14, 15]

# number of z planes
z_dim = len(original_order)

# make paths
base_path = "/data1/rubinov_lab/yantong/project/MIT_dataset"
input_path = os.path.join(base_path, "original_data")
output_path = os.path.join(base_path, "organized_data")
os.makedirs(output_path, exist_ok=True)

# make functions to easily get input and output filenams
get_input_filename = lambda i: os.path.join(input_path, "stitch_layer_{}.hdf5".format(i))
get_output_filename = lambda i: os.path.join(output_path, "timepoint_{:05d}.hdf5".format(i))

# get dimensions using first plane dataset
with h5py.File(get_input_filename(0), "r") as f:
    t_dim, x_dim, y_dim = f["mov"].shape

# create empty volumes
for t in range(t_dim):
    with h5py.File(get_output_filename(t), "w") as f:
        f.create_dataset("data", (z_dim, x_dim, y_dim), compression="gzip")

# loop over z planes
for new_z, old_z in enumerate(original_order):
    
    # extract z plane data for all timepoints
    with h5py.File(get_input_filename(old_z)) as f:
        z_data = f["mov"][()]
    
    # loop over time points
    for t in range(t_dim):
        # store timepoint data for individual z planes
        with h5py.File(get_output_filename(t), "r+") as f:
            f["data"][new_z] = z_data[t]
    
print("Completed reorganizing HDF5 files.")
