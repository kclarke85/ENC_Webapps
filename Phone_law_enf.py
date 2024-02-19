# from googlevoice import Voice
# import streamlit as st
#
# # Embed a logo on the left
# st.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=100)
# # Initialize the Google Voice client
# voice = Voice()
#
#
# # Function to initiate the call
# def make_call(phone_number):
#     try:
#         # Login to Google Voice (will prompt for credentials the first time)
#         voice.login(email='your_google_voice_email@gmail.com', passwd='your_google_voice_password')
#
#         # Initiate the call
#         voice.call(phone_number)
#         st.success("Call initiated successfully")
#     except Exception as e:
#         st.error(f"Error initiating call: {e}")
#
# # Main Streamlit app
# def main():
#     st.title("encounter Escalation")
#
#     # Disclaimer section with explanation
#     with st.expander("Why you shouldn't call 911 falsely?"):
#         st.write(
#             "Calling 911 falsely can divert emergency services away from genuine emergencies, potentially putting lives at risk. It can also lead to legal consequences and waste valuable resources. Please use 911 responsibly and only in genuine emergencies.")
#
#     # Checkbox for agreement
#     agree = st.checkbox("I agree to the terms and conditions", key='agree_checkbox')
#
#     # Change checkbox color to green when checked
#     if agree:
#         st.markdown("<style> .css-15f9baf input:checked { color: green; } </style>", unsafe_allow_html=True)
#
#     # Call button action
#     if agree and st.button("Call"):
#         make_call("911")
#
#     # Disable call button if checkbox is not selected
#     if not agree:
#         st.warning("Please agree to the terms and conditions before making a call")
#
#     # Copyright notice
#     st.write("Copyright © 2024 Encounter Engineering")
#
# if __name__ == "__main__":
#     main()


import streamlit as st
from twilio.rest import Client

# Embed a logo on the left
st.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=100)

# Twilio credentials
TWILIO_ACCOUNT_SID = 'ACeb2d0e8c0b5cc0425df6c91d3cfda3c9'
TWILIO_AUTH_TOKEN = '52c51d6106fb378a7de268d5b2ba1fd3'
TWILIO_PHONE_NUMBER = '+18333531388'

# Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Function to initiate the call
def make_call(outgoing_number):
    try:
        # Initiate the call
        call = client.calls.create(
            twiml='<Response><Say>Hello, this is your Twilio test call.</Say></Response>',
            to=outgoing_number,
            from_=TWILIO_PHONE_NUMBER
        )
        st.success("Call initiated successfully")
        st.write(f"Call SID: {call.sid}")
    except Exception as e:
        st.error(f"Error initiating call: {e}")

# Main Streamlit app
def main():
    st.title("Encounter Escalation")

    # Disclaimer section with explanation
    with st.expander("Why you shouldn't call 911 falsely?"):
        st.write(
            "Calling 911 falsely can divert emergency services away from genuine emergencies, potentially putting lives at risk. It can also lead to legal consequences and waste valuable resources. Please use 911 responsibly and only in genuine emergencies.")

    # Checkbox for agreement
    agree = st.checkbox("I agree to the terms and conditions", key='agree_checkbox')

    # Change checkbox color to green when checked
    if agree:
        st.markdown("<style> .css-15f9baf input:checked { color: green; } </style>", unsafe_allow_html=True)

    # Call button action
    if agree and st.button("Call"):
        outgoing_number = "16785201149"  # Replace with the phone number you want to call
        make_call(outgoing_number)

        # Embed the animation next to the call button for 10 seconds
        st.markdown(
            "<div><lottie-player src='https://cdnl.iconscout.com/lottie/premium/thumb/incoming-call-7137889-5800490.json' background='transparent' speed='1' style='width: 100px; height: 100px;' loop autoplay></lottie-player></div>",
            unsafe_allow_html=True)

        # Delay for 10 seconds
        st.markdown(
            "<script>setTimeout(function() { window.location.reload(); }, 10000);</script>",
            unsafe_allow_html=True)

    # Disable call button if checkbox is not selected
    if not agree:
        st.warning("Please agree to the terms and conditions before making a call")

    # Copyright notice
    st.write("Copyright © 2024 Encounter Engineering")

if __name__ == "__main__":
    main()
