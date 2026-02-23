from data_sources.google_play import fetch_google_reviews
from data_sources.app_store import fetch_app_store_reviews
from data_sources.csv_loader import load_csv
from utils.helpers import process_dataframe
import pandas as pd


def run_pipeline():

    google_df = fetch_google_reviews("com.instagram.android", 100)
    app_df = fetch_app_store_reviews("389801252")

    # Optional CSV
    # csv_df = load_csv("survey.csv")

    df = pd.concat([google_df, app_df], ignore_index=True)

    df = process_dataframe(df)

    df.to_csv("combined_feedback.csv", index=False)

    print("Pipeline completed!")


if __name__ == "__main__":
    run_pipeline()