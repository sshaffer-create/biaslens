# CUSTOMER LIFETIME VALUE (CLV) ANALYSIS
# Using Sample Data


import pandas as pd  # Import pandas for data manipulation (tables, grouping, calculations)
import numpy as np  # Import numpy for numerical operations and random number generation


# STEP 1: CREATE SAMPLE DATA


np.random.seed(42)  # Set random seed so results are reproducible (same output every run)

n_customers = 20  # Define number of customers in our dataset
customer_ids = np.arange(1001, 1001 + n_customers) # Create customer IDs: 1001, 1002, ..., 1020

rows = []  # Create an empty list to store transaction records

for cid in customer_ids:  # Loop through each customer ID

    n_purchases = np.random.randint(1, 8) # Randomly assign each customer between 1 and 7 purchases

    for _ in range(n_purchases):  # Loop for the number of purchases that customer made

        random_days = np.random.randint(1, 365) # Pick a random number of days ago (within last year)

        purchase_date = pd.Timestamp("2026-03-11") - pd.Timedelta(days=random_days) # Subtract random days from a fixed date to create a purchase date

        revenue = round(np.random.uniform(20, 200), 2) # Generate random spending between $20 and $200, rounded to 2 decimals

        rows.append([cid, purchase_date, revenue])  # Add transaction record to list: [CustomerID, Date, Revenue]

df = pd.DataFrame(rows, columns=["CustomerID", "InvoiceDate", "Revenue"]) # Convert list of rows into a pandas DataFrame (table)

df.to_csv("Sample_Data.csv", index=False)

print("Sample Data:")
print(df.head())  # Display first 5 rows to preview dataset


# STEP 2: CALCULATE AVERAGE PURCHASE VALUE


avg_purchase = df.groupby("CustomerID")["Revenue"].mean() # Group transactions by CustomerID and calculate average revenue per customer

avg_purchase.name = "AvgPurchaseValue" # Rename the column for clarity



# STEP 3: CALCULATE PURCHASE FREQUENCY


purchase_freq = df.groupby("CustomerID")["InvoiceDate"].count() # Count number of transactions (purchase frequency) per customer

purchase_freq.name = "PurchaseFrequency" # Rename column for clarity



# STEP 4: CALCULATE CUSTOMER LIFESPAN


lifespan = df.groupby("CustomerID")["InvoiceDate"].agg(["min", "max"]) # For each customer, find first purchase date (min) and last purchase date (max)

lifespan["LifespanDays"] = (lifespan["max"] - lifespan["min"]).dt.days # Subtract dates to calculate number of days between first and last purchase



# STEP 5: COMBINE EVERYTHING


clv = pd.concat([avg_purchase, purchase_freq, lifespan["LifespanDays"]], axis=1) # Combine all calculated metrics into one table (aligned by CustomerID)

clv["CLV"] = (clv["AvgPurchaseValue"] * clv["PurchaseFrequency"] * (clv["LifespanDays"] / 365)) # Apply basic CLV formula:
# CLV = (Average Purchase Value × Purchase Frequency) * (LifespanDays/365)



# STEP 6: SEGMENT CUSTOMERS

clv["Segment"] = pd.qcut(clv["CLV"], q=3, labels=["Low", "Medium", "High"]) # Divide customers into 3 equal-sized groups based on CLV value



# STEP 7: SORT RESULTS


clv_sorted = clv.sort_values("CLV", ascending=False) # Sort customers from highest CLV to lowest


print("Customer Lifetime Value Results:")
print(clv_sorted)  # Display final CLV table


# STEP 8: SAVE RESULTS


clv_sorted.to_csv("CLV_Results.csv") # Export results to CSV file
print("File saved as CLV_Results.csv")
