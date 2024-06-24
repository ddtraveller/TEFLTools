import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from io import StringIO

# Simulating data creation (as if from a text file or HTML table)
data = '''
Date,Municipality,Product,Sales,Price
2023-01-01,Dili,Rice,100,1.5
2023-01-02,Baucau,Corn,150,1.2
2023-01-03,Aileu,Coffee,80,3.0
2023-01-04,Dili,Rice,120,1.5
2023-01-05,Ermera,Coffee,90,3.2
2023-01-06,Baucau,Corn,130,1.3
2023-01-07,Dili,Coffee,70,3.1
'''

# Reading data into a pandas DataFrame
df = pd.read_csv(StringIO(data))

print("Original Data:")
print(df)

# Data cleaning using regular expressions
def clean_product_name(name):
    return re.sub(r'[^a-zA-Z]', '', name).lower()

df['CleanProduct'] = df['Product'].apply(clean_product_name)

print("\nData after cleaning product names:")
print(df)

# Advanced spreadsheet techniques

# 1. Pivot Tables
pivot_table = pd.pivot_table(df, values='Sales', index=['Municipality'], columns=['CleanProduct'], aggfunc=np.sum, fill_value=0)
print("\nPivot Table (Total Sales by Municipality and Product):")
print(pivot_table)

# 2. VLOOKUP equivalent
price_lookup = df.set_index('CleanProduct')['Price'].to_dict()
df['LookedUpPrice'] = df['CleanProduct'].map(price_lookup)
print("\nData with Looked Up Prices:")
print(df)

# 3. Data Aggregation
aggregated_data = df.groupby('Municipality').agg({
    'Sales': ['sum', 'mean'],
    'Price': ['min', 'max']
})
print("\nAggregated Data:")
print(aggregated_data)

# 4. Conditional Formatting (using pandas style)
def highlight_max(s):
    is_max = s == s.max()
    return ['background-color: yellow' if v else '' for v in is_max]

styled_df = df.style.apply(highlight_max, subset=['Sales', 'Price'])
print("\nDataFrame with Conditional Formatting (max values highlighted):")
print(styled_df)

# 5. Data Visualization
plt.figure(figsize=(12, 6))
df.groupby('Municipality')['Sales'].sum().plot(kind='bar')
plt.title('Total Sales by Municipality')
plt.xlabel('Municipality')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Time Series Analysis
df['Date'] = pd.to_datetime(df['Date'])
time_series = df.set_index('Date').resample('D')['Sales'].sum()
print("\nTime Series of Daily Sales:")
print(time_series)

plt.figure(figsize=(12, 6))
time_series.plot()
plt.title('Daily Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# 7. Data Filtering
high_value_sales = df[df['Sales'] * df['Price'] > 200]
print("\nHigh Value Sales (Total Value > 200):")
print(high_value_sales)

# 8. Custom Functions (similar to Excel formulas)
def calculate_total_value(row):
    return row['Sales'] * row['Price']

df['TotalValue'] = df.apply(calculate_total_value, axis=1)
print("\nData with Calculated Total Value:")
print(df)

print("\nThis script demonstrates advanced spreadsheet techniques using Python and pandas.")
print("It covers data cleaning, pivot tables, VLOOKUP, aggregation, conditional formatting,")
print("data visualization, time series analysis, filtering, and custom functions.")