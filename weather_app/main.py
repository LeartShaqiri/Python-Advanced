import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("weather_tokyo_data.csv")

print(df.info())

# Show first rows
print("\nFirst 5 rows:")
print(df.head())




# -----------------------------
# Convert date column to datetime
# -----------------------------
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Remove invalid dates
df.dropna(subset=["date"], inplace=True)










# -----------------------------
# Basic Null Check
# -----------------------------
null_count = df.isnull().sum()
print("\nNull values per column:")
print(null_count)

# Drop null rows
df.dropna(inplace=True)
print("\nAfter dropping null rows:")
print(df.info())






overall_avg = df["temperature"].mean()
print(f"\nOverall average temperature: {overall_avg:.2f}")







df["month"] = df["date"].dt.month
df["month_name"] = df["date"].dt.month_name()

monthly_avg = df.groupby("month_name")["temperature"].mean().sort_values()
print("\nMonthly Average Temperatures:")
print(monthly_avg)

# Plot monthly average
monthly_avg.plot(kind="bar", title="Monthly Average Temperature - Tokyo")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.tight_layout()
plt.show()





hottest_row = df.loc[df["temperature"].idxmax()]
coldest_row = df.loc[df["temperature"].idxmin()]

print("\nHottest Day (full row):")
print(hottest_row)

print("\nColdest Day (full row):")
print(coldest_row)




df.plot(x="date", y="temperature", figsize=(10,5), title="Tokyo Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.tight_layout()
plt.show()





def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Fall"

df["season"] = df["month"].apply(get_season)

seasonal_avg = df.groupby("season")["temperature"].mean()
print("\nSeasonal Average Temperatures:")
print(seasonal_avg)

# Plot seasonal averages
seasonal_avg.plot(kind="line", marker="o", title="Tokyo Seasonal Average Temperature")
plt.xlabel("Season")
plt.ylabel("Average Temperature")
plt.tight_layout()
plt.show()
