import pandas as pd
import numpy as np

products = []

categories = {
    "Beverages": ["Coca Cola","Pepsi","Sprite","Fanta","Red Bull"],
    "Snacks": ["Lays","Kurkure","Doritos","Pringles","Bingo"],
    "Dairy": ["Amul","Mother Dairy","Nestle","Britannia"],
    "Bakery": ["Britannia","Harvest Gold","Modern"],
    "Personal Care": ["Dove","Lux","Pears","Nivea","Dettol"],
    "Household": ["Surf Excel","Ariel","Harpic","Lizol"]
}

for i in range(1, 501):

    category = np.random.choice(list(categories.keys()))

    brand = np.random.choice(categories[category])

    products.append([
        f"SKU{i:04}",
        f"{brand} Product {i}",
        brand,
        category,
        round(np.random.uniform(20, 500), 2),
        category
    ])

products_df = pd.DataFrame(
    products,
    columns=[
        "sku_id",
        "product_name",
        "brand",
        "category",
        "unit_price",
        "shelf_section"
    ]
)

products_df.to_csv(
    "products.csv",
    index=False
)

print("products.csv generated successfully!")