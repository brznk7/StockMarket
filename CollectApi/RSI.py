# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:12:00 2020

@author: safa
"""
    
def RSI(Data,StockName,Period):
    import numpy as np
    Closes = np.array(Data[StockName]['Close'])
#    Closes = np.flip(Closes)
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
    return RSI
