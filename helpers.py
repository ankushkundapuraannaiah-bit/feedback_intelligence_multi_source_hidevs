import pandas as pd
from analysis.sentiment import analyze_sentiment


def process_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    sentiments = df["text"].apply(analyze_sentiment)

    df["sentiment"] = sentiments.apply(lambda x: x[0])
    df["confidence"] = sentiments.apply(lambda x: x[1])

    return df