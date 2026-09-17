import pandas as pd
import numpy as np

# Create a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Salary': [50000, 60000, 75000, 55000, 70000],
    'Department': ['Sales', 'IT', 'HR', 'Sales', 'IT']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the data
print("Dataset:")
print(df)

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Filter data
print("\nSalaries over 60000:")
print(df[df['Salary'] > 60000])

# Group by department
print("\nAverage salary by department:")
print(df.groupby('Department')['Salary'].mean())

# Add a new column
df['Bonus'] = df['Salary'] * 0.1
print("\nDataset with Bonus column:")
print(df)