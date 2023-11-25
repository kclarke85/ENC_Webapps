import streamlit as st
from pymongo import MongoClient

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

# Create the eight text entry fields
st.write("   ")
col1, col2 = st.columns(2)

with col1:
    first_name = st.text_input("First Name")
    email = st.text_input("Email")

with col2:
    last_name = st.text_input("Last Name")
    phone = st.text_input("Phone")

# Create additional information fields
#st.write("Additional Information")
col3, col4 = st.columns(2)

with col3:
    address = st.text_area("Address")
    city = st.text_input("City")

with col4:
    postal_code = st.text_input("Postal Code")
    country = st.text_input("Country")


