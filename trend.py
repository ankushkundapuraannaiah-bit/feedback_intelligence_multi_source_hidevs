import pandas as pd


def sentiment_trend(df: pd.DataFrame):
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    trend = (
        df.groupby(df["date"].dt.date)["confidence"]
        .mean()
        .reset_index()
    )

    return trend