import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from streamlit.components.v1 

# Connect to MongoDB
client = MongoClient("mongodb+srv://doadmin:NX09a6Z7m28K3d1E@Subc-36597421.mongo.ondigitalocean.com/webapp_subscribe?tls=true&authSource=admin&replicaSet=Subc")
db = client["webapp_subscribe"]
negative_collection = db['spoken_negative_words']
positive_collection = db['all_words_phrases']

# Set the page layout to have a centered title
st.set_page_config(layout="wide")

# Embed a logo on the left
st.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=100)

# Embed video from Dropbox
st.write("RealTime Encounter:")
video_url = "https://www.dropbox.com/scl/fi/3tmjbbkjdi920kw63fq2d/out.avi?rlkey=g2h7ly0v91hkraohltjk80fc2&dl=0/out.avi"
st.video(video_url)
st.components.v1.iframe(video_url, width=640, height=360)
