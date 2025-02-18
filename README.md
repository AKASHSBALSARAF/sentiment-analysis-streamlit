# India Today Sentiment Analysis Dashboard (https://docs.streamlit.io/)

This project provides insights into the sentiment trends of India Today's cover stories from January 2018 to February 2025. The sentiment analysis is based on automated models that analyze the sentiment conveyed in the article titles. The tool also tracks the frequency of words used in the cover stories and visualizes sentiment trends over time.

## Features

- **Sentiment Trends Over Time:** Visualize how sentiments have evolved across multiple years.
- **Most Frequent Words:** Analyze the most frequently used words in India Today’s cover stories.
- **Sentiment Distribution:** View how sentiments like positive, negative, and neutral are distributed over time.
- **Rolling Sentiment Analysis:** Track sentiment changes dynamically for each year and month.
- **Interactive Graphs:** Use interactive graphs for sentiment comparison, word trends, and more.
- **Word Cloud Visualization:** Display a word cloud of the most frequent words in the cover stories.

## Data Sources

The data presented here was sourced from archived issues of **India Today** through the **Wayback Machine**. Sentiment scores were assigned to each cover story using machine learning models that analyze the sentiment of article titles.

## Limitations

- The sentiment analysis provided may not fully capture the nuance and context of each cover story.
- Sentiment scores are based on an automated model and may contain inaccuracies.
- This project is intended for educational and research purposes, and should not be used for decision-making.

## Getting Started

Follow these steps to get the project running locally:

### Prerequisites

- Python 3.x
- Streamlit
- Pandas
- Plotly
- Matplotlib
- Numpy
- WordCloud

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/india-today-sentiment-analysis.git
    cd india-today-sentiment-analysis
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. Open your browser and visit the Streamlit app at `http://localhost:8501/`.

## Usage

- Use the date range slider to filter the data by time.
- Visualize sentiment trends over time with the bar chart.
- Explore sentiment distribution using the pie chart.
- Interact with the word cloud to see the most frequent words used in the cover stories.
- Inspect raw data and review the details by expanding sections in the app.

## Disclaimer

The sentiment analysis results provided by this dashboard are based on an automated model and are intended for illustrative and educational purposes only. The results should not be used for decision-making.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
