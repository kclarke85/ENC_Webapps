import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Streamlit app layout
st.title('Raspberry Pi Video Stream')

# Function to display video stream
def display_video():
    video_url = 'http://<raspberry_pi_ip>:5000/video_feed'  # Replace with the Raspberry Pi's IP address

    with st.spinner('Loading video stream...'):
        while True:
            response = requests.get(video_url, stream=True)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                st.image(img, caption='Video Stream', use_column_width=True, channels='BGR')
            else:
                st.error(f"Error accessing video stream. Status code: {response.status_code}")

# Display video stream in Streamlit app
if __name__ == '__main__':
    display_video()
