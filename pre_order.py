import streamlit as st
from pymongo import MongoClient

# Replace these with your MongoDB credentials
MONGO_URI = "mongodb+srv://doadmin:NX09a6Z7m28K3d1E@Subc-36597421.mongo.ondigitalocean.com/webapp_subscribe?tls=true&authSource=admin&replicaSet=Subc"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client.get_database()
collection = db['preorder']

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

# Create the text entry fields for preorder information
st.write("Pre Order Information")
col1, col2 = st.columns(2)

with col1:
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    address = st.text_area("Address")
    city = st.text_input("City")
    state = st.text_input("State")
    zip_code = st.text_input("Zip Code")
    
with col2:
    product_name = st.text_input("Product Name")
    product_quantity = st.number_input("Quantity", min_value=1, step=1)
    phone_number = st.text_input("Phone Number")
    email = st.text_input("Email")

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

# If the Preorder button is clicked
if st.button("Submit"):
    # Get the preorder information
    preorder_info = {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "city": city,
        "state": state,
        "zip_code": zip_code,
        "product_name": product_name,
        "product_quantity": product_quantity,
        "phone_number": phone_number,
        "email": email
    }

    # Insert the preorder information into the MongoDB collection
    collection.insert_one(preorder_info)

    # Additional logic for payment processing using Stripe (if needed)

    # For demonstration purposes, we're just printing the order details here
    st.success(f"Preorder submitted successfully!\n\nProduct: {product_name}\nQuantity: {product_quantity}\nLast Name: {last_name}\nFirst Name: {first_name}\nAddress: {address}\nCity: {city}\nState: {state}\nZip Code: {zip_code}\nPhone Number: {phone_number}\nEmail: {email}")

# Add trademark at the bottom
st.write("©Encounter Engineering, All rights reserved.")
