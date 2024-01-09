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
    'Negative': df_negative['your_negative_field'],  # Replace 'your_negative_field' with the actual field name
    'Positive': df_positive['your_positive_field']   # Replace 'your_positive_field' with the actual field name
})

# Rest of the code remains unchanged
# ...
