import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://doadmin:NX09a6Z7m28K3d1E@Subc-36597421.mongo.ondigitalocean.com/webapp_subscribe?tls=true&authSource=admin&replicaSet=Subc")
db = client["webapp_subscribe"]
positive_collection = db["positive_collection"]
negative_collection = db["negative_collection"]
# Load positive and negative data from MongoDB collections
positive_data = pd.DataFrame(list(positive_collection.find()))
negative_data = pd.DataFrame(list(negative_collection.find()))

# Assuming 'all_words_phrases' and 'positive_data' are actual column names in your positive_data DataFrame
fig = px.scatter(positive_data, x='all_words_phrases', y='negative_data', size='word_size',
                 color='color_column', hover_data=['additional_columns'])
st.plotly_chart(fig)

# Create a table for positive and negative words
st.write("Positive Words:")
st.table(positive_data[['word_column_1', 'word_column_2']])

st.write("Negative Words:")
st.table(negative_data[['word_column_1', 'word_column_2']])

# Embed video from Dropbox
st.write("Embedded Video from Dropbox:")
video_url = "https://www.dropbox.com/s/your_dropbox_video_url"
st.video(video_url)

# Geolocation Chart (using a placeholder map for demonstration)
st.write("Geolocation Chart:")
st.map(your_geolocation_data)

# Run the Streamlit app
if __name__ == '__main__':
    st.title("Your Streamlit Dashboard")
    st.subheader("Subtitle or Description")
    st.sidebar.title("Sidebar Title")
    st.sidebar.subheader("Sidebar Subtitle")
    st.sidebar.markdown("Add other widgets and controls here.")
