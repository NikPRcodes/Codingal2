import pandas as pd

df=pd.read_csv("C:/Users/ahake/Desktop/Codingal/Python/After Class Projects")

print(df.head())
import matplotlib.pyplot as plt

# Assuming 'Month' and 'Profit' are the columns in your dataset
plt.figure(figsize=(10,6))
plt.plot(df['Month'], df['Profit'], linestyle=':', marker='o', color='red', linewidth=3, markerfacecolor='black')

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Profit')
plt.title('Month-wise Profit of the Company')

# Display the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.show()

# Assuming the product sales columns are 'Product1', 'Product2', ..., 'ProductN'
products = ['Product1', 'Product2', 'Product3']  # Replace with actual product names

plt.figure(figsize=(10,6))

for product in products:
    plt.plot(df['Month'], df[product], marker='o', linewidth=3, label=product)

# Adding labels, title, and legend
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales Data of All Products Month-Wise')
plt.legend(title='Products')

# Display the plot
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Assuming 'Face Cream Sales' and 'Face Wash Sales' columns are present
plt.figure(figsize=(10,6))
plt.bar(df['Month'], df['Face Cream Sales'], width=0.4, label='Face Cream', align='center', color='blue')
plt.bar(df['Month'], df['Face Wash Sales'], width=0.4, label='Face Wash', align='edge', color='green')

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Comparison of Face Cream and Face Wash Sales')
plt.legend()

# Display the plot
plt.xticks(rotation=45)
plt.grid(True)
plt.show()