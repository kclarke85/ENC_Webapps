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
