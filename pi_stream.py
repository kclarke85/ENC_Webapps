import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://doadmin:NX09a6Z7m28K3d1E@Subc-36597421.mongo.ondigitalocean.com/webapp_subscribe?tls=true&authSource=admin&replicaSet=Subc")
db = client["webapp_subscribe"]
negative_collection = db['spoken_negative_words']
positive_collection = db['all_words_phrases']


# Load positive and negative data from MongoDB collections
positive_data = pd.DataFrame(list(positive_collection.find()))
negative_data = pd.DataFrame(list(negative_collection.find()))

# Create a Plotly Bubble Chart for positive and negative data
fig = px.scatter(positive_data, x='all_words_phrases', y='positive_data', size='your_size_column',
                 color='your_color_column', hover_data=['additional_columns'])
st.plotly_chart(fig)

# Create a table for positive and negative words
st.write("Positive Words:")
st.table(positive_data[['word_column_1', 'word_column_2']])

st.write("Negative Words:")
st.table(negative_data[['spoken_negative_words', 'negative_data']])

# Embed video from Dropbox
st.write("Embedded Video from Dropbox:")
video_url = "https://www.dropbox.com/scl/fi/3tmjbbkjdi920kw63fq2d/out.avi?rlkey=g2h7ly0v91hkraohltjk80fc2&dl=0/out.avi"
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

# To run the app, save the above code in a Python file (e.g., app.py) and run the following command in your terminal:
# streamlit run app.py

