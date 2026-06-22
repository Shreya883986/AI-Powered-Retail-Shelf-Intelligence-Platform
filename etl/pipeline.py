from extract import extract_data
from transform import transform_data
from load import load_data


def run_pipeline():

    sales, inventory = extract_data()

    transformed_df = transform_data(
        sales,
        inventory
    )

    load_data(transformed_df)

    print("\nETL Pipeline Executed Successfully")


if __name__ == "__main__":
    run_pipeline()