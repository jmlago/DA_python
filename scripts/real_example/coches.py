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
title = soup.find('div',attrs={"class":"mt-SerpList"}).findAll('span')
price = soup.find('div',attrs={"class":"mt-SerpList"}).findAll('strong')
attribute = soup.find('div',attrs={"class":"mt-SerpList"}).findAll('li')

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

##you need to change the directory to your directory
os.chdir("/home/josem/Documentos/PythonCourse/exemples/exemple1")

from cocheslib import buildurl,dfandstats

urlaudi = buildurl("audi","ANY",999999,0,250000,0,"")

dfaudi = dfandstats(urlaudi)

dfaudi.tail(80)
dfaudi["Year"].mean()
dfaudi["Price €"].mean()
dfaudi["Km"].mean()


##otherone is to do some statistics with the data
'''
We want to do some beauty plots to do some descriptive statistics
So for each brand we can do the plot of the price as a function of the years
and compare the line-plots

Another plot is to plot in a 3 dimension space, plot(km.mean,price.mean,year.mean) and change the 
color for each brand
so the brand which is closer to (0,0,inf) is "the best brand"

Buscar els outliers que seran les possibles ganges i mostrar el nom
'''
##initialize all dataframes
urlam = buildurl("aston_martin","ANY",999999,0,250000,0,"")
dfam = dfandstats(urlam)

urlfe = buildurl("ferrari","ANY",999999,0,250000,0,"")
dffe = dfandstats(urlfe)

urlamb = buildurl("lamborghini","ANY",999999,0,250000,0,"")
dflamb = dfandstats(urlamb)

##import interactive plots
from bokeh.plotting import figure, show

p = figure(plot_width=1080, plot_height=720, x_range=(1970,2020), y_range=(0,500000),
           title="SuperCars by brand")

p.circle(x=dfam["Year"], y=dfam["Price €"],
         color="grey", alpha=0.5,radius=0.3,legend="Aston Martin")
p.circle(x=dflamb["Year"], y=dflamb["Price €"],
         color="orange", alpha=0.5,radius=0.3,legend="Lamborghini")
p.circle(x=dffe["Year"], y=dffe["Price €"],
         color="red", alpha=0.5,radius=0.3,legend="Ferrari")

p.legend.location = "top_left"
show(p)

##We can not reuse this code at all because of the colors in the plot, 
##the labels and this stuff

##Let's do some statistics
import statsmodels.api as sm

mod = sm.OLS(dfaudi["Price €"],dfaudi["Year"])
res = mod.fit()
print(res.summary())
sm.stats.linear_rainbow(res)


