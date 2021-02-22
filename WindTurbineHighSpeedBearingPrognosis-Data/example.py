from spectrum import Spectrogram, dolphin_filename, readwav
import scipy.io
import pandas as pd
from datetime import datetime
import numpy as np
from scipy import signal
import os

mat = []
path = '../WindTurbineHighSpeedBearingPrognosis-Data'
for file in os.listdir(path):
    if file.endswith('.mat'):
        date_time_obj = datetime.strptime(file[5:len(file)-4], '%Y%m%dT%H%M%SZ')
        my_dictionary = {
        "Date": None,
        "File": [], 
        }
        print(f'{path}/{file} - data {date_time_obj}')
        my_dictionary["Date"]=date_time_obj
        my_dictionary["File"]=scipy.io.loadmat(f'{path}/{file}')
        mat.append(my_dictionary)

from scipy import special
def calculate_kurtosis(Sxx,fs,f,windowSize,confidenceLevel):
    M4=[]
    M2 = []
    for value in Sxx:
        M4.append(np.mean(np.power(value, 2)))   
        M2.append(np.mean(value))   
    
    K = len(Sxx[0])
    SK=[] 
    if K<2:
        for index in range(len(M4)):
            SK.append(M4[index]/np.power(M2[index],2) - 2) 
        
    else:
        for index in range(len(M4)):
            SK.append((K+1)/(K-1)*M4[index]/np.power(M2[index],2) - 2)

    for index in range(len(SK)):
        if f[index]<= (fs/windowSize):
            SK[index]=0
        elif f[index]>= (fs/2-fs/windowSize):
            SK[index]=0
            
    alpha = 1 - confidenceLevel
    threshold = -np.sqrt(2)*special.erfcinv(2*(1-alpha/2))*(2/np.sqrt(K))
    return SK,threshold,M4,M2,K

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.mlab as mlab
plt.rcParams["figure.figsize"] =(22,15)
fig = plt.figure()
ax = fig.gca(projection='3d')
confidenceLevel=0.950 
fs = 97656
window = window = signal.windows.kaiser(1024, beta=20)

ax.set_xlim3d(50000,0) 
ax.set_ylim3d(50, 0) 
for i in range(1): 
    e = mat[i]["File"]['vibration'].flatten() 
    p= Spectrogram(mat[i]["File"]['vibration'].flatten() ,W=513,  sampling=fs ,ws = 128) 
    p.periodogram()
     
p.plot()