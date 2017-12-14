#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:09:15 2016

This code is not fast because it needs to access to many many many urls
so if someone wants to execute to find very big query he will needs to
wait for too long.

@author: Jose Maria
"""
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pandas as pd

def urllist_flickr(keywords):
    """
    From the string keywords, find all urls of all photos
    that the API flickr.photos.search thinks that are photos
    related with this keywords.
    """
    url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=8fc5524e10ce3c2ee2e616f146239721&text="+keywords.replace(" ","+")+"&format=rest"
    page = urlopen(url)
    soup = BeautifulSoup(page,"lxml")
    totalph = str(soup)
    reg = re.findall("((total=\")+([-+]?\d+[\.]?\d*[eE]?[-+]?\d*)+\")",totalph)
    for el in reg:
        reg = list(el)
    print(reg)
    reg = int(reg[2])
    nump = int(np.ceil(reg/100))
    urllist = []
    for i in range(1,nump):
        url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=8fc5524e10ce3c2ee2e616f146239721&text="+keywords.replace(" ","+")+"&format=rest&page="+str(i)
        page = urlopen(url)
        soup = BeautifulSoup(page,"lxml")
        totalph = soup.findAll('photo')
        for j in range(len(totalph)):
            urlbase="https://www.flickr.com/photos/"+totalph[j]["owner"]+"/"+totalph[j]["id"]+"/"
            urllist.append(urlbase)
    return urllist
    
def geoloc(url):
    """
    This functions returns two floats that are the 
    latitude and the longitude of the photo in flickr 
    corresponding to the url.
    """
    page = urlopen(url)
    soup = BeautifulSoup(page,"lxml")
    info = str(soup)
    reg = re.findall("((\"longitude\")+(:[-+]?\d+[\.]?\d*[eE]?[-+]?\d*)|(\"latitude\")+(:[-+]?\d+[\.]?\d*[eE]?[-+]?\d*))",info)
    numb = []
    for el in reg:
        el = list(el)
        for num in el:
            numb.append(num[11:].replace(":","")) 
    
    a=0
    for el in numb:
        if el == "":
            a=a+1
    for i in range(a):
        numb.remove("")
    numb = np.array(numb).astype(float)
    return numb

def geo_loc_df(text):
    """
    Uses previous functions to build a dataframe
    with latitudes and longitudes of all photos with
    the target text in flickr
    """
    urllist = urllist_flickr(text)
    print("URLs are ready")
    geo_locations = []
    for url in urllist:
        geo_locations.append(geoloc(url))
    print("Now we have all locations")
    geo_loc_df_data = []
    for el in geo_locations:
        if len(el) == 2:
            geo_loc_df_data.append(el)
    geo_loc_df = pd.DataFrame(geo_loc_df_data,columns=["Lat","Lon"])
    return geo_loc_df

#########################################################
text_of_request = "peaky blinders"##this is the example
#########################################################    

##Also this is part of the example of usage
peaky_df = geo_loc_df(text_of_request)
