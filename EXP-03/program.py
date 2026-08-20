import numpy as np

house_data = np.array([
    [3, 1500, 250000],
    [5, 2200, 450000],
    [4, 1800, 300000],
    [6, 2700, 550000],
    [5, 2400, 500000]
])

houses = house_data[house_data[:, 0] > 4]

average_price = np.mean(houses[:, 2])

print("Houses with More Than 4 Bedrooms:")
print(houses)

print("\nAverage Sale Price =", average_price)
