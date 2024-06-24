import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the first PDF (Census data)
census_data = {
    'Municipality': ['Aileu', 'Ainaro', 'Atauro', 'Baucau', 'Bobonaro', 'Covalima', 'Dili', 'Ermera', 'Lautem', 'Liquica', 'Manatuto', 'Manufahi', 'Oecusse', 'Viqueque'],
    'Population_2022': [54631, 72989, 10302, 133881, 106543, 73909, 324269, 138080, 69836, 83689, 50989, 60536, 80726, 80054],
    'Population_2015': [48837, 63136, 9274, 123203, 97762, 65301, 268005, 125702, 65240, 71927, 46619, 53691, 68913, 76033],
    'Area_sq_km': [676.0, 869.8, 140.5, 1508.0, 1380.8, 1206.7, 227.6, 770.8, 1813.1, 551.0, 1786.0, 1326.6, 817.2, 1880.4]
}

df_census = pd.DataFrame(census_data)

# Load data from the second PDF (Health indicators)
health_data = {
    'Indicator': ['Under-5 mortality rate (per 1000 live births)', 'Neonatal mortality rate (per 1000 live births)', 'Maternal mortality ratio (per 100,000 live births)'],
    '1990': [175, 55, 1080],
    '2000': [108, 37, 745],
    '2010': [62, 24, 219],
    '2019': [44, 20, 142]
}

df_health = pd.DataFrame(health_data)

print("1. Basic DataFrames created from PDF data:")
print(df_census.head())
print(df_health)

# Calculate population density for 2022
df_census['Population_Density_2022'] = df_census['Population_2022'] / df_census['Area_sq_km']

print("\n2. Merging DataFrames:")
# For this example, we'll create a mock dataframe to merge with df_census
df_mock = pd.DataFrame({
    'Municipality': ['Dili', 'Baucau', 'Ermera', 'Aileu'],
    'HDI_2022': [0.75, 0.68, 0.62, 0.64]
})

df_merged = pd.merge(df_census, df_mock, on='Municipality', how='left')
print(df_merged)

print("\n3. Plotting with Pandas:")

# Line plot
plt.figure(figsize=(12, 6))
df_health.set_index('Indicator').T.plot(marker='o')
plt.title('Health Indicators Over Time')
plt.xlabel('Year')
plt.ylabel('Rate')
plt.legend(title='Indicator', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Bar plot
plt.figure(figsize=(12, 6))
df_census.sort_values('Population_2022', ascending=False).plot(x='Municipality', y=['Population_2015', 'Population_2022'], kind='bar')
plt.title('Population by Municipality')
plt.xlabel('Municipality')
plt.ylabel('Population')
plt.legend(['2015', '2022'])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
df_census['Population_Density_2022'].hist(bins=20, edgecolor='black')
plt.title('Distribution of Population Density (2022)')
plt.xlabel('Population Density (people per sq km)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

print("\n4. Customizing plots with Seaborn:")
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df_census, x='Area_sq_km', y='Population_2022', hue='Municipality', size='Population_Density_2022', sizes=(20, 200))
plt.title('Population vs Area with Population Density')
plt.xlabel('Area (sq km)')
plt.ylabel('Population (2022)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

print("\n5. Exporting processed data:")
# To CSV
df_merged.to_csv('timor_leste_data.csv', index=False)
print("Data exported to CSV: timor_leste_data.csv")

# To Excel
df_merged.to_excel('timor_leste_data.xlsx', index=False, sheet_name='Census_Data')
with pd.ExcelWriter('timor_leste_data.xlsx', mode='a') as writer:
    df_health.to_excel(writer, sheet_name='Health_Indicators', index=False)
print("Data exported to Excel: timor_leste_data.xlsx")

print("\n6. Additional useful Pandas operations:")

# Descriptive statistics
print("Descriptive statistics of population:")
print(df_census['Population_2022'].describe())

# Sorting
print("\nTop 5 municipalities by population density:")
print(df_census.sort_values('Population_Density_2022', ascending=False).head())

# Filtering
print("\nMunicipalities with population over 100,000:")
print(df_census[df_census['Population_2022'] > 100000]['Municipality'].tolist())

# Grouping and aggregation
print("\nAverage population by first letter of municipality name:")
print(df_census.groupby(df_census['Municipality'].str[0])['Population_2022'].mean())

# Pivot table
pivot_health = df_health.melt(id_vars=['Indicator'], var_name='Year', value_name='Value')
pivot_table = pivot_health.pivot_table(values='Value', index='Year', columns='Indicator', aggfunc='first')
print("\nPivot table of health indicators:")
print(pivot_table)

print("\nThis script demonstrates various Pandas and data visualization techniques using Timor-Leste data.")
print("Experiment with the code to learn more about data analysis and visualization!")