# Online Shopping Peak Hour Analysis
# Minor Project – EDA

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create fake order data
np.random.seed(42)

orders = 1000

timestamps = pd.date_range(
    start="2023-01-01",
    periods=orders,
    freq="min"
)

df = pd.DataFrame({
    "order_id": range(1, orders + 1),
    "timestamp": timestamps + pd.to_timedelta(
        np.random.randint(0, 1440, orders), unit="m"
    ),
    "amount": np.random.randint(200, 5000, orders)
})

# Extract hour
df["hour"] = df["timestamp"].dt.hour

# Descriptive statistics
print("\nOrder Amount Statistics:\n")
print(df["amount"].describe())

# Peak hour analysis
hourly_orders = df.groupby("hour").size()

print("\nOrders per Hour:\n")
print(hourly_orders)

# Plot
plt.figure()
hourly_orders.plot(kind="line", marker="o")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Orders")
plt.title("Online Shopping Peak Hour Analysis")
plt.grid(True)
plt.show()