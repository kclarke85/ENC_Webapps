# # # # # import pandas as pd
# # # # # import plotly.express as px
# # # # # import pydeck as pdk
# # # # # import geocoder
# # # # # import streamlit as st
# # # # #
# # # # # # Define the paths to your text files
# # # # # file_path1 = "Negative.txt"
# # # # # file_path2 = "positive.csv"  # Change this to the path of your positive text file
# # # # #
# # # # # # Read the content of the text files and split into lines
# # # # # with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
# # # # #     content1 = file1.readlines()
# # # # #     content2 = file2.readlines()
# # # # #
# # # # # # Calculate the line counts
# # # # # line_count1 = len(content1)
# # # # # line_count2 = len(content2)
# # # # #
# # # # # # Create a bubble chart using Plotly with red for negative and green for positive
# # # # # data = pd.DataFrame({
# # # # #     'File': ['Negative', 'Positive'],
# # # # #     'Line Count': [line_count1, line_count2]
# # # # # })
# # # # #
# # # # # fig = px.bar(data, x='File', y='Line Count', title='Line Count Comparison', color='File')
# # # # #
# # # # # # Get real-time geo-location of the computer
# # # # # geo = geocoder.ip('me')
# # # # #
# # # # # # Create a GeoMap using Pydeck
# # # # # geo_data = pd.DataFrame({
# # # # #     'Latitude': [geo.lat],
# # # # #     'Longitude': [geo.lng],
# # # # # })
# # # # #
# # # # # # Create two columns with equal size
# # # # # col1, col2 = st.columns(2)
# # # # #
# # # # # # Set the width of the columns to be the same
# # # # # col1.width = col2.width
# # # # #
# # # # # # Display the bubble chart in the first column
# # # # # with col1:
# # # # #     st.plotly_chart(fig, use_container_width=True)
# # # # #
# # # # # # Display the GeoMap in the second column
# # # # # with col2:
# # # # #     st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
# # # # #     st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
# # # # #     st.pydeck_chart(pdk.Deck(
# # # # #         map_style="mapbox://styles/mapbox/light-v9",
# # # # #         initial_view_state=pdk.ViewState(
# # # # #             latitude=geo.lat,
# # # # #             longitude=geo.lng,
# # # # #             zoom=11,
# # # # #             pitch=50,
# # # # #         ),
# # # # #         layers=[
# # # # #             pdk.Layer(
# # # # #                 "ScatterplotLayer",
# # # # #                 data=geo_data,
# # # # #                 get_position=["Longitude", "Latitude"],
# # # # #                 get_radius=200,
# # # # #                 get_fill_color=[255, 0, 0],  # Red color
# # # # #             ),
# # # # #         ],
# # # # #     ))
# # # # #
# # # # # # Create two columns for positive and negative phrases
# # # # # col3, col4 = st.columns(2)
# # # # #
# # # # # # Display positive phrases in the left column
# # # # # with col3:
# # # # #     st.subheader("Positive Phrases")
# # # # #     for line in content2:
# # # # #         st.write(line)
# # # # #
# # # # # # Display negative phrases in the right column
# # # # # with col4:
# # # # #     st.subheader("Negative Phrases")
# # # # #     for line in content1:
# # # # #         st.write(line)
# # # # # import pandas as pd
# # # # # import plotly.express as px
# # # # # import pydeck as pdk
# # # # # import geocoder
# # # # # import streamlit as st
# # # # #
# # # # # # Define the paths to your text files
# # # # # file_path1 = "Negative.txt"
# # # # # file_path2 = "positive.csv"  # Change this to the path of your positive text file
# # # # #
# # # # # # Read the content of the text files and split into lines
# # # # # with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
# # # # #     content1 = file1.readlines()
# # # # #     content2 = file2.readlines()
# # # # #
# # # # # # Calculate the line counts
# # # # # line_count1 = len(content1)
# # # # # line_count2 = len(content2)
# # # # #
# # # # # # Create a bubble chart using Plotly with red for negative and green for positive
# # # # # data = pd.DataFrame({
# # # # #     'File': ['Negative', 'Positive'],
# # # # #     'Line Count': [line_count1, line_count2]
# # # # # })
# # # # #
# # # # # fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Line Count Comparison', color='File')
# # # # #
# # # # # # Get real-time geo-location of the computer
# # # # # geo = geocoder.ip('me')
# # # # #
# # # # # # Create a GeoMap using Pydeck
# # # # # geo_data = pd.DataFrame({
# # # # #     'Latitude': [geo.lat],
# # # # #     'Longitude': [geo.lng],
# # # # # })
# # # # #
# # # # # # Create two columns with equal size
# # # # # col1, col2 = st.columns(2)
# # # # #
# # # # # # Set the width of the columns to be the same
# # # # # col1.width = col2.width
# # # # #
# # # # # # Display the bubble chart in the first column
# # # # # with col1:
# # # # #     st.plotly_chart(fig, use_container_width=True)
# # # # #
# # # # # # Display the GeoMap in the second column
# # # # # with col2:
# # # # #     st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
# # # # #     st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
# # # # #     st.pydeck_chart(pdk.Deck(
# # # # #         map_style="mapbox://styles/mapbox/light-v9",
# # # # #         initial_view_state=pdk.ViewState(
# # # # #             latitude=geo.lat,
# # # # #             longitude=geo.lng,
# # # # #             zoom=11,
# # # # #             pitch=50,
# # # # #         ),
# # # # #         layers=[
# # # # #             pdk.Layer(
# # # # #                 "ScatterplotLayer",
# # # # #                 data=geo_data,
# # # # #                 get_position=["Longitude", "Latitude"],
# # # # #                 get_radius=200,
# # # # #                 get_fill_color=[255, 0, 0],  # Red color
# # # # #             ),
# # # # #         ],
# # # # #     ))
# # # # #
# # # # # # Create two columns for positive and negative phrases
# # # # # col3, col4 = st.columns(2)
# # # # #
# # # # # # Display positive phrases in the left column
# # # # # with col3:
# # # # #     st.subheader("Positive Phrases")
# # # # #     st.write(content2)
# # # # #
# # # # # # Display negative phrases in the right column
# # # # # with col4:
# # # # #     st.subheader("Negative Phrases")
# # # # #     st.write(content1)
# # # # # 10/11/2023 Gold
# # # # import pandas as pd
# # # # import plotly.express as px
# # # # import pydeck as pdk
# # # # import geocoder
# # # # import streamlit as st
# # # #
# # # # # Define the paths to your text files
# # # # file_path1 = "Negative.txt"
# # # # file_path2 = "positive.csv"  # Change this to the path of your positive text file
# # # #
# # # # # Read the content of the text files and split into lines
# # # # with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
# # # #     content1 = file1.readlines()
# # # #     content2 = file2.readlines()
# # # #
# # # # # Calculate the line counts
# # # # line_count1 = len(content1)
# # # # line_count2 = len(content2)
# # # #
# # # # # Create a bubble chart using Plotly with red for negative and green for positive
# # # # data = pd.DataFrame({
# # # #     'File': ['Negative', 'Positive'],
# # # #     'Line Count': [line_count1, line_count2]
# # # # })
# # # #
# # # # fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Line Count Comparison', color='File')
# # # #
# # # # # Get real-time geo-location of the computer
# # # # geo = geocoder.ip('me')
# # # #
# # # # # Create a GeoMap using Pydeck
# # # # geo_data = pd.DataFrame({
# # # #     'Latitude': [geo.lat],
# # # #     'Longitude': [geo.lng],
# # # # })
# # # #
# # # # # Create a layout with four columns: one for the video, one for the chart, and two for the table.
# # # # col1, col2, col3, col4 = st.columns([2, 2, 4, 4])
# # # #
# # # # # Display the video player in the first column
# # # # with col1:
# # # #     video_file = open('C:/Users/kclar/PycharmProjects/VOZ_trigger/static/video.mp4', 'rb')
# # # #     video_bytes = video_file.read()
# # # #     st.video(video_bytes)
# # # #
# # # # # Create two columns with equal size
# # # # col1, col2 = st.columns(2)
# # # #
# # # # # Set the width of the columns to be the same
# # # # col1.width = col2.width
# # # #
# # # # # Display the bubble chart in the first column
# # # # with col1:
# # # #     st.plotly_chart(fig, use_container_width=True)
# # # #
# # # # # Display the GeoMap in the second column
# # # # with col2:
# # # #     st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
# # # #     st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
# # # #     st.pydeck_chart(pdk.Deck(
# # # #         map_style="mapbox://styles/mapbox/light-v9",
# # # #         initial_view_state=pdk.ViewState(
# # # #             latitude=geo.lat,
# # # #             longitude=geo.lng,
# # # #             zoom=11,
# # # #             pitch=50,
# # # #         ),
# # # #         layers=[
# # # #             pdk.Layer(
# # # #                 "ScatterplotLayer",
# # # #                 data=geo_data,
# # # #                 get_position=["Longitude", "Latitude"],
# # # #                 get_radius=200,
# # # #                 get_fill_color=[255, 0, 0],  # Red color
# # # #             ),
# # # #         ],
# # # #     ))
# # # #
# # # # # Create two columns for positive and negative phrases
# # # # col3, col4 = st.columns(2)
# # # #
# # # # # Display positive phrases in the left column
# # # # with col3:
# # # #     st.subheader("Positive Phrases")
# # # #     positive_phrases = [line.strip() for line in content2]
# # # #     st.dataframe(pd.DataFrame(positive_phrases, columns=["Positive Phrases"]), height=500)
# # # #
# # # # # Display negative phrases in the right column
# # # # with col4:
# # # #     st.subheader("Negative Phrases")
# # # #     negative_phrases = [line.strip() for line in content1]
# # # #     st.dataframe(pd.DataFrame(negative_phrases, columns=["Negative Phrases"]), height=500)
# # # #
# # # # #10/12 withh video close to what I want
# # # #
# # # import pandas as pd
# # # import plotly.express as px
# # # import pydeck as pdk
# # # import geocoder
# # # import streamlit as st
# # #
# # # # Define the paths to your text files
# # # file_path1 = "Negative.txt"
# # # file_path2 = "positive.csv"  # Change this to the path of your positive text file
# # #
# # # # Read the content of the text files and split into lines
# # # with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
# # #     content1 = file1.readlines()
# # #     content2 = file2.readlines()
# # #
# # # # Calculate the line counts
# # # line_count1 = len(content1)
# # # line_count2 = len(content2)
# # #
# # # # Create a bubble chart using Plotly with red for negative and green for positive
# # # data = pd.DataFrame({
# # #     'File': ['Negative', 'Positive'],
# # #     'Line Count': [line_count1, line_count2]
# # # })
# # #
# # # fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Line Count Comparison', color='File')
# # #
# # # # Get real-time geo-location of the computer
# # # geo = geocoder.ip('me')
# # #
# # # # Create a GeoMap using Pydeck
# # # geo_data = pd.DataFrame({
# # #     'Latitude': [geo.lat],
# # #     'Longitude': [geo.lng],
# # # })
# # #
# # # # Create a layout with two columns for the video and charts
# # # col1, col2 = st.columns(2)
# # #
# # # # Display the video player in the first column
# # # with col1:
# # #     st.write('Video Player')
# # #     video_file = open('C:/Users/kclar/PycharmProjects/VOZ_trigger/static/video.mp4', 'rb')
# # #     video_bytes = video_file.read()
# # #     st.video(video_bytes)
# # #
# # # # Display the bubble chart in the second column
# # # with col2:
# # #     st.plotly_chart(fig, use_container_width=True)
# # #
# # # # Display the GeoMap
# # # st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
# # # st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
# # # st.pydeck_chart(pdk.Deck(
# # #     map_style="mapbox://styles/mapbox/light-v9",
# # #     initial_view_state=pdk.ViewState(
# # #         latitude=geo.lat,
# # #         longitude=geo.lng,
# # #         zoom=11,
# # #         pitch=50,
# # #     ),
# # #     layers=[
# # #         pdk.Layer(
# # #             "ScatterplotLayer",
# # #             data=geo_data,
# # #             get_position=["Longitude", "Latitude"],
# # #             get_radius=200,
# # #             get_fill_color=[255, 0, 0],  # Red color
# # #         ),
# # #     ],
# # # ))
# # #
# # # # Display positive and negative phrases
# # # st.write('Positive Phrases')
# # # positive_phrases = [line.strip() for line in content2]
# # # st.dataframe(pd.DataFrame(positive_phrases, columns=["Positive Phrases"]), height=500)
# # #
# # # st.write('Negative Phrases')
# # # negative_phrases = [line.strip() for line in content1]
# # # st.dataframe(pd.DataFrame(negative_phrases, columns=["Negative Phrases"]), height=500)
# # # import pandas as pd
# # # import plotly.express as px
# # # import pydeck as pdk
# # # import geocoder
# # # import streamlit as st
# # #
# # # # Define the paths to your text files
# # # file_path1 = "Negative.txt"
# # # file_path2 = "positive.csv"  # Change this to the path of your positive text file
# # #
# # # # Read the content of the text files and split into lines
# # # with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
# # #     content1 = file1.readlines()
# # #     content2 = file2.readlines()
# # #
# # # # Calculate the line counts
# # # line_count1 = len(content1)
# # # line_count2 = len(content2)
# # #
# # # # Create a bubble chart using Plotly with red for negative and green for positive
# # # data = pd.DataFrame({
# # #     'File': ['Negative', 'Positive'],
# # #     'Line Count': [line_count1, line_count2]
# # # })
# # #
# # # fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Line Count Comparison', color='File')
# # #
# # # # Get real-time geo-location of the computer
# # # geo = geocoder.ip('me')
# # #
# # # # Create a GeoMap using Pydeck
# # # geo_data = pd.DataFrame({
# # #     'Latitude': [geo.lat],
# # #     'Longitude': [geo.lng],
# # # })
# # #
# # # # Create a layout with three columns: one for the video, one for the chart, and one for the GeoMap and phrases
# # # col1, col2, col3 = st.columns([2, 2, 4])
# # #
# # # # Display the video player in the first column
# # # with col1:
# # #     st.write('Video Player')
# # #     video_file = open('C:/Users/kclar/PycharmProjects/VOZ_trigger/static/video.mp4', 'rb')
# # #     video_bytes = video_file.read()
# # #     st.video(video_bytes)
# # #
# # # # Display the bubble chart in the second column
# # # with col2:
# # #     st.plotly_chart(fig, use_container_width=True)
# # #
# # # # Display the GeoMap and phrases in the third column
# # # with col3:
# # #     st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
# # #     st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
# # #     st.pydeck_chart(pdk.Deck(
# # #         map_style="mapbox://styles/mapbox/light-v9",
# # #         initial_view_state=pdk.ViewState(
# # #             latitude=geo.lat,
# # #             longitude=geo.lng,
# # #             zoom=11,
# # #             pitch=50,
# # #         ),
# # #         layers=[
# # #             pdk.Layer(
# # #                 "ScatterplotLayer",
# # #                 data=geo_data,
# # #                 get_position=["Longitude", "Latitude"],
# # #                 get_radius=200,
# # #                 get_fill_color=[255, 0, 0],  # Red color
# # #             ),
# # #         ],
# # #     ))
# # #
# # # # Display positive and negative phrases
# # # st.write('Positive Phrases')
# # # positive_phrases = [line.strip() for line in content2]
# # # st.dataframe(pd.DataFrame(positive_phrases, columns=["Positive Phrases"]), height=500)
# # #
# # # st.write('Negative Phrases')
# # # negative_phrases = [line.strip() for line in content1]
# # # st.dataframe(pd.DataFrame(negative_phrases, columns=["Negative Phrases"]), height=500)
# #
# #
# # # import pandas as pd
# # # import plotly.express as px
# # # import pydeck as pdk
# # # import geocoder
# # # import streamlit as st
# # #
# # # # Define the paths to your text files
# # # file_path1 = "Negative.txt"
# # # file_path2 = "positive.csv"  # Change this to the path of your positive text file
# # #
# # # # Read the content of the text files and split into lines
# # # with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
# # #     content1 = file1.readlines()
# # #     content2 = file2.readlines()
# # #
# # # # Calculate the line counts
# # # line_count1 = len(content1)
# # # line_count2 = len(content2)
# # #
# # # # Create a bubble chart using Plotly with red for negative and green for positive
# # # data = pd.DataFrame({
# # #     'File': ['Negative', 'Positive'],
# # #     'Line Count': [line_count1, line_count2]
# # # })
# # #
# # # fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Line Count Comparison', color='File')
# # #
# # # # Get real-time geo-location of the computer
# # # geo = geocoder.ip('me')
# # #
# # # # Create a GeoMap using Pydeck
# # # geo_data = pd.DataFrame({
# # #     'Latitude': [geo.lat],
# # #     'Longitude': [geo.lng],
# # # })
# # #
# # # # Set the page layout to have a centered title and move the MP4 player to the top center of the page
# # # st.set_page_config(layout="wide")
# # #
# # # # Center the title
# # # st.title("Your Data Visualization")
# # #
# # # # Create a layout with three columns: one for the video, one for the chart, and one for the GeoMap and phrases
# # # col1, col2, col3 = st.columns([1, 1, 1])
# # #
# # # # Display the video player at the top center
# # # with col2:
# # #     st.write('Video Player')
# # #     video_file = open('C:/Users/kclar/PycharmProjects/VOZ_trigger/static/video.mp4', 'rb')
# # #     video_bytes = video_file.read()
# # #     st.video(video_bytes)
# # #
# # # # Display the bubble chart in the second column
# # # with col1:
# # #     st.plotly_chart(fig, use_container_width=True)
# # #
# # # # Display the GeoMap and phrases in the third column
# # # with col3:
# # #     st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
# # #     st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
# # #     st.pydeck_chart(pdk.Deck(
# # #         map_style="mapbox://styles/mapbox/light-v9",
# # #         initial_view_state=pdk.ViewState(
# # #             latitude=geo.lat,
# # #             longitude=geo.lng,
# # #             zoom=11,
# # #             pitch=50,
# # #         ),
# # #         layers=[
# # #             pdk.Layer(
# # #                 "ScatterplotLayer",
# # #                 data=geo_data,
# # #                 get_position=["Longitude", "Latitude"],
# # #                 get_radius=200,
# # #                 get_fill_color=[255, 0, 0],  # Red color
# # #             ),
# # #         ],
# # #     ))
# # #
# # # # Display positive and negative phrases
# # # st.write('Positive Phrases')
# # # positive_phrases = [line.strip() for line in content2]
# # # st.dataframe(pd.DataFrame(positive_phrases, columns=["Positive Phrases"]), height=500)
# # #
# # # st.write('Negative Phrases')
# # # negative_phrases = [line.strip() for line in content1]
# # # st.dataframe(pd.DataFrame(negative_phrases, columns=["Negative Phrases"]), height=500)
# #
# # # import pandas as pd
# # # import plotly.express as px
# # # import pydeck as pdk
# # # import geocoder
# # # import streamlit as st
# # #
# # # # Define the paths to your text files
# # # file_path1 = "Negative.txt"
# # # file_path2 = "positive.csv"  # Change this to the path of your positive text file
# # #
# # # # Read the content of the text files and split into lines
# # # with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
# # #     content1 = file1.readlines()
# # #     content2 = file2.readlines()
# # #
# # # # Calculate the line counts
# # # line_count1 = len(content1)
# # # line_count2 = len(content2)
# # #
# # # # Create a bubble chart using Plotly with red for negative and green for positive
# # # data = pd.DataFrame({
# # #     'File': ['Negative', 'Positive'],
# # #     'Line Count': [line_count1, line_count2]
# # # })
# # #
# # # fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Line Count Comparison', color='File')
# # #
# # # # Get real-time geo-location of the computer
# # # geo = geocoder.ip('me')
# # #
# # # # Create a GeoMap using Pydeck
# # # geo_data = pd.DataFrame({
# # #     'Latitude': [geo.lat],
# # #     'Longitude': [geo.lng],
# # # })
# # #
# # # # Set the page layout to have a centered title
# # # st.set_page_config(layout="wide")
# # #
# # # # Center the title
# # # st.title("Your Data Visualization")
# # #
# # # # Create a layout with three columns: one for the video, one for the chart, and one for the phrases
# # # col1, col2, col3 = st.columns([1, 1, 1])
# # #
# # # # Display the video player in the first column and adjust its size to match the geolocation chart
# # # with col2:
# # #     st.write('Video Player')
# # #     video_file = open('C:/Users/kclar/PycharmProjects/VOZ_trigger/static/video.mp4', 'rb')
# # #     video_bytes = video_file.read()
# # #     st.video(video_bytes, width=geo_data.shape[1], height=geo_data.shape[0])
# # #
# # # # Display the bubble chart in the second column
# # # with col1:
# # #     st.plotly_chart(fig, use_container_width=True)
# # #
# # # # Display the GeoMap in the third column
# # # with col3:
# # #     st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
# # #     st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
# # #     st.pydeck_chart(pdk.Deck(
# # #         map_style="mapbox://styles/mapbox/light-v9",
# # #         initial_view_state=pdk.ViewState(
# # #             latitude=geo.lat,
# # #             longitude=geo.lng,
# # #             zoom=11,
# # #             pitch=50,
# # #         ),
# # #         layers=[
# # #             pdk.Layer(
# # #                 "ScatterplotLayer",
# # #                 data=geo_data,
# # #                 get_position=["Longitude", "Latitude"],
# # #                 get_radius=200,
# # #                 get_fill_color=[255, 0, 0],  # Red color
# # #             ),
# # #         ],
# # #     ))
# # #
# # # # Display positive and negative phrases
# # # st.write('Positive Phrases')
# # # positive_phrases = [line.strip() for line in content2]
# # # st.dataframe(pd.DataFrame(positive_phrases, columns=["Positive Phrases"]), height=500)
# # #
# # # st.write('Negative Phrases')
# # # negative_phrases = [line.strip() for line in content1]
# # # st.dataframe(pd.DataFrame(negative_phrases, columns=["Negative Phrases"]), height=500)
# # #
# # # import pandas as pd
# # # import plotly.express as px
# # # import pydeck as pdk
# # # import geocoder
# # # import streamlit as st
# # #
# # # # Define the paths to your text files
# # # file_path1 = "Negative.txt"
# # # file_path2 = "positive.csv"  # Change this to the path of your positive text file
# # #
# # # # Read the content of the text files and split into lines
# # # with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
# # #     content1 = file1.readlines()
# # #     content2 = file2.readlines()
# # #
# # # # Calculate the line counts
# # # line_count1 = len(content1)
# # # line_count2 = len(content2)
# # #
# # # # Create a bubble chart using Plotly with red for negative and green for positive
# # # data = pd.DataFrame({
# # #     'File': ['Negative', 'Positive'],
# # #     'Line Count': [line_count1, line_count2]
# # # })
# # #
# # # fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Line Count Comparison', color='File')
# # #
# # # # Get real-time geo-location of the computer
# # # geo = geocoder.ip('me')
# # #
# # # # Create a GeoMap using Pydeck
# # # geo_data = pd.DataFrame({
# # #     'Latitude': [geo.lat],
# # #     'Longitude': [geo.lng],
# # # })
# # #
# # # # Set the page layout to have a centered title
# # # st.set_page_config(layout="wide")
# # #
# # # # Center the title
# # # st.title("Your Data Visualization")
# # #
# # # # Create a layout with three columns: one for the video, one for the chart, and one for the phrases
# # # col1, col2, col3 = st.columns([1, 1, 1])
# # #
# # # # Display the video player in the first column and adjust its size to match the geolocation chart
# # # with col2:
# # #     st.write('Video Player')
# # #     video_file = open('C:/Users/kclar/PycharmProjects/VOZ_trigger/static/video.mp4', 'rb')
# # #     video_bytes = video_file.read()
# # #     st.video(video_bytes, width=geo_data.shape[1], height=geo_data.shape[0])
# # #
# # # # Display the bubble chart in the second column
# # # with col1:
# # #     st.plotly_chart(fig, use_container_width=True)
# # #
# # # # Display the GeoMap in the third column
# # # with col3:
# # #     st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
# # #     st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
# # #     st.pydeck_chart(pdk.Deck(
# # #         map_style="mapbox://styles/mapbox/light-v9",
# # #         initial_view_state=pdk.ViewState(
# # #             latitude=geo.lat,
# # #             longitude=geo.lng,
# # #             zoom=11,
# # #             pitch=50,
# # #         ),
# # #         layers=[
# # #             pdk.Layer(
# # #                 "ScatterplotLayer",
# # #                 data=geo_data,
# # #                 get_position=["Longitude", "Latitude"],
# # #                 get_radius=200,
# # #                 get_fill_color=[255, 0, 0],  # Red color
# # #             ),
# # #         ],
# # #     ))
# # #
# # # # Create a new layout for the tables below the existing content
# # # col4, col5 = st.columns(2)
# # #
# # # # Display positive and negative phrases side by side in the lower center of the page
# # # with col4:
# # #     st.write('Positive Phrases')
# # #     positive_phrases = [line.strip() for line in content2]
# # #     st.dataframe(pd.DataFrame(positive_phrases, columns=["Positive Phrases"]), height=500)
# # #
# # # with col5:
# # #     st.write('Negative Phrases')
# # #     negative_phrases = [line.strip for line in content1]
# # #     st.dataframe(pd.DataFrame(negative_phrases, columns=["Negative Phrases"]), height=500)
# # #
# # # import pandas as pd
# # # import plotly.express as px
# # # import pydeck as pdk
# # # import geocoder
# # # import streamlit as st
# # #
# # # # Define the paths to your text files
# # # file_path1 = "Negative.txt"
# # # file_path2 = "positive.csv"  # Change this to the path of your positive text file
# # #
# # # # Read the content of the text files and split into lines
# # # with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
# # #     content1 = file1.readlines()
# # #     content2 = file2.readlines()
# # #
# # # # Calculate the line counts
# # # line_count1 = len(content1)
# # # line_count2 = len(content2)
# # #
# # # # Create a bubble chart using Plotly with red for negative and green for positive
# # # data = pd.DataFrame({
# # #     'File': ['Negative', 'Positive'],
# # #     'Line Count': [line_count1, line_count2]
# # # })
# # #
# # # fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Line Count Comparison', color='File')
# # #
# # # # Get real-time geo-location of the computer
# # # geo = geocoder.ip('me')
# # #
# # # # Create a GeoMap using Pydeck
# # # geo_data = pd.DataFrame({
# # #     'Latitude': [geo.lat],
# # #     'Longitude': [geo.lng],
# # # })
# # #
# # # # Set the page layout to have a centered title
# # # st.set_page_config(layout="wide")
# # #
# # # # Center the title
# # # st.title("Your Data Visualization")
# # #
# # # # Create a layout with three columns: one for the video, one for the chart, and one for the phrases
# # # col1, col2, col3 = st.columns([1, 1, 1])
# # #
# # # # Display the video player in the first column
# # # with col2:
# # #     st.write('Video Player')
# # #     video_file = open('C:/Users/kclar/PycharmProjects/VOZ_trigger/static/video.mp4', 'rb')
# # #     video_bytes = video_file.read()
# # #     st.video(video_bytes)
# # #
# # #     # Apply CSS to adjust the size of the video player
# # #     st.markdown(
# # #         f'<style>video {{ width: {geo_data.shape[1]}px; height: {geo_data.shape[0]}px; }}</style>',
# # #         unsafe_allow_html=True
# # #     )
# # #
# # # # Display the bubble chart in the second column
# # # with col1:
# # #     st.plotly_chart(fig, use_container_width=True)
# # #
# # # # Display the GeoMap in the third column
# # # with col3:
# # #     st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
# # #     st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
# # #     st.pydeck_chart(pdk.Deck(
# # #         map_style="mapbox://styles/mapbox/light-v9",
# # #         initial_view_state=pdk.ViewState(
# # #             latitude=geo.lat,
# # #             longitude=geo.lng,
# # #             zoom=11,
# # #             pitch=50,
# # #         ),
# # #         layers=[
# # #             pdk.Layer(
# # #                 "ScatterplotLayer",
# # #                 data=geo_data,
# # #                 get_position=["Longitude", "Latitude"],
# # #                 get_radius=200,
# # #                 get_fill_color=[255, 0, 0],  # Red color
# # #             ),
# # #         ],
# # #     ))
# # #
# # # # Create a new layout for the tables below the existing content
# # # col4, col5 = st.columns(2)
# # #
# # # # Display positive and negative phrases side by side in the lower center of the page
# # # with col4:
# # #     st.write('Positive Phrases')
# # #     positive_phrases = [line.strip() for line in content2]
# # #     st.dataframe(pd.DataFrame(positive_phrases, columns=["Positive Phrases"]), height=500)
# # #
# # # with col5:
# # #     st.write('Negative Phrases')
# # #     negative_phrases = [line.strip for line in content1]
# # #     st.dataframe(pd.DataFrame(negative_phrases, columns=["Negative Phrases"]), height=500)
# #
# # #
# # # import pandas as pd
# # # import plotly.express as px
# # # import pydeck as pdk
# # # import geocoder
# # # import streamlit as st
# # #
# # # # Define the paths to your text files
# # # file_path1 = "Negative.txt"
# # # file_path2 = "positive.csv"  # Change this to the path of your positive text file
# # #
# # # # Read the content of the text files and split into lines
# # # with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
# # #     content1 = file1.readlines()
# # #     content2 = file2.readlines()
# # #
# # # # Calculate the line counts
# # # line_count1 = len(content1)
# # # line_count2 = len(content2)
# # #
# # # # Create a bubble chart using Plotly with red for negative and green for positive
# # # data = pd.DataFrame({
# # #     'File': ['Negative', 'Positive'],
# # #     'Line Count': [line_count1, line_count2]
# # # })
# # #
# # # fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Line Count Comparison', color='File')
# # #
# # # # Get real-time geo-location of the computer
# # # geo = geocoder.ip('me')
# # #
# # # # Create a GeoMap using Pydeck
# # # geo_data = pd.DataFrame({
# # #     'Latitude': [geo.lat],
# # #     'Longitude': [geo.lng],
# # # })
# # #
# # # # Set the page layout to have a centered title
# # # st.set_page_config(layout="wide")
# # #
# # # # Center the title
# # # st.title("Your Data Visualization")
# # #
# # # # Create a layout with three columns: one for the video, one for the chart, and one for the phrases
# # # col1, col2, col3 = st.columns([1, 1, 1])
# # #
# # # # Display the video player in the first column
# # # with col2:
# # #     st.write('Video Player')
# # #     video_file = open('C:/Users/kclar/PycharmProjects/VOZ_trigger/static/video.mp4', 'rb')
# # #     video_bytes = video_file.read()
# # #     st.video(video_bytes)
# # #
# # # # Display the bubble chart in the second column
# # # with col1:
# # #     st.plotly_chart(fig, use_container_width=True)
# # #
# # # # Display the GeoMap in the third column
# # # with col3:
# # #     st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
# # #     st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
# # #     st.pydeck_chart(pdk.Deck(
# # #         map_style="mapbox://styles/mapbox/light-v9",
# # #         initial_view_state=pdk.ViewState(
# # #             latitude=geo.lat,
# # #             longitude=geo.lng,
# # #             zoom=11,
# # #             pitch=50,
# # #         ),
# # #         layers=[
# # #             pdk.Layer(
# # #                 "ScatterplotLayer",
# # #                 data=geo_data,
# # #                 get_position=["Longitude", "Latitude"],
# # #                 get_radius=200,
# # #                 get_fill_color=[255, 0, 0],  # Red color
# # #             ),
# # #         ],
# # #     ))
# # #
# # # # Create a new layout for the tables below the existing content
# # # col4, col5 = st.columns(2)
# # #
# # # # Display positive and negative phrases side by side in the center of the page
# # # with col4:
# # #     st.write('Positive Phrases')
# # #     positive_phrases = [line.strip() for line in content2]
# # #     st.dataframe(pd.DataFrame(positive_phrases, columns=["Positive Phrases"]))
# # #
# # # with col5:
# # #     st.write('Negative Phrases')
# # #     negative_phrases = [line.strip() for line in content1]
# # #     st.dataframe(pd.DataFrame(negative_phrases, columns=["Negative Phrases"]))
# # #
# #
# # import pandas as pd
# # import plotly.express as px
# # import pydeck as pdk
# # import geocoder
# # import streamlit as st
# #
# # # Define the paths to your text files
# # file_path1 = "Negative.txt"
# # file_path2 = "positive.csv"  # Change this to the path of your positive text file
# #
# # # Read the content of the text files and split into lines
# # with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
# #     content1 = file1.readlines()
# #     content2 = file2.readlines()
# #
# # # Calculate the line counts
# # line_count1 = len(content1)
# # line_count2 = len(content2)
# #
# # # Create a bubble chart using Plotly with red for negative and green for positive
# # data = pd.DataFrame({
# #     'File': ['Negative', 'Positive'],
# #     'Line Count': [line_count1, line_count2]
# # })
# #
# # fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Line Count Comparison', color='File')
# #
# # # Get real-time geo-location of the computer
# # geo = geocoder.ip('me')
# #
# # # Create a GeoMap using Pydeck
# # geo_data = pd.DataFrame({
# #     'Latitude': [geo.lat],
# #     'Longitude': [geo.lng],
# # })
# #
# # # Set the page layout to have a centered title
# # st.set_page_config(layout="wide")
# #
# # # Center the title
# # st.title("Your Data Visualization")
# #
# # # Create a layout with three columns: one for the video, one for the chart, and one for the phrases
# # col1, col2, col3 = st.columns([1, 1, 1])
# #
# # # Display the video player in the first column
# # with col2:
# #     st.write('Video Player')
# #     video_file = open('C:/Users/kclar/PycharmProjects/VOZ_trigger/static/video.mp4', 'rb')
# #     video_bytes = video_file.read()
# #     st.video(video_bytes)
# #
# # # Display the bubble chart in the second column
# # with col1:
# #     st.plotly_chart(fig, use_container_width=True)
# #
# # # Display the GeoMap in the third column
# # with col3:
# #     st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
# #     st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
# #     st.pydeck_chart(pdk.Deck(
# #         map_style="mapbox://styles/mapbox/light-v9",
# #         initial_view_state=pdk.ViewState(
# #             latitude=geo.lat,
# #             longitude=geo.lng,
# #             zoom=11,
# #             pitch=50,
# #         ),
# #         layers=[
# #             pdk.Layer(
# #                 "ScatterplotLayer",
# #                 data=geo_data,
# #                 get_position=["Longitude", "Latitude"],
# #                 get_radius=200,
# #                 get_fill_color=[255, 0, 0],  # Red color
# #             ),
# #         ],
# #     ))
# #
# # # Create a new layout for the tables below the existing content
# # col4 = st.columns(1)
# #
# # # Display combined positive and negative phrases in a single table
# # with col4:
# #     st.write('Combined Phrases')
# #     combined_phrases = [line.strip() for line in content2] + [line.strip() for line in content1]
# #     st.dataframe(pd.DataFrame(combined_phrases, columns=["Combined Phrases"]))
# # WORKING CODE 10/13
# import pandas as pd
# import plotly.express as px
# import pydeck as pdk
# import geocoder
# import streamlit as st
#
# # Define the paths to your text files
# file_path1 = "Negative.txt"
# file_path2 = "positive.csv"  # Change this to the path of your positive text file
#
# # Read the content of the text files and split into lines
# with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
#     content1 = file1.readlines()
#     content2 = file2.readlines()
#
# # Find the maximum number of lines in both files
# max_lines = max(len(content1), len(content2))
#
# # Pad the shorter list with empty strings to make them of equal length
# content1.extend([''] * (max_lines - len(content1)))
# content2.extend([''] * (max_lines - len(content2)))
#
# # Create a DataFrame with two columns: 'Negative' and 'Positive'
# df = pd.DataFrame({
#     'Negative': content1,
#     'Positive': content2
# })
#
# # Create a bubble chart using Plotly with red for negative and green for positive
# data = pd.DataFrame({
#     'File': ['Negative', 'Positive'],
#     'Line Count': [len(content1), len(content2)]
# })
#
# fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Realtime Word Analysis', color='File')
#
# # Get real-time geo-location of the computer
# geo = geocoder.ip('me')
import pandas as pd
import plotly.express as px
import pydeck as pdk
import geocoder
import streamlit as st
from streamlit import components

# Define the paths to your text files
file_path1 = "Negative.txt"
file_path2 = "positive.txt"  # Change this to the path of your positive text file

# Read the content of the text files and split into lines
with open(file_path1, "r") as file1, open(file_path2, "r") as file2:
    content1 = file1.readlines()
    content2 = file2.readlines()

# Find the maximum number of lines in both files
max_lines = max(len(content1), len(content2))

# Pad the shorter list with empty strings to make them of equal length
content1.extend([''] * (max_lines - len(content1)))
content2.extend([''] * (max_lines - len(content2)))

# Create a DataFrame with two columns: 'Negative' and 'Positive'
df = pd.DataFrame({
    'Negative': content1,
    'Positive': content2
})

# Create a bubble chart using Plotly with red for negative and green for positive
data = pd.DataFrame({
    'File': ['Negative', 'Positive'],
    'Line Count': [len(content1), len(content2)]
})

fig = px.scatter(data, x='File', y='Line Count', size='Line Count', title='Realtime Word Analysis', color='File')

# Get real-time geo-location of the computer
geo = geocoder.ip('me')

# Create a GeoMap using Pydeck
geo_data = pd.DataFrame({
    'Latitude': [geo.lat],
    'Longitude': [geo.lng],
})

# Set the page layout to have a centered title
st.set_page_config(layout="wide")
# Embed a logo on the left
st.image('https://img1.wsimg.com/isteam/ip/e66af92a-07a8-4ac6-8d3f-a41caa301a88/blob-65affbe.png/:/rs=w:184,h:158,cg:true,m/cr=w:184,h:158/qt=q:95', use_column_width=100)

# Create a layout with three columns: one for the video, one for the chart, and one for the table
col1, col2, col3 = st.columns([1, 1, 1])


# Display the video player in the first column
with col2:
    st.write('Encounter In Realtime')
    video_file = open('C:/Users/kclar/PycharmProjects/VOZ_trigger/static/video.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

# Display the bubble chart in the second column
with col1:
    st.plotly_chart(fig, use_container_width=True)

# Display the GeoMap in the third column
with col3:
    st.write(f"Location: {geo.city}, {geo.state}, {geo.country}")
    st.write(f"Latitude: {geo.lat}, Longitude: {geo.lng}")
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=geo.lat,
            longitude=geo.lng,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=geo_data,
                get_position=["Longitude", "Latitude"],
                get_radius=200,
                get_fill_color=[255, 0, 0],  # Red color
            ),
        ],
    ))

# # Create a container for the table and the paragraph text
# table_col, paragraph_col = st.columns([1, 1])
#
# # Display the combined table with negative and positive data values in the first column
# with table_col:
#     st.write('Combined Phrases')
#     st.dataframe(df)
#
# # Use CSS to style and align the attached text to the right of the table in the second column
# with st.markdown(
#     """
#     <div style="text-align: left; padding-left: 10px;">
#         Oftentimes the intersection of positive words in a conversation can blend with negative words.
#         Occurring in an argument or confrontation, The Encounter Engineering platform provides a real-time monitor of this type of interaction.
#         So when your loved one that wears our wearable technology has a negative interaction based on the usage of dangerous keywords,
#         the loved one is now empowered to advocate in real-time. You should either call the police or call a bondsman.
#         You may also need to, depending on the interaction, call a lawyer or even the State Department embassy if traveling abroad.
#         With the awareness of the international and the ability to share with your community, law enforcement, and or legal defense makes this platform very powerful.
#         Always Aware, Always Safe, Always an advocate.
#     </div>
#     """,
#     unsafe_allow_html=True
# ):
#     pass
import streamlit as st

# Create a container for the table and the paragraph text
col = st.columns([2, 1])  # Adjust the width ratio as needed

# Display the combined table with negative and positive data values in the first column
with col[0]:
    st.write('Combined Phrases')
    st.dataframe(df, width=810)  # Adjust the width as needed

# Use CSS to style and align the attached text to the right of the table in the second column
with col[1]:
    st.markdown(
        """
        <div style="text-align: left; padding-left: 10px;">
            Oftentimes the intersection of positive words in a conversation can blend with negative words. 
            Occurring in an argument or confrontation, The Encounter Engineering platform provides a real-time monitor of this type of interaction. 
            So when your loved one that wears our wearable technology has a negative interaction based on the usage of dangerous keywords, 
            the loved one is now empowered to advocate in real-time. You should either call the police or call a bondsman. 
            You may also need to, depending on the interaction, call a lawyer or even the State Department embassy if traveling abroad. 
            With the awareness of the international and the ability to share with your community, law enforcement, and or legal defense makes this platform very powerful. 
            Always Aware, Always Safe, Always an advocate.
        </div>
        """,
        unsafe_allow_html=True
    )


