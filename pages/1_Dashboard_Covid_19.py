import streamlit as st 
import pandas as pd
import numpy as np
import os
from matplotlib import image
import plotly.express as px


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images","covid.png")

img = image.imread(IMAGE_PATH)

st.image(img,width=200)

st.title('Dashboard :red[Covid 19]!')

st.write('The Covid 19 dataset')

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "covid_19.csv")

df=pd.read_csv(DATA_PATH)

st.dataframe(df)

country =st.selectbox('Select the region:',df['Country/Region'].unique())
col=st.selectbox("Select to analyse",df.columns)

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Country/Region'] == country ], x='Confirmed',y=col)
col1.plotly_chart(fig_1,use_container_width=True)
fig_2 = px.box(df[df['Country/Region'] == country], x='Confirmed',y=col)
col2.plotly_chart(fig_2,use_container_width=True)