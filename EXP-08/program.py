import pandas as pd

sales_data = pd.DataFrame({
    "Product_Name": [
        "Laptop", "Mouse", "Keyboard", "Laptop",
        "Mouse", "Laptop", "Monitor", "Keyboard",
        "Mouse", "Printer", "Monitor", "Laptop"
    ],
    "Quantity_Sold": [
        5, 8, 4, 7,
        3, 6, 2, 5,
        9, 4, 6, 8
    ]
})

top_products = sales_data.groupby("Product_Name")["Quantity_Sold"].sum()

top_products = top_products.sort_values(ascending=False)

print("Top 5 Selling Products")
print(top_products.head(5))
