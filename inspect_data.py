import pandas as pd

# Load dataset
df = pd.read_csv("data/heart.csv")

# Display first five rows
print(df.head())

# Display dataset dimensions
print("Shape:", df.shape)

# Display column names
print("Columns:", df.columns.tolist())

# Display data types
print(df.dtypes)

# Check missing values
print(df.isnull().sum())