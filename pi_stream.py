import streamlit as st
import requests

# Set the page layout to have a centered title
st.set_page_config(layout="wide")

# Dropbox access token
DROPBOX_ACCESS_TOKEN = 'sl.BtomJzI-qj3UJftIPlfQM46rRSPgGmgFQuGmXarIvKa8bcyu5edklJjNlw4itAGsf9_LfS2Paua_Nw07cYfN01bGSVNJj6SptoSpwEpt-aBwtIMeHttQXCH8pNSA91UyiOGjocrxgAk_e5a0_opmp9Y'

# Dropbox video path
DROPBOX_VIDEO_PATH = '/remote/mete-data/out.mp4'

# Fetch video from Dropbox
response = requests.post(
    'https://content.dropboxapi.com/2/files/download',
    headers={
        'Authorization': f'Bearer {DROPBOX_ACCESS_TOKEN}',
        'Dropbox-API-Arg': '{"path": "' + DROPBOX_VIDEO_PATH + '"}',
    }
)

# Embed a logo on the left
st.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=100)

# Display the recorded video from Dropbox in Streamlit with reduced width
st.video(response.content, width=480)
