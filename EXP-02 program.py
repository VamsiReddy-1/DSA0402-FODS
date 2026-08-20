import numpy as np

sales = np.array([
    [100, 120, 110],
    [200, 220, 210],
    [150, 160, 170]
])

average_price = np.mean(sales)

print("Sales Data:")
print(sales)

print("\nAverage Price of All Products =", average_price)
