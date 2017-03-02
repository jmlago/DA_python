# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:16:56 2017

@author: JoseMaria
"""
import numpy as np
import plotly.offline as offline
import plotly.graph_objs as go
import pandas as pd
from sklearn.cluster import DBSCAN


def degrad(deg):
    """
    Degrees to Radiants
    """
    return deg*(np.pi/180)

def distance(loc1, loc2):
    """
    From latitude and longitude of two locations
    computes the distance (in meters) betweem them.
    This uses the ‘haversine’ formula.
    Not own-developed.
    """
    R=6371000           # Divide by 1000 to give the results in Km
    dLat = degrad(loc2[0] - loc1[0])
    dLon = degrad(loc2[1] - loc1[1])
    a = np.sin(dLat/2)**2 + np.cos(degrad(loc1[0]))* np.cos(degrad(loc2[0]))* np.sin(dLon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    d = R * c
    return d

sh = pd.read_csv('C:\\Users\\JoseMaria\\Desktop\\shameless_locations.csv')
pk = pd.read_csv('C:\\Users\\JoseMaria\\Desktop\\peaky_locations.csv')

def df_with_clusters(df):
    a = np.zeros((len(df.Lat),len(df.Lat)))
    i = 0
    for x in np.array([df.Lat,df.Lon]).transpose():
        j = 0
        for y in np.array([df.Lat,df.Lon]).transpose():
            a[i][j] = distance(x,y)
            j = j+1
        i = i+1
    cluster = DBSCAN(eps=300.0, min_samples=2, metric="precomputed", algorithm='auto')    
    cluster_components = cluster.fit_predict(a)
    df["Clusters"] = cluster_components

    return df

del pk["Unnamed: 0"]  
pk = df_with_clusters(pk).drop_duplicates()

# Map printing (from Jose Maria)
def clustered_plot(ddff):
    mapbox_access_token = 'pk.eyJ1IjoiY2hlbHNlYXBsb3RseSIsImEiOiJjaXFqeXVzdDkwMHFrZnRtOGtlMGtwcGs4In0.SLidkdBMEap9POJGIe1eGw'
    predata = []
    for i in range(-1,ddff.Clusters.max()):
        a = go.Scattermapbox(
                lat=ddff[(ddff["Clusters"] == i)]["Lat"],
                lon=ddff[(ddff["Clusters"] == i)]["Lon"],
                mode='markers',
                marker=go.Marker(
                    size=14
                ),
            )
        predata.append(a)
    data = go.Data(predata)
    
    layout = go.Layout(
        width=3840,
        height=2160,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            pitch=0,
            zoom=0
        ),
    )
    
    fig = dict(data=data, layout=layout)
    offline.plot(fig, filename='Peaky blinders Mapbox.html', validate=False)

clustered_plot(pk)