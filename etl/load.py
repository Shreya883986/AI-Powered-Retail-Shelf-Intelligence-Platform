from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

output_path = (
    BASE_DIR
    / "datasets"
    / "processed datasets"
    / "etl_output.csv"
)


def load_data(df):

    df.to_csv(
        output_path,
        index=False
    )

    print("Loading Completed")