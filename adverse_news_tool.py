import streamlit as st
import requests
from textblob import TextBlob

# -------------------------------
# Function: Fetch news (title + url + source + published date)
# -------------------------------
def fetch_news(query):
    try:
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey=Your Key"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "articles" not in data:
            return []
        return [
            {
                "title": article.get("title", "No Title"),
                "url": article.get("url", ""),
                "source": article.get("source", {}).get("name", "Unknown"),
                "published": article.get("publishedAt", "Unknown Date")
            }
            for article in data["articles"]
        ]
    except Exception as e:
        st.error(f"Error fetching news: {e}")
        return []

# -------------------------------
# Function: Analyze sentiment
# -------------------------------
def analyze_sentiment(articles):
    results = []
    for art in articles:
        blob = TextBlob(art["title"])
        polarity = blob.sentiment.polarity
        art["sentiment"] = polarity
        results.append(art)
    return results

# -------------------------------
# Function: Flag adverse news
# -------------------------------
def flag_adverse(results):
    adverse = []
    keywords = [
        "fraud", "lawsuit", "scandal", "corruption", "bankruptcy",
        "money laundering", "sanction", "tax evasion", "crime", "drug trafficking",
        "terrorism", "bribery", "embezzlement", "insider trading"
    ]
    for art in results:
        if art["sentiment"] < 0 or any(k in art["title"].lower() for k in keywords):
            adverse.append(art)
    return adverse

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("📰 Adverse Media News Detection Tool")

query = st.text_input("Enter company or individual name:")

if query.strip():  # ✅ ensures query is not empty
    articles = fetch_news(query)
    if not articles:
        st.warning("No articles found. Try another name or check your API key.")
    else:
        sentiments = analyze_sentiment(articles)
        adverse_articles = flag_adverse(sentiments)

        st.write(f"Total Articles Retrieved: {len(articles)}")
        st.write(f"Adverse Articles Flagged: {len(adverse_articles)}")

        st.subheader("⚠️ Adverse News Found:")
        if adverse_articles:
            for art in adverse_articles:
                severity = (
                    "High" if art["sentiment"] < -0.3
                    else "Medium" if art["sentiment"] < 0
                    else "Keyword Flag"
                )
                st.markdown(
                    f"- [{art['title']}]({art['url']}) "
                    f"<br>Source: **{art['source']}** | Published: {art['published']} "
                    f"<br>Sentiment Score: `{art['sentiment']:.2f}` | Severity: **{severity}**",
                    unsafe_allow_html=True
                )
        else:
            st.info("No adverse articles detected.")

        # Chart
        scores = [a["sentiment"] for a in sentiments]
        if scores:
            st.subheader("📊 Sentiment Distribution")
            st.bar_chart(scores)
else:
    st.info("Please enter a company or individual name to begin.")
