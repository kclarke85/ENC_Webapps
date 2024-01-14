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

# Display the recorded video from Dropbox in Streamlit with reduced width
st.video(response.content, width=480)
