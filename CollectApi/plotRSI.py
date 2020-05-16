# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:52:44 2020

@author: safa
"""

import pandas as pnd
import numpy as np
from RSI import RSI
import matplotlib.pyplot as plt

Data = pnd.read_pickle('CompanyDataUpdated.pkl')
Period = 14
StockNames = list(Data.keys())


LowRsiLim = 20
HighRsiLim = 80

for StockName in StockNames:
    Time = Data[StockName].index
    Rsi = RSI(Data,StockName,Period)
    LowRsi = np.zeros(Time.size) + LowRsiLim
    HighRsi = np.zeros(Time.size) + HighRsiLim
    if Rsi[-1] < 35:
        fig, ax1 = plt.subplots()
        ax1.plot(Time,Rsi,'red')
        ax1.plot(Time,LowRsi,'black')
        ax1.plot(Time,HighRsi,'black')
        ax1.set_xlabel('time')
        ax1.set_ylabel('RSI',color = 'red')
        ax1.tick_params(axis='y', labelcolor='red')
        
        ax2 = ax1.twinx() 
        ax2.plot(Time,Data[StockName]['Close'],color = 'blue')
        ax2.set_ylabel('Price',color = 'blue')
        ax2.tick_params(axis='y', labelcolor='blue')
        plt.gcf().autofmt_xdate()
        plt.title(StockName)

#from RSIgit import rsiFunc
#RsiGit = rsiFunc(Data[StockName]['Close'],Period)
#ax1.plot(Time,RsiGit)
