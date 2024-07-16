import pandas as pd

# Read the CSV file
df = pd.read_csv('data/data.csv')

# Convert the 'bmi' column to float
df['bmi'] = df['bmi'].astype(float)

# Save the updated CSV file
df.to_csv('data/modified_data.csv', index=False)
