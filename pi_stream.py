import streamlit as st
import requests

# Set the page layout to have a centered title
st.set_page_config(layout="wide")

# Dropbox access token
DROPBOX_ACCESS_TOKEN = 'sl.BtomJzI-qj3UJftIPlfQM46rRSPgGmgFQuGmXarIvKa8bcyu5edklJjNlw4itAGsf9_LfS2Paua_Nw07cYfN01bGSVNJj6SptoSpwEpt-aBwtIMeHttQXCH8pNSA91UyiOGjocrxgAk_e5a0_opmp9Y'

# Dropbox video path
DROPBOX_VIDEO_PATH = '/remote/mete-data/out.mp4'

# Set the page layout to have a centered title
st.set_page_config(layout="wide")

# Embed a logo on the left
st.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=100)

# Create the horizontal banner using HTML and CSS
st.write(
    """
    <style>
        .banner {
            background-image: url('https://media.istockphoto.com/id/1160249819/photo/busy-city-intersection-with-technology-theme.jpg?s=612x612&w=0&k=20&c=FxT76zRLGmAmdlJsDqiSKiaGRdarQGt1JuBatq6l7N0=');
            background-size: cover;
            height: 100px;
            width: 100%;
        }
    </style>
    <div class="banner"></div>
    """,
    unsafe_allow_html=True
)

# Add custom CSS to change the button color to blue
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #0074E4;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create additional information fields
st.write("  ")
col3, col4 = st.columns(2)
