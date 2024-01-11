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

# Assuming your data has columns 'x', 'y', and 'size'
# Replace these column names with your actual column names
positive_data['marker_color'] = 'green'  # Set color for positive data
negative_data['marker_color'] = 'red'  # Set color for negative data

# Combine positive and negative data
combined_data = pd.concat([positive_data, negative_data])

# Create a bubble chart using Plotly Express
fig = px.scatter(combined_data,
                 x='x',  # Replace with your actual x-axis column
                 y='y',  # Replace with your actual y-axis column
                 size='size',  # Replace with your actual size column
                 color='marker_color',  # Color by marker_color column
                 title='Two-Variable Bubble Chart',
                 labels={'x': 'X-axis Label', 'y': 'Y-axis Label'},
                 size_max=50)  # Adjust size_max based on your data

# Show the chart
fig.show()

