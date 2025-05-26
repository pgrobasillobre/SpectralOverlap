
from __future__ import division

import sys
import re
import numpy as np
import time
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d


# ==============================================================================
#                            Spectral Overlap Calculator
# ==============================================================================
#
# Description:
#   This script computes the spectral overlap between two spectra — typically
#   the emission spectrum of a donor molecule and the absorption spectrum of
#   an acceptor molecule — as a function of photon energy (in eV).
#
# Usage:
#   python3 spectral_overlap.py donor_emission.csv acceptor_absorption.csv
#
# Inputs:
#   donor_emission.csv       - Emission spectrum data (2 columns: Energy [eV], Intensity)
#   acceptor_absorption.csv  - Absorption spectrum data (2 columns: Energy [eV], Absorbance)
#
# Output:
#   - Prints the spectral overlap integral (in eV⁻¹)
#   - Saves normalized interpolated spectra as:
#       • data1_norm.csv (donor)
#       • data2_norm.csv (acceptor)
#
# Example Data:
#   The directory `absorption-emission-example/` contains example spectra:
#     • znpc-abs.csv  — Absorption spectrum of ZnPc
#     • pdpc-em.csv   — Emission spectrum of PdPc
#
#   These example files are based on spectral data from the study:
#     Nature Chemistry (2022), https://doi.org/10.1038/s41557-021-00697-z
#
# Dependencies:
#   numpy, scipy, matplotlib
#
# Author:
#   Pablo Grobas Illobre
#
# ==============================================================================


# --> Initialize variables
min_energy    = 1.872   # Minimum Energy for the convoluted spectra in eV
max_energy    = 1.950   # Maximum Energy for the convoluted spectra in eV
grid_points   = 100000  # Number of energy points in the spectral range

# --> Conversion factors
ev_to_hartree = 1.0/27.211399


# ==============================
#           FUNCTIONS
# ==============================

def read_command_line(command_line):

   if len(sys.argv) < 2:
      print('')
      print('')
      print('   Please provide inputs files:')
      print('')
      print('      For more details --> python3 fret_coulomb.py -h')
      print('')
      print('')
      sys.exit()

   elif sys.argv[1] == '-h' or sys.argv[1] == '-help':
      print('')
      print('')
      print(' Execution --> python3 spectral_overlap_from_exp.py file1.csv file2.csv')
      print('')
      print('')
      sys.exit()

   else:
      return(sys.argv[1],sys.argv[2])
 

# -----

def read_data(infile):
   
   data = []
   ev   = []
   with open(infile,'r') as f:

      lines = f.readlines()
      for line in lines:
         if not line.startswith('#'):
            ev.append(float(line.split()[0]))
            data.append(float(line.split()[1]))

   return(ev,data)

# -----

def print_interpolated_data(name,ev,data):

   with open(name,'w') as f:

      for ev_,data_ in zip(ev,data):

         f.write(f'{ev_}  {data_} \n')

# -----


          
# ==============================
#         MAIN PROGRAM 
# ==============================


# START TIMER
start = time.time()


# --> Read command line, excitation energies and oscillator strengths
file_1, file_2 = read_command_line(sys.argv)

# Create an array of energy values in the specified range
energies = np.linspace(min_energy+0.01, max_energy-0.01, grid_points)

# --> Create Gaussian convolution
ev_1, data_1 = read_data(file_1)
ev_2, data_2 = read_data(file_2)

# --> Create an interpolation function and interpolate
interpolation_function_1 = interp1d(ev_1, data_1, kind='linear')
data_interpolated_1 = interpolation_function_1(energies)

# --> Create an interpolation function and interpolate
interpolation_function_2 = interp1d(ev_2, data_2, kind='linear')
data_interpolated_2 = interpolation_function_2(energies)


# Normalize each dataset
integral_1 = np.trapz(data_interpolated_1, energies)
integral_2 = np.trapz(data_interpolated_2, energies)

data_interpolated_1_normalized = data_interpolated_1 / integral_1
data_interpolated_2_normalized = data_interpolated_2 / integral_2

# print normalized data
print_interpolated_data('data1_norm.csv',energies,data_interpolated_1_normalized)
print_interpolated_data('data2_norm.csv',energies,data_interpolated_2_normalized)


## --> Calculate the overlap using numerical integration (area under the product of the two Gaussians)
overlap = np.trapz(data_interpolated_1 * data_interpolated_2, energies) 


# END TIMER
end = time.time()

print('')
print('   ===============================================')
print('')
print('     Spectral Overlap (eV^-1): ' + str(overlap))
print('                              ')
print('     -------------------------------------------')
print('')
print('     NORMAL TERMINATION')
print('')
print('     COMPUTATIONAL TIME: ', str(round(end-start,2)), ' s')
print('')
print('   ===============================================')
print('')




# ==============================
#         MAIN PROGRAM 
# ==============================








