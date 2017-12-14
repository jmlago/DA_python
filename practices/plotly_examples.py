# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 10:32:33 2017

@author: JoseMaria
"""

import random
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from numpy import * ## the same that above but this is bad :) 

##Plot a huge amount of boxplots

N = 30.     # Number of boxes

# generate an array of rainbow colors by fixing the saturation and lightness of the HSL representation of colour 
# and marching around the hue. 
# Plotly accepts any CSS color format, see e.g. http://www.w3schools.com/cssref/css_colors_legal.asp.
c = ['hsl('+str(h)+',50%'+',50%)' for h in linspace(0, 360, N)]

# Each box is represented by a dict that contains the data, the type, and the colour. 
# Use list comprehension to describe N boxes, each with a different colour and with different randomly generated data:
data = [{
    'y': 3.5*sin(pi * i/N) + i/N+(1.5+0.5*cos(pi*i/N))*random.rand(10), 
    'type':'box',
    'marker':{'color': c[i]}
    } for i in range(int(N))]

# format the layout
layout = {'xaxis': {'showgrid':False,'zeroline':False, 'tickangle':60,'showticklabels':False},
          'yaxis': {'zeroline':False,'gridcolor':'white'},
          'paper_bgcolor': 'rgb(233,233,233)',
          'plot_bgcolor': 'rgb(233,233,233)',
          }

py.plot(data)


#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------

##Plot a 3d surface

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

data = [
    go.Surface(
        z=z_data.as_matrix()
    )
]
layout = go.Layout(
    title='Example of 3d surface',
    autosize=False,
    width=1500,
    height=800,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='elevations-3d-surface')

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------

##Plot a beauty Histogram

x0 = np.random.randn(500)
x1 = np.random.randn(500)+1

trace1 = go.Histogram(
    x=x0,
    opacity=0.75
)
trace2 = go.Histogram(
    x=x1,
    opacity=0.75
)

data = [trace1, trace2]
layout = go.Layout(barmode='overlay')
fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='overlaid histogram')

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------


## Scatter plot of random numbers just to see another example 

##Prepare the data
n = 750
col = []
for i in range(250):
    for elem in ['rgb(0, 255, 0)', 'rgb(255, 0, 0)', 'rgb(0, 0, 255)']:
        col.append(elem)

        
trace0 = go.Scatter(
    x= np.random.rand(n).tolist(),
    y= np.random.rand(n).tolist(),
    mode='markers',
    marker=dict(
        color=col,
        #opacity=np.full([1,n],0.1),
        size= 100*np.random.rand(n),
    )
)

##Plot the results offline
data = [trace0]
py.plot(data, filename='Random-Scatter')