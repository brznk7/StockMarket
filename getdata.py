# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:17:57 2020

@author: safa
"""

def CollectApi():
    import http.client
    import json
    conn = http.client.HTTPSConnection("api.collectapi.com")
    
    headers = {
        'content-type': "application/json",
        'authorization': "apikey bla-bla"
        }
    
    conn.request("GET", "/economy/hisseSenedi", headers=headers)
    
    res = conn.getresponse()
    data = res.read()
    
    Data = json.loads(data.decode("utf-8"))
    return Data

    
