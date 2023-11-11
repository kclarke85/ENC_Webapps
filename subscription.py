# import streamlit as st
#
# # Set the page layout to have a centered title
# st.set_page_config(layout="wide")
#
# # Embed a logo on the left
# st.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=100)
#
# # Create the horizontal banner using HTML and CSS
# st.write(
#     """
#     <style>
#         .banner {
#             background-image: url('https://media.istockphoto.com/id/1160249819/photo/busy-city-intersection-with-technology-theme.jpg?s=612x612&w=0&k=20&c=FxT76zRLGmAmdlJsDqiSKiaGRdarQGt1JuBatq6l7N0=');
#             background-size: cover;
#             height: 100px;
#             width: 100%;
#         }
#     </style>
#     <div class="banner"></div>
#     """,
#     unsafe_allow_html=True
# )
#
# # Create the text entry fields for subscription information
# st.write("Subscription Information")
# col1, col2 = st.columns(2)
#
# with col1:
#     first_name = st.text_input("First Name")
#     last_name = st.text_input("Last Name")
#
# with col2:
#     email = st.text_input("Email")
#     phone = st.text_input("Phone")
#
# # Create additional subscription information fields
# col3, col4 = st.columns(2)
#
# with col3:
#     address = st.text_area("Address")
#     postal_code = st.text_input("Postal Code")
#
# with col4:
#     city = st.text_input("City")
#     country = st.text_input("Country")
#
# # Add custom CSS to change the button color to blue
# st.markdown(
#         """
#         <style>
#         .stButton > button {
#             background-color: #0074E4;
#             color: white;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
#
#
# # Create additional information fields
# st.write("  ")
# col3, col4 = st.columns(2)
#
# if st.button("Submit"):
#   st.success("Form submitted!")

import streamlit as st
import stripe

# Initialize Stripe with your API key
stripe.api_key = "your_stripe_api_key_here"

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

# Create the text entry fields for subscription information
st.write("Subscription Information")
col1, col2 = st.columns(2)

with col1:
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")

with col2:
    email = st.text_input("Email")
    phone = st.text_input("Phone")

# Create additional subscription information fields
col3, col4 = st.columns(2)

with col3:
    address = st.text_area("Address")
    postal_code = st.text_input("Postal Code")

with col4:
    city = st.text_input("City")
    country = st.text_input("Country")

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

if st.button("Submit"):
    # You can add payment processing logic here
    # For example, if using Stripe, you can create a payment intent and display credit card input fields

    # Example: Create a payment intent
    payment_intent = stripe.PaymentIntent.create(
        amount=1000,  # Replace with the actual amount in cents
        currency="usd",
    )

    # Display credit card input fields using Stripe Elements
    st.write("Credit Card Information")
    card_number = st.text_input("Card Number", type="password")
    card_expiry = st.text_input("Expiration (MM/YY)")
    card_cvc = st.text_input("CVC", type="password")

    # Submit the payment
    if st.button("Pay"):
        try:
            # Use Stripe API to confirm the payment
            payment_intent.confirm(
                payment_method="card",
                payment_method_options={"card": {"number": card_number, "cvc": card_cvc, "exp_month": card_expiry[:2], "exp_year": card_expiry[-2:]}}
            )
            st.success("Payment successful!")
        except stripe.error.CardError as e:
            st.error(f"Payment failed: {e.error.message}")
