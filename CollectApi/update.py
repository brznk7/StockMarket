# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:41:40 2020

@author: safa
"""

from YahooFinance import yahoo
import datetime as dt
import pandas as pnd

OldData = pnd.read_pickle(r'C:\Users\SAFA\Desktop\CollectApi\CollectApi\CompanyData.pkl')

start = dt.datetime(2020,5,13)
end = dt.date.today()

CurrentData = yahoo(start,end)

UpdatedData = dict()
for key in list(CurrentData.keys()):
    UpdatedData[key] = OldData[key].append(CurrentData[key])

pnd.to_pickle(UpdatedData,'CompanyDataUpdated.pkl')