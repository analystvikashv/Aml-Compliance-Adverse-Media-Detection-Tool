Adverse Media News Detection Tool
Overview
This tool is designed to detect adverse media news related to companies or individuals. It leverages Python, Streamlit, and sentiment analysis to flag potential financial crime, reputational risk, or negative coverage. The interface is simple, interactive, and compliance-style, making it useful for AML/KYC workflows, risk analysts, and researchers.

✨ Features
- Fetches real-time news articles using NewsAPI.
- Performs sentiment analysis on headlines.
- Flags adverse articles based on negative sentiment and financial crime keywords (fraud, corruption, money laundering, sanctions, insider trading, etc.).
- Displays:
- Clickable URLs to original articles.
- Source name & published date.
- Sentiment score & severity level (High/Medium/Keyword Flag).
- Provides a sentiment distribution chart for quick risk overview.
- Handles errors gracefully (empty input, API issues, no articles found).

🛠 Requirements
- Python 3.8+
- Libraries:
- streamlit
- requests
- 
- textblob
Install dependencies:
pip install streamlit requests textblob



🚀 How to Run
- Save the script as adverse_news_tool.py.
- Open terminal/command prompt in the folder containing the file.
- Run:
streamlit run adverse_news_tool.py
- 
- A local web app will open in your browser (default: http://localhost:8501).

📊 Sentiment Distribution
The chart shows how articles are spread across negative, neutral, and positive sentiment scores:
- Negative (<0) → Potential adverse coverage.
- Neutral (≈0) → Balanced or factual reporting.
- Positive (>0) → Favorable coverage.
This helps visualize the overall tone of media coverage around the entity.


Notes
- You must replace YOUR_API_KEY in the script with a valid NewsAPI key.
- Free API tiers may have request limits.
- This tool is for educational and research purposes. It should not replace professional compliance systems.

📂 Future Enhancements
- Add CSV/Excel export for flagged articles.
- Integrate VADER sentiment analysis for sharper headline detection.
- Enable alerts/notifications when new adverse news appears.
- Add filters (date range, source type, region).

