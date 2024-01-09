import pandas as pd
import plotly.express as px
import pydeck as pdk
import geocoder
import streamlit as st
from pymongo import MongoClient

# Replace these with your MongoDB credentials
MONGO_URI = "mongodb+srv://doadmin:NX09a6Z7m28K3d1E@Subc-36597421.mongo.ondigitalocean.com/webapp_subscribe?tls=true&authSource=admin&replicaSet=Subc"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client['your_database_name']  # Replace 'your_database_name' with your actual database name
negative_collection = db['spoken_negative_words']
positive_collection = db['all_words_phrases']

# Fetch data from MongoDB collections
negative_data = negative_collection.find({}, {'_id': 0})  # Exclude '_id' field from the result
positive_data = positive_collection.find({}, {'_id': 0})

# Convert MongoDB cursor to Pandas DataFrame
df_negative = pd.DataFrame(list(negative_data))
df_positive = pd.DataFrame(list(positive_data))

# Merge data frames on a common key if needed
# For example, assuming 'common_key' is a common field in both negative and positive data
# df = pd.merge(df_negative, df_positive, on='common_key', how='outer')

# Find the maximum number of lines in both DataFrames
max_lines = max(len(df_negative), len(df_positive))

# Pad the shorter list with empty strings to make them of equal length
df_negative = df_negative.reindex(range(max_lines)).fillna('')
df_positive = df_positive.reindex(range(max_lines)).fillna('')

# Create a DataFrame with two columns: 'Negative' and 'Positive'
df = pd.DataFrame({
    'Negative': df_negative['Negative'],  # Replace 'your_negative_field' with the actual field name
    'Positive': df_positive['Positive']   # Replace 'your_positive_field' with the actual field name
})

# Create a bubble chart using Plotly with red for negative and green for positive
data = pd.DataFrame({
    'File': ['Negative', 'Positive'],
    'Line Count': [len(df_negative), len(df_positive)]
})

fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Realtime Word Analysis', color='File')

# Get real-time geo-location of the computer
geo = geocoder.ip('me')

# Create a GeoMap using Pydeck
geo_data = pd.DataFrame({
    'Latitude': [geo.lat],
    'Longitude': [geo.lng],
})

# Set the page layout to have a centered title
st.set_page_config(layout="wide")
# Embed a logo on the left
st.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=100)

# Create a layout with three columns: one for the video, one for the chart, and one for the table
col1, col2, col3 = st.columns([1, 1, 1])

# Display the video stream in the first column
with col2:
    st.write('Encounter In Realtime')
    video_url = 'http://<raspberry_pi_ip>:5000/video_feed'  # Replace with the Raspberry Pi's IP address
    st.markdown(f'<video src="{video_url}" width="640" height="480" controls></video>', unsafe_allow_html=True)

# Display the bubble chart in the second column
with col1:
    st.plotly_chart(fig, use_container_width=True)

# Display the GeoMap in the third column
with col3:
    st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
    st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=geo.lat,
            longitude=geo.lng,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=geo_data,
                get_position=["Longitude", "Latitude"],
                get_radius=200,
                get_fill_color=[255, 0, 0],  # Red color
            ),
        ],
    ))

# Create a container for the table and the paragraph text
col = st.columns([2, 1])  # Adjust the width ratio as needed

# Display the combined table with negative and positive data values in the first column
with col[0]:
    st.write('Combined Phrases')
    st.dataframe(df, width=810)  # Adjust the width as needed
    # Use CSS to style and align the attached text to the right of the table in the second column
with col[1]:
    st.markdown(
        """
        <div style="text-align: left; padding-left: 10px;">
            Oftentimes the intersection of positive words in a conversation can blend with negative words. 
            Occurring in an argument or confrontation, The Encounter Engineering platform provides a real-time monitor of this type of interaction. 
            So when your loved one that wears our wearable technology has a negative interaction based on the usage of dangerous keywords, 
            the loved one is now empowered to advocate in real-time. You should either call the police or call a bondsman. 
            You may also need to, depending on the interaction, call a lawyer or even the State Department embassy if traveling abroad. 
            With the awareness of the international and the ability to share with your community, law enforcement, and or legal defense makes this platform very powerful. 
            Always Aware, Always Safe, Always an advocate.
        </div>
        """,
        unsafe_allow_html=True
    )
