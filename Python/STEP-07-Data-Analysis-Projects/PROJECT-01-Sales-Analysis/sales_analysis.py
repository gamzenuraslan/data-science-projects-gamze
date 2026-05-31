import pandas as pd
from matplotlib import pyplot as plt

#read the dataset
df = pd.read_csv('sales_data.csv')

#first look at the dataset
print(df.head())

print("-----")

#dataset information
print(df.info())
"""info() bize neleri gösterir?
   Satır sayısı?
   Sütun sayısı?
   Veri tipleri?
   Eksik veriler? ---> hepsini"""

print("-----")

#statistical summary(özet)
print(df.describe())

print("-----")

#create profit column
df["Profit"] = df["Sales"] - df["Expenses"]
print(df.head())

print("-----")

#total sales
print(df["Sales"].sum())

print("-----")

#total profit
print(df["Profit"].sum())

print("-----")

max_sales = df["Sales"].max()
best_month = df[df["Sales"] == max_sales]
print(best_month)
print(best_month["Month"].iloc[0])

print("-----")

min_sales = df["Sales"].min()
worst_month = df[df["Sales"] == min_sales]
print(worst_month["Month"].iloc[0])


print("-----")

average_sales = df["Sales"].mean()
print(f"avg_mean_sales: {average_sales}")

print("-----")

average_profit = df["Profit"].mean()
print(f"avg_profit: {average_profit}")

print("-----")

#Months with above average sales
above_average_sales = df[df["Sales"] > average_sales]
print(f"above_average_sales : {above_average_sales}")

print("-----")

plt.plot(df["Month"], df["Sales"], marker = "o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()