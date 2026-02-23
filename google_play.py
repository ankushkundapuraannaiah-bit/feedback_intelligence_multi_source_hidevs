from google_play_scraper import reviews
import pandas as pd


def fetch_google_reviews(app_id: str, count: int = 200) -> pd.DataFrame:
    try:
        result, _ = reviews(
            app_id,
            lang="en",
            country="us",
            count=count
        )

        data = [{
            "source": "Google Play",
            "date": r["at"],
            "text": r["content"],
            "rating": r["score"]
        } for r in result]

        return pd.DataFrame(data)

    except Exception as e:
        print("Google Play Error:", e)
        return pd.DataFrame()