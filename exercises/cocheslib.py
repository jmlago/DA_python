#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Analysis in Python

Example 1.lib

Author: Jose Maria Lago
"""


import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

import re

##first of all I analyzed the page for one day more or less
##and I found another way easier to build the url
## there are 70 brands and some subbrands

def buildurl(marca,GType,makm,mikm,mapr,miy,txt):
    if GType == "GASOLINA":
        GasType = "2"
    elif GType == "DIESEL":
        GasType = "1"
    else: GasType = "0"
    url2 = "http://www.coches.net/"+marca+"/segunda-mano/?pg=1&FuelTypeId="+str(GasType)+"&MaxKms="+str(makm)+"&MinKms="+str(mikm)+"&MinYear="+str(miy)+"&text="+str(txt).replace(" ","%20")
    print(url2)
    page = urlopen(url2)
    soup = BeautifulSoup(page,"lxml")
    #print(soup)
    iterations = soup.find('div',attrs={"class":"mt-SerpHeader u-flex--spaceBetween"}).find('strong',attrs={"class":"u-mr--small"}).string
    print(iterations)
    reg = re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", iterations)
    print(reg)
    regex = int(reg[0].replace('.',''))
    num = round(int(regex)/30)
    print(num)
    urllist = []
    for i in range(1,num+1):
        urllist.append("http://www.coches.net/"+marca+"/segunda-mano/?pg="+str(i)+"&FuelTypeId="+str(GasType)+"&MaxKms="+str(makm)+"&MinKms="+str(mikm)+"&MinYear="+str(miy)+"&text="+str(txt))
    return urllist
    
    
##build a dataframe with all the cars of the same brand
##for 9000 cars or more it'll take a while
def dfandstats(urllist):
    df = []
    for url in urllist:
        ##Make the soup
        page = urlopen(url)
        soup = BeautifulSoup(page,"lxml")
        
        
        ##Analize the tools of Chrome to see how the page encodes the data with the tag
        title = soup.find('div',attrs={"class":"mt-SerpList"}).findAll('span',attrs={"class":"mt-CardAd-titleHiglight"})
        price = soup.find('div',attrs={"class":"mt-SerpList"}).findAll('strong')
        attribute = soup.find('div',attrs={"class":"mt-SerpList"}).findAll('li',attrs={"class":"mt-CardAd-attribute"})
        
        ##initialize all variable lists that we want
        titles = []
        prices = []
        locality = []
        gas = []
        year = []
        numkm = []
        
        ##make the loops to full the lists also we need to pop the . , km and €
        for i in range(len(title)):
            if title[i].string[:6] != "Añadir":
                titles.append(title[i].string)
        
        for i in range(len(price)):
            prices.append(int(price[i].string[:-2].replace(".","")))
        
        for i in range(int(len(attribute)/4)):
            locality.append(attribute[4*i].string)
            gas.append(attribute[4*i+1].string)
            year.append(int(attribute[4*i+2].string))
            if attribute[4*i+3].string[:-3] == "N/D":
                numkm.append(None)
            else:
                numkm.append(int(attribute[4*i+3].string[:-3].replace(".","")))
    		
        ##put a correct data format
        d = []
        for i in range(len(titles)):
            d.append([titles[i],prices[i],locality[i],gas[i],year[i],numkm[i]])
        
        ##set the dataframe
        a = pd.DataFrame(data=d,columns=["Title","Price €","Locality","GasType","Year","Km"])        
        df.append(a)
        ##take a look
        #print(a.head(10))
        #print(a["Price €"].mean())
        #print(a["Year"].mean())
        #print(a["Km"].mean())
        df2 = pd.concat(df)
    return df2

