import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from wordcloud import WordCloud
import os

# Define base path (relative to the project directory)
base_path = os.path.dirname(os.path.abspath(__file__))

# Set page layout to extend width and use a modern theme
st.set_page_config(layout="wide", page_title="India Today Sentiment Analysis", page_icon="🗞️")

# Load the data from the Excel file
cover_sentiment_data = pd.read_excel(os.path.join(base_path, 'data', 'INDIA_TODAY_COVER_SENTIMENT.xlsx'))

# Convert the date column to datetime format so we can work with it more easily
cover_sentiment_data['DATE'] = pd.to_datetime(cover_sentiment_data['DATE'])

# Streamlit Title (no font size increase)
st.markdown("<h1 style='font-size:50px;'>India Today Cover Story Analysis️</h1>", unsafe_allow_html=True)

# Project Description for the users
st.markdown("""
    <h2 style='font-size:20px;'>This project analyzes the cover stories of <strong>India Today</strong> from January 2018 to February 2025.
    It visualizes sentiment trends, word frequencies, and sentiment distribution across time.
    The data is sourced from archived versions of <strong>India Today</strong> magazine through the <strong>Wayback Machine</strong>.</h2>
""", unsafe_allow_html=True)

# Date Range Slider to allow users to select the time period they want to view
start_date, end_date = st.slider(
    "Select Date Range",
    min_value=cover_sentiment_data['DATE'].min().date(),  # Convert to date
    max_value=cover_sentiment_data['DATE'].max().date(),  # Convert to date
    value=(cover_sentiment_data['DATE'].min().date(), cover_sentiment_data['DATE'].max().date()),  # Default range
)

# Filter the data based on the selected date range
filtered_data = cover_sentiment_data[
    (cover_sentiment_data['DATE'] >= pd.to_datetime(start_date)) & 
    (cover_sentiment_data['DATE'] <= pd.to_datetime(end_date))
]

# Sentiment Trends Over Time - A bar chart that shows sentiment over time (positive in green, negative in red)
st.subheader('Sentiment Trends Over Time')

# Create a new column for color based on sentiment score (green for positive, red for negative)
filtered_data['Color'] = np.where(filtered_data['SENTIMENT_SCORE'] > 0, 'green', 'red')

# Create the bar chart using Plotly
fig = px.bar(filtered_data, x='DATE', y='SENTIMENT_SCORE', color='Color',
             color_discrete_map={'green': 'green', 'red': 'red'},
             title=" ", height=800)  # Increased height for better visual
fig.update_xaxes(title='Date')
fig.update_yaxes(title='Sentiment Score')
fig.update_layout(title_x=0.5)  # Center title

# Display the bar chart on the Streamlit app
st.plotly_chart(fig, use_container_width=True)

# Sentiment Distribution - Pie chart that shows the distribution of sentiments (positive, negative, etc.)
st.subheader('Sentiment Distribution')

# Calculate the counts for each sentiment category (positive, neutral, negative)
sentiment_counts = filtered_data['SENTIMENT'].value_counts(dropna=True)
labels = sentiment_counts.index
values = sentiment_counts.values

# Plotly Pie chart
fig2.update_layout(
    plot_bgcolor='#0E1117',  # Dark background for a modern look
    paper_bgcolor='#0E1117',  # Dark paper background for consistency
    title_x=0.5,  # Center the title
    title_font=dict(size=22, color='white'),  # White title font
    legend_title_font=dict(size=15, color='white'),  # White legend font for visibility
    height=770,  # Set the chart height for better spacing
    width=770,   # Set width to maintain symmetry
)
# Customize layout (background and title centering)
fig2.update_layout(
    plot_bgcolor='#0E1117',  # Dark background for a modern look
    paper_bgcolor='#0E1117',  # Dark paper background for consistency
    title_x=0.5,  # Center the title
    title_font=dict(size=22, color='white'),  # White title font
    legend_title_font=dict(size=15, color='white'),  # White legend font for visibility
    height=770,  # Set the chart height for better spacing
    width=770,   # Set width to maintain symmetry
)

# Word Cloud for Frequent Words in the titles of the cover stories
word_freq_data = pd.read_excel(os.path.join(base_path, 'data', 'INDIA_TODAY_COVER_WORD_FREQ.xlsx'))
word_freq_dict = dict(zip(word_freq_data['Word'], word_freq_data['Frequency']))
wordcloud = WordCloud(
    background_color='rgb(14, 17, 23)',  # Dark background for the word cloud
    colormap='YlGnBu',  # Vibrant colormap for visual appeal
    max_font_size=33,  # Font size for the words
    width=275,  # Width of the word cloud image
    height=220  # Height of the word cloud image
).generate_from_frequencies(word_freq_dict)

# Adjust Pie Chart and Word Cloud to display side by side (nice layout)
col1, col2 = st.columns([1.2, 1])  # Proportions for the columns (pie chart on left, word cloud on right)

# Display Pie chart in the first column
with col1:
    st.plotly_chart(fig2, use_container_width=True)

# Display Word Cloud in the second column
with col2:
    st.subheader('Word Cloud')
    st.image(wordcloud.to_array(), use_container_width=True)

# Slider to set the number of top words to display in a bar chart
num_words = st.slider('Select Number of Top Words', min_value=5, max_value=30, value=10, step=1)

# Get the top `num_words` based on the slider selection
top_words = word_freq_data.head(num_words)  # Get the top words according to the slider

# Create a bar chart to display the most frequent words
fig3 = px.bar(
    top_words, 
    x='Word', 
    y='Frequency', 
    title="Most Used Words", 
    color='Frequency',  # Color the bars based on frequency
    color_continuous_scale='Blues',  # Use a blue gradient for color
    hover_data={'Word': True, 'Frequency': True},  # Show word and frequency when hovering
)

# Rotate x-axis labels for better readability
fig3.update_xaxes(
    title='Words', 
    tickangle=-0,  # No angle rotation for labels
    tickmode='array',  # Make sure all words are displayed
    title_font=dict(size=16, color='#FFFFFF')  # Title font size and color
)

# Update y-axis to make it clear
fig3.update_yaxes(
    title='Frequency',
    title_font=dict(size=16, color='#FFFFFF')
)

# Set transparent background and better fonts
fig3.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper background
    font=dict(size=14, family="Arial, sans-serif"),
    title_font=dict(size=22, color='#FFFFFF', family="Helvetica, Arial"),  # Larger title
    coloraxis_showscale=False,  # Hide color scale
    margin=dict(t=40, b=60, l=40, r=40),  # Add margins to make the chart look better
    height=700,  # Set height of the graph
    width=800  # Set width of the graph
)

# Display the bar chart on the Streamlit app
st.plotly_chart(fig3, use_container_width=True)

# Load additional standardized data for inspection
data_path = os.path.join(base_path, 'data', 'INDIA_TODAY_COVER_STANDARDIZED.xlsx')
df = pd.read_excel(data_path)

# Section: Inspect Raw Data (View Data and Disclaimer)
st.markdown("""
    <h2 style='font-size:30px;'>📂 Inspect Raw Data</h2>
""", unsafe_allow_html=True)

with st.expander("Click to view disclaimer details"):
    st.markdown("""
    Below is a sample of the raw data with clickable links in the **Wayback Archive** column.  
    Use the slider below to adjust the number of rows displayed. Displaying fewer rows improves performance.  
    Click column headers to sort.
    """, unsafe_allow_html=True)

    # Slider for row selection (to avoid performance issues)
    num_rows = st.slider("Select number of rows to display", min_value=5, max_value=len(df), value=10, step=5)

    # Display the dataframe with clickable links
    st.write(df.head(num_rows).to_html(escape=False), unsafe_allow_html=True)

# Section: Disclaimer (inform users about the limitations of the analysis)
st.markdown("""
    <h2 style='font-size:30px;'>⚠️ Disclaimer</h2>
""", unsafe_allow_html=True)

with st.expander("Click to view disclaimer details"):
    st.markdown("""
        <h3 style='font-size:17px;'>The sentiment analysis provided on this dashboard is based on the coverage and titles of archived India Today stories from 2018-2025. The sentiment scores are generated through automated models, which may not always reflect the nuances of each story. 

    This tool is intended for educational and research purposes only. The results presented should not be taken as definitive or relied upon for decision-making. 

    **Please Note:**
    - The sentiment scores do not represent absolute factual statements and may contain inaccuracies.
    - The analysis should not be substituted for professional judgment or original sources.
    - This is a demonstration project and is not endorsed by any media organization.
    - No liability is assumed for errors or misinterpretations of the data.

    By using this site, you acknowledge that the information here is for illustrative purposes and should be treated accordingly.</h3>
    """, unsafe_allow_html=True)

# Section: About the Project (info about the project)
st.markdown("""
    <h2 style='font-size:30px;'>🔍 About the Project</h2>
""", unsafe_allow_html=True)

with st.expander("Click to view project details"):
    st.markdown("""
        <h3 style='font-size:17px;'>India Today Sentiment Analysis offers insights into the sentiment trends of India Today's cover stories between January 2018 and February 2025. 

    This dashboard allows users to explore sentiment fluctuations across time, track the frequency of words, and understand the broader trends that have shaped India Today's narrative over the years. 

    **Features:**
    - **Sentiment Trends Over Time:** Visualize how sentiments have evolved over the past several years.
    - **Most Frequent Words:** Analyze the most frequently used words in India Today’s cover stories.
    - **Sentiment Distribution:** View how different sentiments like positive, negative, and neutral are distributed across time.
    - **Rolling Sentiment Analysis:** Track sentiment changes dynamically for each year and month.

    **Data Sources:**
    The data presented here was sourced from archived issues of India Today through the Wayback Machine. Sentiment scores were assigned to each cover story using machine learning models that analyze the sentiment conveyed in the article titles. 

    **Note on Limitations:**
    While this tool provides insights, the sentiment scores generated are not perfect. Due to the automated nature of the model, it’s possible for some results to be misleading or inaccurate. We are continuously working to refine and improve the model to provide more accurate and meaningful analysis.

    This project aims to illustrate the potential of sentiment analysis in studying media narratives and is not intended for commercial use.</h3>
    """, unsafe_allow_html=True)


# Contact Section with Stable LinkedIn and GitHub Icons
st.markdown("""
    <h2 style='font-size:28px; color:#1f77b4;'>📬 Get in Touch!</h2>
    <p style='font-size:20px; color:#ffffff;'>
        If you have any questions or just want to connect, feel free to reach out to me on LinkedIn or check out my GitHub!
    </p>
    <p style='font-size:22px; font-weight:bold; color:#ffffff; text-align: center;'>
        🔗 <span style="font-weight: bold;">Akash Shridhar Balsaraf</span>
    </p>
    <!-- LinkedIn Icon and GitHub Icon -->
    <div style="display: flex; justify-content: center; gap: 20px; align-items: center;">
        <a href="https://www.linkedin.com/in/akash-shridhar-balsaraf/" target="_blank">
            <img src="https://www.svgrepo.com/show/448234/linkedin.svg" alt="LinkedIn"
                 style="width: 60px; height: 60px;">
        </a>
        <a href="https://github.com/AKASHSBALSARAF" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub"
                 style="width: 60px; height: 60px;">
        </a>
    </div>
""", unsafe_allow_html=True)










