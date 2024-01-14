import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from pymongo import MongoClient
from plotly.subplots import make_subplots
import plotly.figure_factory as ff

# Set the page layout to have a centered title
st.set_page_config(layout="wide")

# Connect to MongoDB
client = MongoClient("mongodb+srv://doadmin:NX09a6Z7m28K3d1E@Subc-36597421.mongo.ondigitalocean.com/webapp_subscribe?tls=true&authSource=admin&replicaSet=Subc")
db = client["webapp_subscribe"]
negative_collection = db['spoken_negative_words']
positive_collection = db['all_words_phrases']

# Dropbox access token
DROPBOX_ACCESS_TOKEN = 'your_dropbox_access_token'

# Dropbox video path
DROPBOX_VIDEO_PATH = '/remote/out.mp4'

# Fetch video from Dropbox
response = requests.post(
    'https://content.dropboxapi.com/2/files/download',
    headers={
        'Authorization': f'Bearer {DROPBOX_ACCESS_TOKEN}',
        'Dropbox-API-Arg': '{"path": "' + DROPBOX_VIDEO_PATH + '"}',
    }
)

# Save video locally
video_path = '/home/kclar/Encounter/Image/out_from_dropbox.mp4'
with open(video_path, 'wb') as video_file:
    video_file.write(response.content)

# Embed a logo on the left
st.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=100)

# Display the recorded video from Dropbox in Streamlit
st.video(video_path)
