import pandas as pd

property_data = pd.DataFrame({
    "Property_ID": [101,102,103,104,105],
    "Location": ["Chennai","Chennai","Bangalore","Hyderabad","Bangalore"],
    "Bedrooms": [3,5,4,6,2],
    "Area": [1500,2500,1800,3200,1400],
    "Listing_Price": [6500000,9800000,7200000,12500000,5800000]
})

print("Average Listing Price by Location")
print(property_data.groupby("Location")["Listing_Price"].mean())

print("\nProperties with more than 4 Bedrooms")
print(property_data[property_data["Bedrooms"] > 4])

print("\nProperty with Largest Area")
print(property_data.loc[property_data["Area"].idxmax()])
