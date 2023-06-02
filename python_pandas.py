import pandas as pd

# read the sample dataset into a pandas dataframe
data = {
    'Name': ['John', 'Jane', 'Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 28, 35, 22],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [5000, 6000, 55000, 70000, 45000]

}

# Create a Pandas DataFrame from the data dictionary
df = pd.DataFrame(data)


# Display the dataframe
print(df)

# filter the dataframe based on a condition
filtered_df = df[df['Age']>25]
print(filtered_df)

avg_salary = df['Salary'].mean()
print(avg_salary)

df['Bonus'] = df['Salary'] * 0.1
print(df)