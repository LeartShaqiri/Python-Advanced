import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('avgIQpercountry.csv')

print(df.info())

# Show first rows
first_rows = df.head()
print(first_rows)

# Show country column
country_data = df['Country']
print(country_data)

# FIX: wrong syntax for column subset
subset = df[['Country', 'Average IQ']]
print(subset)

# Null mask
null_mask = df.isnull()
null_count = null_mask.sum()
print('\nCount of null values in each column:')
print(null_count)

# Drop null rows
df.dropna(inplace=True)
print('\nDataFrame after dropping rows with null values:')
print(df.info())

# Duplicates
duplicated_count = df.duplicated().sum()
print("\nNumber of duplicated rows:", duplicated_count)

# FIX: consistent variable name
average_iq_per_continent = df.groupby('Continent')['Average IQ'].mean()
print(average_iq_per_continent)

# Clean population formatting
df['Population - 2023'] = df['Population - 2023'].apply(lambda x: float(str(x).replace(',', '')))
print(df.info())

# Total Nobel Prizes by Country
total_nobel_prizes_by_country = df.groupby('Country')['Nobel Prizes'].sum()

sorted_total_nobel_by_country = total_nobel_prizes_by_country.sort_values(ascending=False)

print("\nTotal Nobel Prizes by Country:")
print(sorted_total_nobel_by_country)

# Plot top 10 countries
sorted_total_nobel_by_country.head(10).plot(kind='bar', title='Top 10 Countries by Nobel Prizes')
plt.xlabel('Country')
plt.ylabel('Nobel Prizes')
plt.tight_layout()
plt.show()
