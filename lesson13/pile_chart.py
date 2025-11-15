import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')   # FIXED: read_csv, not read_cvs

# FIXED: 'Nobel Prizes' and .sum()
nobel_prizes_by_country = df.groupby('Continent')['Nobel Prizes'].sum()

# Count number of continents represented (optional)
no_of_countries = nobel_prizes_by_country.count()
print(no_of_countries)

colors = ['goldenrod', 'lightblue', 'lightgreen', 'salmon', 'violet']

plt.figure(figsize=(10,10))

# FIXED: autopct, not autocpt
nobel_prizes_by_country.plot(kind='pie', colors=colors, autopct='%1.1f%%')

plt.title('Distribution of Nobel Prices by Continent')
plt.axis('equal')     # keeps pie chart circular
plt.ylabel("")        # remove y-label
plt.tight_layout()

plt.show()
