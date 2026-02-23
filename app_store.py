import feedparser
import pandas as pd


def fetch_app_store_reviews(app_id: str) -> pd.DataFrame:
    try:
        url = f"https://itunes.apple.com/rss/customerreviews/id={app_id}/sortBy=mostRecent/json"
        feed = feedparser.parse(url)

        data = []

        for entry in feed.entries:
            data.append({
                "source": "App Store",
                "date": entry.published,
                "text": entry.content[0].value,
                "rating": entry.im_rating
            })

        return pd.DataFrame(data)

    except Exception as e:
        print("App Store Error:", e)
        return pd.DataFrame()