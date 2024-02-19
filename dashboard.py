# import streamlit as st
# import pandas as pd
# import requests
# import plotly.express as px
# import geocoder
# from gtts import gTTS
# import io
# import pydeck as pdk
#
# # Function to read JSON data from the server and calculate sum
# def read_json_and_sum(endpoint):
#     url = f"http://192.168.1.69:5000/api/{endpoint}"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for bad status codes
#         data = response.json()
#
#         # Get total lines from JSON data
#         total_lines = len(data)
#         return total_lines
#     except requests.exceptions.HTTPError as http_err:
#         st.error(f"HTTP error occurred: {http_err}")
#     except Exception as err:
#         st.error(f"Error occurred: {err}")
#     return None
#
# # Function to generate speech
# def generate_speech():
#     message = "Hello, You received this link because a loved one is in a potentially dangerous situation. Perhaps a negative traffic stop, walking alone at night or anxious about a ride share. If the video shows a harmful situation, call 911 immediately. Or use the help links. If everything is ok give your loved one a call to follow up. We hope everything is ok. Let's keep our loved ones safe."
#     tts = gTTS(text=message, lang='en')
#     audio_fp = io.BytesIO()
#     tts.write_to_fp(audio_fp)
#     audio_fp.seek(0)
#     return audio_fp
#
# # # Display the sidebar with icon
# st.sidebar.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=True)
# st.sidebar.write("Here are some actions you can take:")
# st.sidebar.write("- Call Law Enforcement")
# st.sidebar.write("- Call Bail Bondsman")
# st.sidebar.write("- Share Video via Social Media")
# st.sidebar.write("- Ayuda En Español")
# st.sidebar.write("- Call Legal Aid")
#
# # Get real-time geo-location of the computer
# geo = geocoder.ip('me')
#
# # Display the video
# #st.title("Encounter Video")
# flask_video_url = "http://192.168.1.69:5000/video"  # Replace with actual video URL
# st.video(flask_video_url)
#
# # Button to explain
# # Button to explain
# button_html = """
#     <style>
#         .stButton>button {
#             background-color: #ADD8E6; /* Light Blue */
#         }
#     </style>
# """
# st.markdown(button_html, unsafe_allow_html=True)
#
# if st.button("Explain", key="explanation_button"):
#     with st.spinner("Generating Explanation..."):
#         audio_file = generate_speech()
#     st.audio(audio_file, format='audio/mp3', start_time=0)
#     st.success("Explanation Generated")
#
# # Get total lines from all_words_phrases.json and matched_neg_words.json
# total_lines_all_words = read_json_and_sum("all_words_phrases")
# total_lines_matched_neg = read_json_and_sum("matched_neg_words")
#
# # Create DataFrame for the bubble chart
# data = pd.DataFrame({
#     'File': ['all_words_phrases.json', 'matched_neg_words.json'],
#     'Total Lines': [total_lines_all_words, total_lines_matched_neg],
#     'Color': ['green', 'red']  # Assigning colors for bubble chart
# })
#
# # Plotly bubble chart
# fig = px.scatter(data, x='File', y='Total Lines', size='Total Lines', color='File',
#                  hover_name='File', size_max=50,
#                  color_discrete_map={"all_words_phrases.json": "green", "matched_neg_words.json": "red"})
#
# fig.update_layout(title="Safety Risk Analysis")  # Leave font size adjustment out here
#
# # Display the chart
# st.plotly_chart(fig)
#
# # Geolocation map
# st.markdown("<h1 style='font-size: larger;'>Subscriber Location</h1>", unsafe_allow_html=True)
# #st.markdown("<h1 style='font-size: smaller;'>Subscriber Location</h1>", unsafe_allow_html=True)
# #st.title("<span style='font-size: smaller;'>Subscriber Location</span>", unsafe_allow_html=True)
#
# layer = pdk.Layer(
#     'ScatterplotLayer',
#     data=pd.DataFrame({'Latitude': [geo.lat], 'Longitude': [geo.lng]}),
#     get_position='[Longitude, Latitude]',
#     get_radius=20000,
#     get_fill_color=[0, 255, 255],
#     pickable=True,
#     opacity=0.8,
# )
#
# map = pdk.Deck(
#     layers=[layer],
#     initial_view_state=pdk.ViewState(latitude=geo.lat, longitude=geo.lng, zoom=10),
# )
#
# st.pydeck_chart(map)
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import geocoder
from gtts import gTTS
import io
import pydeck as pdk
import subprocess

# Function to read JSON data from the server and calculate sum
def read_json_and_sum(endpoint):
    url = f"http://192.168.1.69:5000/api/{endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()

        # Get total lines from JSON data
        total_lines = len(data)
        return total_lines
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        st.error(f"Error occurred: {err}")
    return None

# Function to generate speech
def generate_speech():
    message = "Hello, You received this link because a loved one is in a potentially dangerous situation. Perhaps a negative traffic stop, walking alone at night or anxious about a ride share. If the video shows a harmful situation, call 911 immediately. Or use the help links. If everything is ok give your loved one a call to follow up. We hope everything is ok. Let's keep our loved ones safe."
    tts = gTTS(text=message, lang='en')
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

# # Sidebar with actions
# st.sidebar.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=True)
# st.sidebar.write("Here are some actions you can take:")
# st.sidebar.write("- Call Law Enforcement")
# st.sidebar.write("- Call Bail Bondsman")
# st.sidebar.write("- Share Video via Social Media")
# st.sidebar.write("- Ayuda En Español")
# st.sidebar.write("- Call Legal Aid")

# Function to run subprocess based on the label clicked
def run_streamlit_app(app_name):
    subprocess.Popen(["streamlit", "run", app_name])

# Function to run subprocess based on the label clicked
def run_streamlit_app(app_name):
    subprocess.Popen(["streamlit", "run", app_name])

# Sidebar with actions
st.sidebar.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=True)
st.sidebar.write("Here are some actions you can take:")

# Create text hyperlinks and call run_streamlit_app function on click
if st.sidebar.markdown("[Call Law Enforcement](http://localhost:8501/)"):
    run_streamlit_app("Phone_law_enf.py")
if st.sidebar.markdown("[Call Bail Bondsman](http://localhost:8502/)"):
    run_streamlit_app("program2.py")  # Change program2.py to the actual file name
if st.sidebar.markdown("[Share Video via Social Media](http://localhost:8503/)"):
    run_streamlit_app("program3.py")  # Change program3.py to the actual file name
if st.sidebar.markdown("[Ayuda En Español](http://localhost:8504/)"):
    run_streamlit_app("program4.py")  # Change program4.py to the actual file name
if st.sidebar.markdown("[Call Legal Aid](http://localhost:8505/)"):
    run_streamlit_app("program5.py")  # Change program5.py to the actual file name



# Get real-time geo-location of the computer
geo = geocoder.ip('me')

# Display the video
st.video("http://192.168.1.69:5000/video")  # No height adjustment

# Button to explain
if st.button("Explain", key="explanation_button"):
    with st.spinner("Generating Explanation..."):
        audio_file = generate_speech()
    st.audio(audio_file, format='audio/mp3', start_time=0)
    st.success("Explanation Generated")

# Get total lines from all_words_phrases.json and matched_neg_words.json
total_lines_all_words = read_json_and_sum("all_words_phrases")
total_lines_matched_neg = read_json_and_sum("matched_neg_words")

# Create DataFrame for the bubble chart
data = pd.DataFrame({
    'File': ['all_words_phrases.json', 'matched_neg_words.json'],
    'Total Lines': [total_lines_all_words, total_lines_matched_neg],
    'Color': ['green', 'red']  # Assigning colors for bubble chart
})

# Plotly bubble chart
fig = px.scatter(data, x='File', y='Total Lines', size='Total Lines', color='File',
                 hover_name='File', size_max=50,
                 color_discrete_map={"all_words_phrases.json": "green", "matched_neg_words.json": "red"})

fig.update_layout(title="Safety Risk Analysis")  # Leave font size adjustment out here

# Display the chart
st.plotly_chart(fig, use_container_width=True)  # Adjust for responsiveness

# Geolocation map
st.markdown("<h1 style='font-size: larger;'>Subscriber Location</h1>", unsafe_allow_html=True)

layer = pdk.Layer(
    'ScatterplotLayer',
    data=pd.DataFrame({'Latitude': [geo.lat], 'Longitude': [geo.lng]}),
    get_position='[Longitude, Latitude]',
    get_radius=20000,
    get_fill_color=[0, 255, 255],
    pickable=True,
    opacity=0.8,
)

map = pdk.Deck(
    layers=[layer],
    initial_view_state=pdk.ViewState(latitude=geo.lat, longitude=geo.lng, zoom=10),
)

st.pydeck_chart(map, use_container_width=True)  # Adjust for responsiveness
