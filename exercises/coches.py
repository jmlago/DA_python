'''
Data Analysis in Python

Example 1

Author: Jose Maria Lago
'''

import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

##First take a look at the url to see how information is encoded (sometimes you can't)
url = "http://www.coches.net/segunda-mano/?MakeId=28&ModelId=0&PrvId=0&Version=&BodyTypeId=0&FuelTypeId=0&MaxKms=9999999&MinKms=0&MaxYear=9999&MinYear=0&fi=SortDate&or=-1&MaxPrice=0&SearchOrigin=2&text=mercedes__benz"
url2 = "http://www.coches.net/porsche/segunda-mano/?pg=5"
##Make the soup
page = urlopen(url2)
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

##take a look
print(a.head(10))
print(a["Price €"].mean())
print(a["Year"].mean())
print(a["Km"].mean())



##now two approaches, one is to build this into functions for reuse
'''
It's really easy to make a function that recives and URL and returns the DataFrame

Another function that we can do is analysing the url to build some "url constructor"
'''

##this is reusage and let's take a look at the library
import os

path_scripts = os.path.expanduser('~/DA_python/exercises')
##you need to change the directory to your directory
os.chdir(path_scripts)

from cocheslib import buildurl,dfandstats

##initialize all dataframes
urlam = buildurl("aston_martin","ANY",999999,0,250000,0,"")
dfam = dfandstats(urlam)

urlfe = buildurl("ferrari","ANY",999999,0,250000,0,"")
dffe = dfandstats(urlfe)

urlamb = buildurl("lamborghini","ANY",999999,0,250000,0,"")
dflamb = dfandstats(urlamb)

dfsupercars = dffe.append(dfam).append(dflamb)


urlaudi = buildurl("audi","ANY",999999,0,250000,0,"")
dfaudi = dfandstats(urlaudi)

dfaudi.to_csv(path_scripts+"audi_df.csv")
dfsupercars.to_csv(path_scripts+"supercars_df.csv")

## Categories and dummies
dflamb["CatLocality"] = pd.Categorical(dflamb["Locality"]).codes
pd.get_dummies(dflamb)


############## plotly ##############
##import interactive plots
import plotly.offline as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x = dffe["Year"],
    y = dffe["Price €"],
    mode = 'markers',
    marker= dict(size= 10,
                    color= "rgba(255, 0, 0, 1.0)",
                    opacity= 0.8
                   ),
    name = "Ferrari"
)
trace2 = go.Scatter(
    x = dfam["Year"],
    y = dfam["Price €"],
    mode = 'markers',
    marker= dict(size= 10,
                    color= "rgba(155, 155, 155, 1.0)",
                    opacity= 0.8
                   ),
    name = "Aston Martin"
)
trace3 = go.Scatter(
    x = dflamb["Year"],
    y = dflamb["Price €"],
    mode = 'markers',
    marker= dict(size= 10,
                    color= "rgba(255, 200, 0, 1.0)",
                    opacity= 0.8
                   ),
    name = "Lamborghini"
)


data = [trace1,trace2,trace3]

# Plot and embed in HTML
py.plot(data, filename='Super-Cars')
