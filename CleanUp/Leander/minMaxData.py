import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv("data.csv")

# Get the minimum and maximum values for all numeric columns
min_values = data.min()
max_values = data.max()

# Display the results
print("Minimum values:")
print(min_values)

print("\nMaximum values:")
print(max_values)

