import numpy as np

fuel_efficiency = np.array([22, 26, 30, 35, 40])

average_efficiency = np.mean(fuel_efficiency)

car1 = fuel_efficiency[1]
car2 = fuel_efficiency[4]

percentage_improvement = ((car2 - car1) / car1) * 100

print("Fuel Efficiency (mpg):")
print(fuel_efficiency)

print("\nAverage Fuel Efficiency =", average_efficiency, "mpg")

print("Percentage Improvement = {:.2f}%".format(percentage_improvement))
