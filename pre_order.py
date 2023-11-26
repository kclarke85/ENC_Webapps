import streamlit as st
from pymongo import MongoClient

# Replace these with your MongoDB credentials
MONGO_URI = "mongodb+srv://doadmin:NX09a6Z7m28K3d1E@Subc-36597421.mongo.ondigitalocean.com/webapp_subscribe?tls=true&authSource=admin&replicaSet=Subc"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client.get_database()
collection = db['preorder']

# ... (Rest of your code)

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
