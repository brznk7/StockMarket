# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:38:23 2020

@author: safa
"""

def yahoo(start,end,CompanyNames):
    import pandas_datareader.data as web
    import time
    
    CompanyData = dict()
    for name in CompanyNames:
        SearchName = name+'.IS'
        time.sleep(0.5)
        try:
            df = web.DataReader(SearchName,'yahoo',start,end)
            CompanyData[name] = df
        except:
            print(name)
    return CompanyData
    

