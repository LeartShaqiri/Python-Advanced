import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('lesson13/avgIQpercountry.csv')

# Filter for IQ >= 100
filter_df = df[df['Average IQ'] >= 100]

# Sort from highest to lowest
filter_df = filter_df.sort_values(by='Average IQ', ascending=False)

print(filter_df)

plt.figure(figsize=(14, 8))

# Corrected column name
bars = plt.bar(filter_df['Country'], filter_df['Average IQ'])

# Corrected title function
plt.title('Average IQ per Country (IQ >= 100)', fontsize=16)

plt.xlabel('Country', fontsize=14)
plt.ylabel('Average IQ', fontsize=14)

plt.xticks(rotation=90,  fontsize=10)
plt.yticks(fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.8)

plt.bar_label(bars, fmt="%.2f", fontsize=10,color='black')

plt.tight_layout()
plt.show()
