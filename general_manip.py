import numpy as np

import os, sys	
sys.path.insert(1, '/home/alex/Desktop/tfm-xisco/sci-vis/csv')
from io_csv import read_times_vals_csv_2d
#==============================================================================
def read_sim_params(directory:str)->dict:
	sim_params= {}
	with open(directory+"/sim_params.txt", "r") as f:
		for line in f:
			line= line.rstrip("\n").split(" ")
			sim_params[line[0]]= line[1]
	return sim_params
#==============================================================================
def extract_mean_asymp(file_name:str) -> (np.array, np.array):

	times, vals=  read_times_vals_csv_2d(file_name)

	nx, ny= vals[0].shape
	ptx= nx-1

	asymptotic_vals= [np.mean(step[ptx]) for step in vals]

	return (np.array(times), np.array(asymptotic_vals))
#==============================================================================
def extract_mean_horizon(file_name:str) -> (np.array, np.array):

	times, vals=  read_times_vals_csv_2d(file_name)

	nx, ny= vals[0].shape
	ptx= 0

	asymptotic_vals= [np.mean(step[ptx]) for step in vals]

	return (np.array(times), np.array(asymptotic_vals))