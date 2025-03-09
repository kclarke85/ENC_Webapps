# import streamlit as st
# import base64
# import requests
# from io import BytesIO
# from PIL import Image
# import re
#
# # Page configuration
# st.set_page_config(
#     page_title="Coming Soon | Get Notified",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )
#
# # Custom CSS for modern look
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
#
#     html, body, [class*="css"] {
#         font-family: 'Poppins', sans-serif;
#     }
#
#     .main {
#         background-color: #f8f9fa;
#     }
#
#     .stButton button {
#         background-color: #0066ff;
#         color: white;
#         border-radius: 30px;
#         padding: 0.5rem 2rem;
#         font-weight: 500;
#         border: none;
#         transition: all 0.3s;
#     }
#
#     .stButton button:hover {
#         background-color: #0052cc;
#         transform: translateY(-2px);
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#     }
#
#     .title {
#         color: #333;
#         font-size: 3.5rem;
#         font-weight: 700;
#         margin-bottom: 1rem;
#     }
#
#     .subtitle {
#         color: #555;
#         font-size: 1.5rem;
#         font-weight: 400;
#         margin-bottom: 2rem;
#     }
#
#     .container {
#         background-color: white;
#         padding: 2rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
#         margin-bottom: 2rem;
#     }
#
#     .highlight {
#         color: #0066ff;
#         font-weight: 600;
#     }
#
#     .notification-form {
#         background-color: white;
#         padding: 1.5rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
#     }
#
#     .stTextInput input {
#         border-radius: 30px;
#         padding: 0.75rem 1rem;
#         border: 1px solid #e0e0e0;
#     }
#
#     .footer {
#         text-align: center;
#         color: #777;
#         font-size: 0.9rem;
#         margin-top: 2rem;
#     }
#
#     .image-container {
#         display: flex;
#         justify-content: center;
#         margin-bottom: 1.5rem;
#     }
#
#     .image-container img {
#         border-radius: 10px;
#         box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
#     }
# </style>
# """, unsafe_allow_html=True)
#
#
# # Function to load and resize images
# def load_image(url, width=None):
#     response = requests.get(url)
#     img = Image.open(BytesIO(response.content))
#     if width:
#         width_percent = width / float(img.size[0])
#         height = int(float(img.size[1]) * float(width_percent))
#         img = img.resize((width, height))
#     return img
#
#
# # Function to validate email
# def is_valid_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     return re.match(pattern, email) is not None
#
#
# # Function to handle signup
# def handle_signup(email):
#     # In a real app, you would save this to a database
#     # For now, just show a success message
#     if is_valid_email(email):
#         st.session_state.signed_up = True
#         st.session_state.email = email
#         return True
#     return False
#
#
# # Initialize session state
# if 'signed_up' not in st.session_state:
#     st.session_state.signed_up = False
#     st.session_state.email = ""
#
# # Main page content
# col1, col2, col3 = st.columns([1, 6, 1])
#
# with col2:
#     # Coming soon image
#     coming_soon_url = "https://t4.ftcdn.net/jpg/02/49/43/47/240_F_249434721_cfKowKR9QeMJ5c2fBmIjGuIQ4u5coCBH.jpg"
#     st.markdown(f"""
#     <div class="image-container">
#         <img src="{coming_soon_url}" alt="Coming Soon">
#     </div>
#     """, unsafe_allow_html=True)
#
#     # Title and subtitle
#     st.markdown('<h1 class="title">Something Essential Is On The Way!</h1>', unsafe_allow_html=True)
#     st.markdown('<p class="subtitle">We\'re working hard to bring you an amazing new experience. Stay tuned!</p>',
#                 unsafe_allow_html=True)
#
#     # Main content container
#     st.markdown('<div class="container">', unsafe_allow_html=True)
#
#     # Driving image
#     driving_url = "https://t4.ftcdn.net/jpg/05/55/63/71/240_F_555637140_NvHR8TYOJ531Z64WcSNU7LlqejpSX0Yo.jpg"
#     st.markdown(f"""
#     <div class="image-container">
#         <img src="{driving_url}" alt="Driving Experience">
#     </div>
#     """, unsafe_allow_html=True)
#
#     st.markdown("""
#     <h2>A New Way to give peace of mind</h2>
#     <p>We're revolutionizing how you connect with friends and family during negative encounters.</p>
#     <br>
#     <h3>Why You'll Love It:</h3>
#     <ul>
#         <li>When switched on. Negative words and phrases alert your loves ones. So they can take the appropriate next steps</li>
#         <li>Share with friends and family your situational awareness of your surroundings
# </li>
#     </ul>
#     """, unsafe_allow_html=True)
#
#     st.markdown('</div>', unsafe_allow_html=True)
#
#     # Email signup container
#     st.markdown('<div class="notification-form">', unsafe_allow_html=True)
#
#     if st.session_state.signed_up:
#         st.success(f"Thank you! We'll notify {st.session_state.email} as soon as we launch.")
#         if st.button("Notify Someone Else"):
#             st.session_state.signed_up = False
#     else:
#         st.markdown("""
#         <h2>Be The First To Know!</h2>
#         <p>Don't miss out on our launch. Enter your email below to get notified and share the excitement with your <span class="highlight">friends and family</span>!</p>
#         """, unsafe_allow_html=True)
#
#         with st.form("signup_form"):
#             email = st.text_input("Email Address", placeholder="your.email@example.com")
#
#             col1, col2, col3 = st.columns([1, 1, 1])
#             with col2:
#                 submit = st.form_submit_button("Notify Me")
#
#             if submit:
#                 if handle_signup(email):
#                     st.success(f"Thank you! We'll notify {email} as soon as we launch.")
#                 else:
#                     st.error("Please enter a valid email address.")
#
#         st.markdown("""
#         <p>Spread the word! Let your friends and family know quickly by sharing this page:</p>
#         """, unsafe_allow_html=True)
#
#         share_col1, share_col2, share_col3, share_col4 = st.columns([1, 1, 1, 1])
#         with share_col1:
#             st.button("Share on Facebook")
#         with share_col2:
#             st.button("Share on Twitter")
#         with share_col3:
#             st.button("Share on LinkedIn")
#         with share_col4:
#             st.button("Share via Email")
#
#     st.markdown('</div>', unsafe_allow_html=True)
#
#     # Countdown timer (Optional)
#     st.markdown('<div class="container">', unsafe_allow_html=True)
#     st.markdown("""
#     <h2>Launching Soon</h2>
#     <p>Our team is putting the finishing touches on this exciting new project. We can't wait to share it with you!</p>
#     <div style="text-align: center; margin: 2rem 0;">
#         <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">30</span>
#         <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">:</span>
#         <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">15</span>
#         <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">:</span>
#         <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">22</span>
#         <br>
#         <span style="color: #777; margin: 0 1rem;">Days</span>
#         <span style="color: #777; margin: 0 1rem;"></span>
#         <span style="color: #777; margin: 0 1rem;">Hours</span>
#         <span style="c
#         color: #777; margin: 0 1rem;"></span>
#         <span style="color: #777; margin: 0 1rem;">Minutes</span>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)
#
#     # Footer
#     st.markdown("""
#     <div class="footer">
#         <p>© 2025 Your Amazing Company. All rights reserved.</p>
#     </div>
# #     """, unsafe_allow_html=True)
# import streamlit as st
# import base64
# import requests
# from io import BytesIO
# from PIL import Image
# import re
# import urllib.parse
#
# # Page configuration
# st.set_page_config(
#     page_title="Coming Soon | Get Notified",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )
#
# # Custom CSS for modern look
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
#
#     html, body, [class*="css"] {
#         font-family: 'Poppins', sans-serif;
#     }
#
#     .main {
#         background-color: #f8f9fa;
#     }
#
#     .stButton button {
#         background-color: #0066ff;
#         color: white;
#         border-radius: 30px;
#         padding: 0.5rem 2rem;
#         font-weight: 500;
#         border: none;
#         transition: all 0.3s;
#     }
#
#     .stButton button:hover {
#         background-color: #0052cc;
#         transform: translateY(-2px);
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#     }
#
#     .title {
#         color: #333;
#         font-size: 3.5rem;
#         font-weight: 700;
#         margin-bottom: 1rem;
#     }
#
#     .subtitle {
#         color: #555;
#         font-size: 1.5rem;
#         font-weight: 400;
#         margin-bottom: 2rem;
#     }
#
#     .container {
#         background-color: white;
#         padding: 2rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
#         margin-bottom: 2rem;
#     }
#
#     .highlight {
#         color: #0066ff;
#         font-weight: 600;
#     }
#
#     .notification-form {
#         background-color: white;
#         padding: 1.5rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
#     }
#
#     .stTextInput input {
#         border-radius: 30px;
#         padding: 0.75rem 1rem;
#         border: 1px solid #e0e0e0;
#     }
#
#     .footer {
#         text-align: center;
#         color: #777;
#         font-size: 0.9rem;
#         margin-top: 2rem;
#     }
#
#     .image-container {
#         display: flex;
#         justify-content: center;
#         margin-bottom: 1.5rem;
#     }
#
#     .image-container img {
#         border-radius: 10px;
#         box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
#     }
#
#     .share-button {
#         display: inline-flex;
#         align-items: center;
#         justify-content: center;
#         gap: 8px;
#         margin: 5px;
#         padding: 10px 15px;
#         background-color: white;
#         color: #333;
#         border: 1px solid #ddd;
#         border-radius: 8px;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         text-decoration: none;
#     }
#
#     .share-button:hover {
#         background-color: #f5f5f5;
#         transform: translateY(-2px);
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#     }
#
#     .facebook { color: #3b5998; border-color: #3b5998; }
#     .facebook:hover { background-color: #3b599815; }
#
#     .twitter { color: #1da1f2; border-color: #1da1f2; }
#     .twitter:hover { background-color: #1da1f215; }
#
#     .linkedin { color: #0077b5; border-color: #0077b5; }
#     .linkedin:hover { background-color: #0077b515; }
#
#     .email { color: #ea4335; border-color: #ea4335; }
#     .email:hover { background-color: #ea433515; }
# </style>
# """, unsafe_allow_html=True)
#
#
# # Function to load and resize images
# def load_image(url, width=None):
#     response = requests.get(url)
#     img = Image.open(BytesIO(response.content))
#     if width:
#         width_percent = width / float(img.size[0])
#         height = int(float(img.size[1]) * float(width_percent))
#         img = img.resize((width, height))
#     return img
#
#
# # Function to validate email
# def is_valid_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     return re.match(pattern, email) is not None
#
#
# # Function to handle signup
# def handle_signup(email):
#     # In a real app, you would save this to a database
#     # For now, just show a success message
#     if is_valid_email(email):
#         st.session_state.signed_up = True
#         st.session_state.email = email
#         return True
#     return False
#
#
# # Initialize session state
# if 'signed_up' not in st.session_state:
#     st.session_state.signed_up = False
#     st.session_state.email = ""
#
# # Main page content
# col1, col2, col3 = st.columns([1, 6, 1])
#
# with col2:
#     # Coming soon image
#     coming_soon_url = "https://t4.ftcdn.net/jpg/02/49/43/47/240_F_249434721_cfKowKR9QeMJ5c2fBmIjGuIQ4u5coCBH.jpg"
#     st.markdown(f"""
#     <div class="image-container">
#         <img src="{coming_soon_url}" alt="Coming Soon">
#     </div>
#     """, unsafe_allow_html=True)
#
#     # Title and subtitle
#     st.markdown('<h1 class="title">Something Essential Is On The Way!</h1>', unsafe_allow_html=True)
#     st.markdown('<p class="subtitle">We\'re working hard to bring you an amazing new experience. Stay tuned!</p>',
#                 unsafe_allow_html=True)
#
#     # Main content container
#     st.markdown('<div class="container">', unsafe_allow_html=True)
#
#     # Driving image
#     driving_url = "https://t4.ftcdn.net/jpg/05/55/63/71/240_F_555637140_NvHR8TYOJ531Z64WcSNU7LlqejpSX0Yo.jpg"
#     st.markdown(f"""
#     <div class="image-container">
#         <img src="{driving_url}" alt="Driving Experience">
#     </div>
#     """, unsafe_allow_html=True)
#
#     st.markdown("""
#     <h2>A New Way to give peace of mind</h2>
#     <p>We're revolutionizing how you connect with friends and family during negative encounters.</p>
#     <br>
#     <h3>Why You'll Love It:</h3>
#     <ul>
#         <li>When switched on. Negative words and phrases alert your loves ones. So they can take the appropriate next steps</li>
#         <li>Share with friends and family your situational awareness of your surroundings
# </li>
#     </ul>
#     """, unsafe_allow_html=True)
#
#     st.markdown('</div>', unsafe_allow_html=True)
#
#     # Email signup container
#     st.markdown('<div class="notification-form">', unsafe_allow_html=True)
#
#     if st.session_state.signed_up:
#         st.success(f"Thank you! We'll notify {st.session_state.email} as soon as we launch.")
#         if st.button("Notify Someone Else"):
#             st.session_state.signed_up = False
#     else:
#         st.markdown("""
#         <h2>Be The First To Know!</h2>
#         <p>Don't miss out on our launch. Enter your email below to get notified and share the excitement with your <span class="highlight">friends and family</span>!</p>
#         """, unsafe_allow_html=True)
#
#         with st.form("signup_form"):
#             email = st.text_input("Email Address", placeholder="your.email@example.com")
#
#             col1, col2, col3 = st.columns([1, 1, 1])
#             with col2:
#                 submit = st.form_submit_button("Notify Me")
#
#             if submit:
#                 if handle_signup(email):
#                     st.success(f"Thank you! We'll notify {email} as soon as we launch.")
#                 else:
#                     st.error("Please enter a valid email address.")
#
#         st.markdown("""
#         <p>Spread the word! Let your friends and family know quickly by sharing this page:</p>
#         """, unsafe_allow_html=True)
#
#         # Share settings
#         page_url = "https://yoursafety.app"  # Replace with your actual URL when deployed
#         page_title = "Safety Alert App Coming Soon"
#         page_description = "A new way to stay connected and protected during negative encounters. Sign up to get notified!"
#
#         # URL encode parameters for sharing
#         encoded_url = urllib.parse.quote(page_url)
#         encoded_title = urllib.parse.quote(page_title)
#         encoded_description = urllib.parse.quote(page_description)
#
#         # Create sharing URLs
#         facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={encoded_url}"
#         twitter_url = f"https://twitter.com/intent/tweet?url={encoded_url}&text={encoded_title}"
#         linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}"
#         email_subject = urllib.parse.quote(page_title)
#         email_body = urllib.parse.quote(f"{page_description}\n\nCheck it out here: {page_url}")
#         email_url = f"mailto:?subject={email_subject}&body={email_body}"
#
#         # Social media sharing buttons
#         st.markdown(f"""
#         <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin: 20px 0;">
#             <a href="{facebook_url}" target="_blank" class="share-button facebook">
#                 <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
#                     <path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/>
#                 </svg>
#                 Facebook
#             </a>
#             <a href="{twitter_url}" target="_blank" class="share-button twitter">
#                 <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
#                     <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
#                 </svg>
#                 Twitter
#             </a>
#             <a href="{linkedin_url}" target="_blank" class="share-button linkedin">
#                 <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
#                     <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
#                 </svg>
#                 LinkedIn
#             </a>
#             <a href="{email_url}" class="share-button email">
#                 <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
#                     <path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414.05 3.555ZM0 4.697v7.104l5.803-3.558L0 4.697ZM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586l-1.239-.757Zm3.436-.586L16 11.801V4.697l-5.803 3.546Z"/>
#                 </svg>
#                 Email
#             </a>
#         </div>
#         """, unsafe_allow_html=True)
#
#     st.markdown('</div>', unsafe_allow_html=True)
#
#     # Countdown timer (Optional)
#     st.markdown('<div class="container">', unsafe_allow_html=True)
#     st.markdown("""
#     <h2>Launching Soon</h2>
#     <p>Our team is putting the finishing touches on this exciting new project. We can't wait to share it with you!</p>
#     <div style="text-align: center; margin: 2rem 0;">
#         <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">30</span>
#         <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">:</span>
#         <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">15</span>
#         <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">:</span>
#         <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">22</span>
#         <br>
#         <span style="color: #777; margin: 0 1rem;">Days</span>
#         <span style="color: #777; margin: 0 1rem;"></span>
#         <span style="color: #777; margin: 0 1rem;">Hours</span>
#         <span style="color: #777; margin: 0 1rem;"></span>
#         <span style="color: #777; margin: 0 1rem;">Minutes</span>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)
#
#     # Footer
#     st.markdown("""
#     <div class="footer">
#         <p>© 2025 Your Amazing Company. All rights reserved.</p>
#     </div>
#     """, unsafe_allow_html=True)
#
# # Add JavaScript to track sharing button clicks (optional)
# st.markdown("""
# <script>
# function trackShare(platform) {
#     // In a real app, you could send analytics data here
#     console.log("Shared on " + platform);
# }
# </script>
# """, unsafe_allow_html=True)
import streamlit as st
import base64
import requests
from io import BytesIO
from PIL import Image
import re
import urllib.parse
import pymongo
import os
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="Coming Soon | Get Notified",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# MongoDB Connection Settings
# Remove any backup connection strings that might be causing the issue
MONGO_CONNECTION_STRING = "mongodb+srv://doadmin:6W1X0945oscPd7j3@db-mongodb-nyc3-98048-77b8bd3a.mongo.ondigitalocean.com/admin?authSource=admin&replicaSet=db-mongodb-nyc3-98048&tls=true"
MONGO_DB_NAME = "Comming_Soon"
MONGO_COLLECTION_NAME = "email_subscribers"

# Enable MongoDB by default
MONGO_ENABLED = True


# Initialize MongoDB connection
@st.cache_resource
def init_db_connection():
    if not MONGO_ENABLED:
        logger.info("MongoDB connection disabled by configuration")
        return None

    try:
        # Add a timeout to avoid hanging if the connection is wrong
        client = pymongo.MongoClient(MONGO_CONNECTION_STRING, serverSelectionTimeoutMS=5000)
        # Check connection
        client.admin.command('ping')
        logger.info("Connected successfully to MongoDB")
        return client
    except Exception as e:
        logger.error(f"MongoDB Connection Error: {e}")
        # Log additional information for debugging
        logger.error(
            f"Connection string used: {MONGO_CONNECTION_STRING.replace(MONGO_CONNECTION_STRING.split('@')[0], 'mongodb+srv://[CREDENTIALS_HIDDEN]')}")
        # Don't show error to users, handle it gracefully
        return None


# Function to save email to MongoDB
def save_email_to_db(email):
    # If MongoDB is not enabled, just log the email and return success
    if not MONGO_ENABLED:
        logger.info(f"MongoDB disabled. Would have saved email: {email}")
        return True

    try:
        client = init_db_connection()
        if not client:
            logger.warning("MongoDB connection not available, saving email to session state only")
            # Still return True to not block the user experience
            return True

        db = client[MONGO_DB_NAME]
        collection = db[MONGO_COLLECTION_NAME]

        # Check if email already exists
        existing_email = collection.find_one({"email": email})
        if existing_email:
            logger.info(f"Email {email} already exists in database")
            return True

        # Create subscriber document
        subscriber = {
            "email": email,
            "signup_date": datetime.utcnow(),
            "source": "coming_soon_page",
            "confirmed": False,
            "ip_address": None  # In production, you might want to store IP for compliance
        }

        # Insert into database
        result = collection.insert_one(subscriber)
        logger.info(f"Added new subscriber: {email}, ID: {result.inserted_id}")
        return True

    except Exception as e:
        logger.error(f"Database Error: {e}")
        # Save email to a backup file as fallback
        try:
            with open("email_subscribers_backup.txt", "a") as f:
                f.write(f"{email},{datetime.utcnow()}\n")
            logger.info(f"Saved email to backup file: {email}")
        except Exception as backup_error:
            logger.error(f"Backup file error: {backup_error}")
        # Still return True to not block the user experience
        return True


# Custom CSS for modern look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .main {
        background-color: #f8f9fa;
    }

    .stButton button {
        background-color: #0066ff;
        color: white;
        border-radius: 30px;
        padding: 0.5rem 2rem;
        font-weight: 500;
        border: none;
        transition: all 0.3s;
    }

    .stButton button:hover {
        background-color: #0052cc;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .title {
        color: #333;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .subtitle {
        color: #555;
        font-size: 1.5rem;
        font-weight: 400;
        margin-bottom: 2rem;
    }

    .container {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 2rem;
    }

    .highlight {
        color: #0066ff;
        font-weight: 600;
    }

    .notification-form {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }

    .stTextInput input {
        border-radius: 30px;
        padding: 0.75rem 1rem;
        border: 1px solid #e0e0e0;
    }

    .footer {
        text-align: center;
        color: #777;
        font-size: 0.9rem;
        margin-top: 2rem;
    }

    .image-container {
        display: flex;
        justify-content: center;
        margin-bottom: 1.5rem;
    }

    .image-container img {
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    .share-button {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        margin: 5px;
        padding: 10px 15px;
        background-color: white;
        color: #333;
        border: 1px solid #ddd;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
    }

    .share-button:hover {
        background-color: #f5f5f5;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .facebook { color: #3b5998; border-color: #3b5998; }
    .facebook:hover { background-color: #3b599815; }

    .twitter { color: #1da1f2; border-color: #1da1f2; }
    .twitter:hover { background-color: #1da1f215; }

    .linkedin { color: #0077b5; border-color: #0077b5; }
    .linkedin:hover { background-color: #0077b515; }

    .email { color: #ea4335; border-color: #ea4335; }
    .email:hover { background-color: #ea433515; }

    .success-icon {
        color: #28a745;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .error-icon {
        color: #dc3545;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .notification {
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .notification.success {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }

    .notification.error {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
</style>
""", unsafe_allow_html=True)


# Function to load and resize images
def load_image(url, width=None):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    if width:
        width_percent = width / float(img.size[0])
        height = int(float(img.size[1]) * float(width_percent))
        img = img.resize((width, height))
    return img


# Function to validate email
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


# Function to handle signup
def handle_signup(email):
    if not is_valid_email(email):
        return False, "Please enter a valid email address."

    # Save to MongoDB
    success = save_email_to_db(email)
    if success:
        st.session_state.signed_up = True
        st.session_state.email = email
        return True, "Thank you! We'll notify you as soon as we launch."
    else:
        return False, "Unable to register your email. Please try again later."


# Initialize session state
if 'signed_up' not in st.session_state:
    st.session_state.signed_up = False
    st.session_state.email = ""
if 'form_message' not in st.session_state:
    st.session_state.form_message = ""
if 'form_status' not in st.session_state:
    st.session_state.form_status = ""

# Main page content
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    # Coming soon image
    coming_soon_url = "https://t4.ftcdn.net/jpg/02/49/43/47/240_F_249434721_cfKowKR9QeMJ5c2fBmIjGuIQ4u5coCBH.jpg"
    st.markdown(f"""
    <div class="image-container">
        <img src="{coming_soon_url}" alt="Coming Soon">
    </div>
    """, unsafe_allow_html=True)

    # Title and subtitle
    st.markdown('<h1 class="title">Something Essential Is On The Way!</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">We\'re working hard to bring you an amazing new experience. Stay tuned!</p>',
                unsafe_allow_html=True)

    # Main content container
    st.markdown('<div class="container">', unsafe_allow_html=True)

    # Driving image
    driving_url = "https://t4.ftcdn.net/jpg/05/55/63/71/240_F_555637140_NvHR8TYOJ531Z64WcSNU7LlqejpSX0Yo.jpg"
    st.markdown(f"""
    <div class="image-container">
        <img src="{driving_url}" alt="Driving Experience">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2>A New Way to give peace of mind</h2>
    <p>We're revolutionizing how you connect with friends and family during negative encounters.</p>
    <br>
    <h3>Why You'll Love It:</h3>
    <ul>
        <li>When switched on. Negative words and phrases alert your loves ones. So they can take the appropriate next steps</li>
        <li>Share with friends and family your situational awareness of your surroundings 
</li>     
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Email signup container
    st.markdown('<div class="notification-form">', unsafe_allow_html=True)

    if st.session_state.signed_up:
        st.markdown(f"""
        <div class="notification success">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16">
                <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
            </svg>
            <span>Thank you! We'll notify <strong>{st.session_state.email}</strong> as soon as we launch.</span>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Notify Someone Else"):
            st.session_state.signed_up = False
    else:
        st.markdown("""
        <h2>Be The First To Know!</h2>
        <p>Don't miss out on our launch. Enter your email below to get notified and share the excitement with your <span class="highlight">friends and family</span>!</p>
        """, unsafe_allow_html=True)

        # Display error message if exists
        if st.session_state.form_status == "error" and st.session_state.form_message:
            st.markdown(f"""
            <div class="notification error">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                    <path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/>
                </svg>
                <span>{st.session_state.form_message}</span>
            </div>
            """, unsafe_allow_html=True)

        with st.form("signup_form"):
            email = st.text_input("Email Address", placeholder="your.email@example.com")

            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                submit = st.form_submit_button("Notify Me")

            if submit:
                success, message = handle_signup(email)
                if success:
                    st.session_state.form_status = "success"
                else:
                    st.session_state.form_status = "error"
                    st.session_state.form_message = message
                    st.experimental_rerun()

        st.markdown("""
        <p>Spread the word! Let your friends and family know quickly by sharing this page:</p>
        """, unsafe_allow_html=True)

        # Share settings
        page_url = "https://yoursafety.app"  # Replace with your actual URL when deployed
        page_title = "Safety Alert App Coming Soon"
        page_description = "A new way to stay connected and protected during negative encounters. Sign up to get notified!"

        # URL encode parameters for sharing
        encoded_url = urllib.parse.quote(page_url)
        encoded_title = urllib.parse.quote(page_title)
        encoded_description = urllib.parse.quote(page_description)

        # Create sharing URLs
        facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={encoded_url}"
        twitter_url = f"https://twitter.com/intent/tweet?url={encoded_url}&text={encoded_title}"
        linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}"
        email_subject = urllib.parse.quote(page_title)
        email_body = urllib.parse.quote(f"{page_description}\n\nCheck it out here: {page_url}")
        email_url = f"mailto:?subject={email_subject}&body={email_body}"

        # Social media sharing buttons
        st.markdown(f"""
        <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin: 20px 0;">
            <a href="{facebook_url}" target="_blank" class="share-button facebook">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/>
                </svg>
                Facebook
            </a>
            <a href="{twitter_url}" target="_blank" class="share-button twitter">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
                </svg>
                Twitter
            </a>
            <a href="{linkedin_url}" target="_blank" class="share-button linkedin">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg>
                LinkedIn
            </a>
            <a href="{email_url}" class="share-button email">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414.05 3.555ZM0 4.697v7.104l5.803-3.558L0 4.697ZM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586l-1.239-.757Zm3.436-.586L16 11.801V4.697l-5.803 3.546Z"/>
                </svg>
                Email
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Countdown timer (Optional)
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown("""
    <h2>Launching Soon</h2>
    <p>Our team is putting the finishing touches on this exciting new project. We can't wait to share it with you!</p>
    <div style="text-align: center; margin: 2rem 0;">
        <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">30</span>
        <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">:</span>
        <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">15</span>
        <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">:</span>
        <span style="font-size: 2rem; font-weight: 700; margin: 0 1rem;">22</span>
        <br>
        <span style="color: #777; margin: 0 1rem;">Days</span>
        <span style="color: #777; margin: 0 1rem;"></span>
        <span style="color: #777; margin: 0 1rem;">Hours</span>
        <span style="color: #777; margin: 0 1rem;"></span>
        <span style="color: #777; margin: 0 1rem;">Minutes</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2025 Your Amazing Company. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

# Add Analytics tracking (optional)
st.markdown("""
<script>
function trackShare(platform) {
    // In a real app, you could send analytics data here
    console.log("Shared on " + platform);
}

function trackSignup(email) {
    // Track signup events
    console.log("New signup: " + email);
}
</script>
""", unsafe_allow_html=True)