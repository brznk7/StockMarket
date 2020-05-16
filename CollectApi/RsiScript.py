# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:09:28 2020

@author: safa
"""

import numpy as np
import pandas as pnd

#Data = pnd.read_pickle('CompanyData.pkl')
#StockName = 'ACSEL'
Period = 14
#Closes = np.array(Data[StockName]['Close'])
Closes = [54.8,56.8,57.85,59.85,60.57,61.1,62.17,60.6,\
         62.35,62.15,62.35,61.45,62.8,61.37,62.5,62.57,\
         60.8,59.37,60.35,62.35,62.17,62.55,65.55,64.37,\
         65.3,64.42,62.9,61.6,62.05,60.05,59.7,60.9,60.25,\
         58.27,58.7,57.72,58.1,58.2]
Closes = np.array(Closes)
#Closes = np.flip(Closes)
## Up & Down
Up = np.zeros((Closes.size,1))
Down = np.zeros((Closes.size,1))
for i in range(Closes.size-1):
    if Closes[i+1] >= Closes[i]:
        Up[i+1] = Closes[i+1] - Closes[i]
    elif Closes[i+1] <= Closes[i]:
        Down[i+1] = Closes[i] - Closes[i+1]

## 
UpAve = np.zeros((Closes.size,1))
DownAve = np.zeros((Closes.size,1))
RS = np.zeros((Closes.size,1))
RSI = np.zeros((Closes.size,1))
for i in np.arange(Period,Closes.size,1):
    ## UP AVERAGE & DOWN AVERAGE
    if i == Period:
        UpAve[i] = Up[i-14:i].sum() / Period
        DownAve[i] = Down[i-14:i].sum() / Period
    else:
        UpAve[i] = (UpAve[i-1]*(Period-1)+Up[i]) / Period
        DownAve[i] = (DownAve[i-1]*(Period-1)+Down[i]) / Period
        
    ## RELATIVE STREGTH
    RS[i] = UpAve[i] / DownAve[i]
    ## RELATIVE STREGTH INDEX
    RSI[i] = 100 - (100/(1 + RS[i]))

import matplotlib.pyplot as plt
Date = np.arange(0,38,1)
plt.plot(Date,RSI)