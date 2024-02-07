import h5py
import numpy as np
import os

original_to_new_order = [0, 29, 1, 28, 2, 27, 3, 26, 4, 25, 5, 24, 6, 23, 7, 22, 8, 21, 9, 20, 10, 19, 11, 18, 12, 17, 13, 16, 14, 15]

new_to_original_order = sorted(range(len(original_to_new_order)), key=lambda k: original_to_new_order[k])

file_path_template = "/data1/rubinov_lab/yantong/project/MIT_dataset/original_data/stitch_layer_{:03d}.hdf5"

output_path_template = "/data1/rubinov_lab/yantong/project/MIT_dataset/organized_data/timepoint_{:05d}.hdf5"

output_dir = os.path.dirname(output_path_template)

os.makedirs(output_dir, exist_ok=True)

z_planes = len(original_to_new_order)
timepoints = 6700
x_dim, y_dim = 505, 1280

for t in range(timepoints):

    data_for_current_timepoint = np.zeros((z_planes, x_dim, y_dim), dtype=np.uint16)

    for z in range(z_planes):

        original_index = new_to_original_order[z]

        file_path = file_path_template.format(original_index)

        with h5py.File(file_path, 'r') as f:

            data_for_current_timepoint[z] = f['mov'][t, :, :]

    output_path = output_path_template.format(t+1)  

    with h5py.File(output_path, 'w') as f:

        f.create_dataset('mov', data=data_for_current_timepoint, compression="gzip", compression_opts=9)

print("Completed reorganizing HDF5 files.")

print("successfully created")