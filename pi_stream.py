import streamlit as st
import stripe
from pymongo import MongoClient

# Assuming you have already set up a MongoDB client and a database
#connection_string = 'mongodb+srv://Subc-36597421.mongo.ondigitalocean.com'
#db = mongo_client["webapp_subscribe"]

# Replace these with your MongoDB credentials
MONGO_URI = "mongodb+srv://doadmin:NX09a6Z7m28K3d1E@Subc-36597421.mongo.ondigitalocean.com/webapp_subscribe?tls=true&authSource=admin&replicaSet=Subc"
# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client.get_database()


# Assuming 'collection_name' is the name of the collection you want to use
collection = db['subscriber']

# Initialize Stripe with your API key
stripe.api_key = "your_stripe_api_key_here"

# Connect to MongoDB
# mongo_client = MongoClient('localhost', 27017)
# db = mongo_client["webapp_subscribe"]
# collection = db["subscriber"]

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
