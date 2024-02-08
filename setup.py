# set up
import os
import pprint
import voluseg

voluseg.update()

# set and save parameters
parameters0 = voluseg.parameter_dictionary()

# disable parallelism
parameters0['parallel_volume'] = False
parameters0['parallel_clean'] = False

# set paths
parameters0['dir_ants'] = '/home/zhuy37/.conda/pkgs/ants-2.5.0-h00ab1b0_4/bin'
parameters0['dir_input'] = '/data1/rubinov_lab/yantong/project/MIT_dataset/organized_data'
parameters0['dir_output'] = '/data1/rubinov_lab/yantong/project/MIT_dataset/output'

# input data parameters
parameters0['res_x'] = 0.73             # x resolution (microns)
parameters0['res_y'] = 0.73             # y resolution (microns)
parameters0['res_z'] = 5.86             # z resolution (microns)
parameters0['f_volume'] = 200.8         # acquisition frequency
parameters0['t_section'] = 0            # plane image time (seconds)
parameters0['t_baseline'] = 5           # timescale for computing baseline (seconds)

# data processing parameters
parameters0['diam_cell'] = 6.0          # cell diameter (microns)
parameters0['ds'] = 2                   # spatial downsampling

voluseg.step0_process_parameters(parameters0)

# load and print parameters
filename_parameters = os.path.join(parameters0['dir_output'], 'parameters.pickle')
parameters = voluseg.load_parameters(filename_parameters)
pprint.pprint(parameters)

print("process volumes.")
voluseg.step1_process_volumes(parameters)

print("align volumes.")
voluseg.step2_align_volumes(parameters)

print("mask volumes.")
voluseg.step3_mask_volumes(parameters)

print("detect cells.")
voluseg.step4_detect_cells(parameters)

print("clean cells.")
voluseg.step5_clean_cells(parameters)

print("finished.")
