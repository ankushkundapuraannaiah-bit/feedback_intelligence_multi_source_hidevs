import streamlit as st
import pandas as pd
from analysis.trend import sentiment_trend
from analysis.issues import prioritize_issues
from reports.pdf_report import generate_pdf


st.title("📊 Feedback Intelligence Dashboard")

df = pd.read_csv("../combined_feedback.csv")

# Filters
source = st.selectbox("Source", ["All"] + list(df["source"].unique()))
sentiment = st.selectbox("Sentiment", ["All", "positive", "neutral", "negative"])

filtered = df.copy()

if source != "All":
    filtered = filtered[filtered["source"] == source]

if sentiment != "All":
    filtered = filtered[filtered["sentiment"] == sentiment]

# Metrics
st.metric("Total Feedback", len(filtered))
st.metric("Average Rating", round(filtered["rating"].mean(), 2))

# Trend
trend_df = sentiment_trend(filtered)
st.line_chart(trend_df.set_index("date"))

# Top Issues
st.subheader("Top Issues")
issues = prioritize_issues(filtered)

for word, count in issues:
    st.write(word, count)

# Generate PDF
if st.button("Generate Weekly Report"):

    summary = f"""
    Total Feedback: {len(filtered)}
    Average Rating: {round(filtered['rating'].mean(),2)}
    """

    generate_pdf(summary, trend_df)

    st.success("Report Generated!")