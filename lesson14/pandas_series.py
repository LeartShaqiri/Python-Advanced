import pandas as pd

products = ['Laptop', 'Tablet', 'Smartphone', 'Desktop']

sales = [1500, 1200, 3000, 800]

sales_series = pd.Series(sales, index=products)
print(sales_series)

print(sales_series['Smartphone'])

total_sales = sales_series.sum()
print(total_sales)

best_selling_product = sales_series.idxmax()
print(f"*best_selling_product: {best_selling_product}*")