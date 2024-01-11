import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient
from plotly.subplots import make_subplots
import plotly.figure_factory as ff

# Connect to MongoDB
client = MongoClient("mongodb+srv://doadmin:NX09a6Z7m28K3d1E@Subc-36597421.mongo.ondigitalocean.com/webapp_subscribe?tls=true&authSource=admin&replicaSet=Subc")
db = client["webapp_subscribe"]
negative_collection = db['spoken_negative_words']
positive_collection = db['all_words_phrases']

# Load positive and negative data from MongoDB collections
positive_data = pd.DataFrame(list(positive_collection.find()))
negative_data = pd.DataFrame(list(negative_collection.find()))

# Create a bubble chart using Plotly Express
fig_bubble = px.scatter(
    positive_data,
    x='x',  # Replace with your actual x-axis column
    y='y',  # Replace with your actual y-axis column
    size='size',  # Replace with your actual size column
    color='marker_color',  # Color by marker_color column
    title='Two-Variable Bubble Chart',
    labels={'x': 'X-axis Label', 'y': 'Y-axis Label'},
    size_max=50  # Adjust size_max based on your data
)

# Create a Pie chart for positive and negative percentages
positive_percentage = len(positive_data) / (len(positive_data) + len(negative_data)) * 100
negative_percentage = len(negative_data) / (len(positive_data) + len(negative_data)) * 100

fig_pie = px.pie(
    names=['Positive', 'Negative'],
    values=[positive_percentage, negative_percentage],
    title='Positive vs. Negative Percentage'
)

# Create Tables using Figure Factory
table_positive = ff.create_table(positive_data.head())
table_negative = ff.create_table(negative_data.head())

# Create Subplots
fig = make_subplots(
    rows=1, cols=3,
    column_widths=[0.6, 0.2, 0.2],
    subplot_titles=['Bubble Chart', 'Positive Table', 'Negative Table']
)

# Add figures to subplots
fig.add_trace(fig_bubble['data'][0], row=1, col=1)
fig.add_trace(fig_pie['data'][0], row=1, col=2)
fig.add_trace(table_positive['data'][0], row=1, col=2)
fig.add_trace(table_negative['data'][0], row=1, col=3)

# Update layout
fig.update_layout(height=600, showlegend=False)

# Show the final layout
st.plotly_chart(fig)
