from collections import Counter
import re


def extract_keywords(texts):
    words = []

    for text in texts:
        tokens = re.findall(r"\b\w+\b", str(text).lower())
        words.extend(tokens)

    return Counter(words)


def prioritize_issues(df):
    negative_df = df[df["sentiment"] == "negative"]

    keywords = extract_keywords(negative_df["text"])

    return keywords.most_common(10)