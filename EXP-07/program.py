import pandas as pd

order_data = pd.DataFrame({
    "Customer_ID": [101, 102, 101, 103, 102, 104],
    "Order_Date": [
        "2026-07-01",
        "2026-07-02",
        "2026-07-05",
        "2026-07-03",
        "2026-07-06",
        "2026-07-04"
    ],
    "Product_Name": [
        "Laptop",
        "Mouse",
        "Laptop",
        "Keyboard",
        "Mouse",
        "Laptop"
    ],
    "Order_Quantity": [2, 1, 3, 2, 4, 1]
})

order_data["Order_Date"] = pd.to_datetime(order_data["Order_Date"])

customer_orders = order_data.groupby("Customer_ID").size()

average_quantity = order_data.groupby("Product_Name")["Order_Quantity"].mean()

earliest_date = order_data["Order_Date"].min()
latest_date = order_data["Order_Date"].max()

print("Total Orders by Customer")
print(customer_orders)

print("\nAverage Order Quantity by Product")
print(average_quantity)

print("\nEarliest Order Date:", earliest_date.date())
print("Latest Order Date:", latest_date.date())
