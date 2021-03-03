from urllib.parse import uses_relative
from numpy.core.fromnumeric import trace
from pandas.io.sql import table_exists
import streamlit as st
import numpy as np 
import pandas as pd
import base64 
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np 
# Import tracks.py for track names
import tracks

st.markdown('''
# 2021 Formula 1 Web Application
Display upcoming F1 2021 schedule

**Developed by/using**
- Author: [Kyle Martin](https://github.com/Kymartin45)
- Built in `Python` using `pandas`, `streamlit`, and `numpy`
''')
st.write('---')
st.subheader('2021 F1 Track Schedule')

st.sidebar.header('Track Information')
trackName = st.sidebar.selectbox('Tracks', tracks.trackNames)

def getTrack(trackName):
    url = "https://www.racefans.net/2021-f1-season/2021-f1-calendar/"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop([df.Forum == 'Forum'].index)
    raw = raw.fillna(0)
    trackStats = raw.drop(['td'], axis=0)
    return trackStats
    
trackStats = getTrack(trackName)
