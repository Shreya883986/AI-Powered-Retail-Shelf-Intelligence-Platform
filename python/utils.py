import pandas as pd


def load_csv(path):
    return pd.read_csv(path)


def save_csv(df, path):
    df.to_csv(path, index=False)
    print(f"Saved successfully → {path}")


def check_missing_values(df):
    print("\nMissing Values:")
    print(df.isnull().sum())


def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"Removed {before-after} duplicate rows")
    return df