import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
data = pd.read_csv(r"C:\Users\krott\Documents\[Github]\assistance-systems-recommendation-system\Leander\data.csv")

# Count the occurrences of each unique year
year_counts = data['year'].value_counts()

# Plotting the frequency of each year
plt.bar(year_counts.index, year_counts.values)

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Frequency')
plt.title('Frequency of Each Year')

# Show the plot
plt.show()

