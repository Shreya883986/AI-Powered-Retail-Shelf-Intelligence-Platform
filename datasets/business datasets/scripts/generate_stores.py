import pandas as pd
import numpy as np
from faker import Faker

fake = Faker("en_IN")

stores = []

cities = [
    ("Delhi", "Delhi", "North"),
    ("Mumbai", "Maharashtra", "West"),
    ("Pune", "Maharashtra", "West"),
    ("Bangalore", "Karnataka", "South"),
    ("Chennai", "Tamil Nadu", "South"),
    ("Hyderabad", "Telangana", "South"),
    ("Kolkata", "West Bengal", "East"),
    ("Lucknow", "Uttar Pradesh", "North"),
    ("Jaipur", "Rajasthan", "North"),
    ("Ahmedabad", "Gujarat", "West")
]

for i in range(1, 51):

    city, state, region = cities[np.random.randint(len(cities))]

    stores.append([
        f"S{i:03}",
        f"RetailMart {city}-{i}",
        city,
        state,
        region,
        np.random.choice(["Small", "Medium", "Large"]),
        np.random.randint(2015, 2025)
    ])

stores_df = pd.DataFrame(
    stores,
    columns=[
        "store_id",
        "store_name",
        "city",
        "state",
        "region",
        "store_size",
        "opening_year"
    ]
)

stores_df.to_csv(
    "stores.csv",
    index=False
)

print("stores.csv generated successfully")