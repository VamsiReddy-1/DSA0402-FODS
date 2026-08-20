import pandas as pd

# Read stock data from CSV
df = pd.read_csv("stock_data.csv")

# Display the stock data
print("Stock Data")
print(df)

# Calculate variability measures
mean_price = df["Close"].mean()
minimum_price = df["Close"].min()
maximum_price = df["Close"].max()
price_range = maximum_price - minimum_price
standard_deviation = df["Close"].std()

# Display results
print("\nStock Price Analysis")
print("Mean Closing Price:", mean_price)
print("Minimum Closing Price:", minimum_price)
print("Maximum Closing Price:", maximum_price)
print("Price Range:", price_range)
print("Standard Deviation:", standard_deviation)
