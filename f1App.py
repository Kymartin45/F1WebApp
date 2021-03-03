from urllib.parse import uses_relative
import streamlit as st
import numpy as np 
import pandas as pd
import base64 
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np 
import tracks


st.title('F1 Schedule and Driver Statistics')
st.markdown("**Author: Kyle Martin**")
st.subheader('Web scraping 2021 F1 track schedule and driver statistics')

st.sidebar.header('Track Information')
trackName = st.sidebar.selectbox('Tracks', tracks.trackNames)

def getTrack(trackName):
    url = "https://www.formula1.com/en/racing/2021/" + str(trackName) + ".html"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    trackStats = raw.drop(['Rk'], axis=1)
    return trackStats
trackStats = getTrack(trackName)
    