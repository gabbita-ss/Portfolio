import numpy as np
import statistics as stats
import bmxobs as bmx
import matplotlib.pyplot as plt
import sys
sys.path.append("/home/chandrahas/Desktop/BMX/modules")
from denoise import denoise
from doppler_correct import correct_doppler as doppler

data1 = bmx.BMXObs("/home/chandrahas/Desktop/BMX/pas/210903_0000", channels = "110")
data2 = bmx.BMXObs("/home/chandrahas/Desktop/BMX/pas/211221_1600", channels = "110")

data_array1_1 = denoise(data1,"110",20000)
#data_array2_1 = denoise(data2, "111", 20000)
data_array1_2 = doppler(data1, "110", 3, data_from_source = False, data_array = data_array1_1)
data_array2_2 = doppler(data2, "111", 3, data_from_source = False, data_array = data_array2_1)

############ POST-PROCESSING ######################
mean1 = np.mean(data_array1_2, axis = 1)
mean2 = np.mean(data_array2_2, axis = 1)

################### PLOT ##########################
extent1 = [0,1,data1.freq[1][0],data1.freq[1][-1]]
im = plt.imshow(data_array1_2, cmap = "Blues", extent = extent1, aspect = 'auto')
plt.colorbar()
plt.show()

extent2 = [0,1,data2.freq[1][0],data2.freq[1][-1]]
im = plt.imshow(data_array2_2, cmap = "Blues", extent = extent2, aspect = 'auto')
plt.colorbar()
plt.show()

plt.plot(data1.freq[1], np.mean(data_array1_1, axis = 1), color = "r", label = "raw_day1")   
plt.plot(data1.freq[1], mean1, color = "g", label = "corrected_day1")
plt.plot(data2.freq[1], np.mean(data_array2_1, axis = 1), color = "b", label = "raw_day2")
plt.plot(data2.freq[1], mean2, color = "y", label = "corrected_day2")
plt.legend()
plt.yscale('linear')
plt.show()


