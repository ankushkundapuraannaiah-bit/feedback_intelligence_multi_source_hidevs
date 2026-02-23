import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)

        if "text" not in df.columns:
            raise ValueError("CSV must contain 'text' column")

        df["source"] = "Survey"

        return df

    except Exception as e:
        print("CSV Error:", e)
        return pd.DataFrame()