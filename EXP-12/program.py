import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [22, 24, 28, 32, 35, 34, 31, 30, 29, 27, 25, 23]

rainfall = [20, 25, 35, 45, 70, 120, 180, 160, 110, 80, 40, 25]

# Line Plot for Temperature
plt.figure(figsize=(7,4))
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Scatter Plot for Rainfall
plt.figure(figsize=(7,4))
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.show()
