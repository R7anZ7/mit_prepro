# set up
import os
import pprint
import voluseg


voluseg.update()
# set and save parameters
parameters0 = voluseg.parameter_dictionary()
parameters0['parallel_volume'] = False
parameters0['parallel_clean'] = False

parameters0['dir_ants'] = '/home/zhuy37/.conda/pkgs/ants-2.5.0-h00ab1b0_4/bin'
# alternative path: /accre/arch/easybuild/software/MPI/GCC/10.2.0/OpenMPI/4.0.5/ANTs/2.3.5/bin/antsRegistration
#/home/zhuy37/.conda/pkgs/ants-2.5.0-had84ea8_3/bin
#/home/zhuy37/.conda/envs/voluseg/bin
parameters0['dir_input'] = '/data1/rubinov_lab/yantong/project/MIT_dataset/organized_data'
parameters0['dir_output'] = '/data1/rubinov_lab/yantong/project/MIT_dataset/output'
# parameters0['registration'] = 'none'
parameters0['diam_cell'] = 6.0
parameters0['f_volume'] = 200.0
parameters0['t_section'] = 0
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

print("finished")
