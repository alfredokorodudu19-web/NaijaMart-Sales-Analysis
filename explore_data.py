from itertools import groupby

import pandas as pd  # pyright: ignore[reportMissingModuleSource]

df = pd.read_csv("data/naijamart_raw_sales.csv")

print(df.head())

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFirst 10 Rows:")
print(df.head(10))

print("\nLast 10 Rows:")
print(df.tail(10))

print("\nUnique Cities:")
print(df["City"].unique())

print("\nUnique Payment Methods:")
print(df["Payment_Method"].unique())

print("\nUnique Products:")
print(df["Product"].unique())

print("\nQuantity Statistics:")
print(df["Quantity"].describe())

print("\nMinimum Quantity:")
print(df["Quantity"].min())

print("\nMaximum Quantity:")
print(df["Quantity"].max())

print("\nMinimum Price:")
print(df["Price"].min())

print("\nMaximum Price:")
print(df["Price"].max())

print("\nNegative Quantities:")
print(df[df["Quantity"] < 0])

print("\nPrice data type:")
print(df["Price"].dtype)

print("\nSample prices:")
print(df["Price"].head(10).tolist())

Naira_prices = df[df["Price"].str.contains("₦", na=False)]
print("\nNaira Prices:")
print(Naira_prices["Price"].tolist())

Comma_prices = df[df["Price"].str.contains(",", na=False)]
print("\nComma Prices:")
print(Comma_prices["Price"].tolist())

print("Naira prices:", len(Naira_prices))
print("Comma prices:", len(Comma_prices))

cleaned_prices = df["Price"].str.replace("₦", "").str.replace(",", "").astype(float)
print("\nCleaned Prices:")
print(cleaned_prices.head(10).tolist())

print("\ncleaned_prices data type:")
print(cleaned_prices.dtype)

print("\ncleaned price statistics:")
print(cleaned_prices.describe())

print("]\nOriginal price statistics:")
print(df["Price"].dtype) 

print("\nLowest price:")
print(cleaned_prices.min())

print("\nHighest price:")
print(cleaned_prices.max())

df["Price"]= (
    df["Price"].str.replace("₦", "").str.replace(",", "").astype(float)
)

print("\nPrice datatype after cleaning:")
print(df["Price"].dtype)

print("\nPrice statistics after cleaning:")
print(df["Price"].describe())

print("\nCities before cleaning:")
print(df["City"].value_counts(dropna=False))

df["City"] = df["City"].str.strip().str.title()

print("\nCities after cleaning:")
print(df["City"].value_counts(dropna=False))

print("\nUnknown Cities:")
print(df[df["City"].isnull() | (df["City"] == "")])

print("\nUnknown Products:")
print(df[df["Product"].isnull() | (df["Product"] == "")])

df["Customer"] = df["Customer"].str.strip().str.title()
df = df[df["Customer"].isin(["Tunde Bello","aisha musa","Emeka Obi","David Ade","John Doe","Alfred Okoro","Chioma Eze","Mary Johnson","Sarah Williams"])][["Customer","Email","City"]]

print("\nCleaned Customer Data:")
print(df.head(10))

#df[df["Order_ID"] == "ORD0433"]

print(df.shape)

df[df["Customer"] == "Tunde Bello"]

missing_customers = df.loc[df["City"].isna(), "Customer"].unique()

df[df["Customer"].isin(missing_customers)].sort_values("Customer")

print("\nMissing Customers:")
print(missing_customers)

df[df["Customer"].isin(missing_customers)].sort_values(["Customer", "City"])

print("\nMissing Customers with City:")
print(df[df["Customer"].isin(missing_customers)].sort_values(["Customer", "City"]))

df["City"] = df["City"].fillna("Unknown")

print("\nCities after filling missing values:")
print(df["City"].value_counts(dropna=False))

print(df["City"].isna().sum())

print(df["City"].unique())

print(df.info())

print(df[df["Email"].isna()])

missing_emails = df.loc[df["Email"].isna(), "Customer"].unique()
print(df[df["Customer"].isin(missing_emails)][["Customer", "Email", "City"]].sort_values("Customer"))

print(df.groupby("Customer")["Email"].nunique().sort_values(ascending=False))

df.loc[(df["Customer"] == "Mary Johnson") & (df["Email"].isna()), "Email"] = "mary.johnson@example.com"
df.loc[(df["Customer"] == "Sarah Williams") & (df["Email"].isna()), "Email"] = "sarah.williams@example.com"
df.loc[(df["Customer"] == "Tunde Bello") & (df["Email"].isna()), "Email"] = "tunde.bello@example.com"

print("\nEmails after filling missing values:")
print(df[df["Email"].isna()])

print(df[(df["Customer"] == "Alfred Okoro") & (df["Email"])])

customers_with_multiple_emails = (
    df.groupby("Customer")["Email"]
      .nunique()
      .loc[lambda x: x > 1]
      .index
)

print(df[df["Customer"].isin(customers_with_multiple_emails)][
    ["Customer", "Email", "City"]]
.sort_values(["Customer", "Email"]))

print(df[df["Customer"].isin(customers_with_multiple_emails)][
    ["Customer", "Email"]
].drop_duplicates().sort_values(["Customer", "Email"]))

print(df["Email"].value_counts(dropna=False))

df["Email"] = df["Email"].replace("invalid@email", pd.NA)

print(df["Email"].value_counts(dropna=False))

print(df[df["Email"].isna()][["Customer", "Email","City"]])

email_mapping = (df.dropna(subset=["Email"]).drop_duplicates("Customer").set_index("Customer")["Email"])

df["Email"] = df["Email"].fillna(df["Customer"].map(email_mapping))

print(df[df["Email"].isna()][["Customer", "Email","City"]])

print(df["Email"].value_counts(dropna=False))

print(df["Email"].isna().sum())

print(df["Email"].str.contains("@").value_counts(dropna=False))

print(df["Email"].str.contains(r"\.").value_counts(dropna=False))

print(df["Email"].str.split("@").str[0].str.len().value_counts())

print(df.groupby("Customer")["Email"].nunique().sort_values(ascending=False))

print("\nUnknown Customers:")
print(df[df["Customer"].isnull() | (df["Customer"] == "")])

print("\nColumns:")
print(df.columns.tolist())

print(df["Customer"].value_counts(dropna=False))

print(df["Customer"].isna().sum())

print((df["Customer"] != df["Customer"].str.strip()).sum())

print(df.columns)


#New line of code for cleaning the other columns

raw_df = pd.read_csv("data/naijamart_raw_sales.csv")

print("\nOriginal Dataframe columns:")
print(raw_df.columns.tolist())

print("\nOriginal Dataframe shape:")
print(raw_df.shape)

print("\nMissing Order_IDs:")
print(raw_df["Order_ID"].isna().sum())

print("\nDuplicate Order_IDs:")
print(raw_df["Order_ID"].duplicated().sum())

print("\nDistinct Order_IDs:")
print(raw_df["Order_ID"].nunique())

duplicate_order_ids = raw_df.loc[raw_df["Order_ID"].duplicated(keep=False), "Order_ID"].unique()

print("\nDuplicate Order_IDs:")
print(duplicate_order_ids)

print(raw_df[raw_df["Order_ID"].isin(duplicate_order_ids)].sort_values("Order_ID"))

print(raw_df["Order_ID"].duplicated().sum())

cleaned_df = raw_df.drop_duplicates().copy()

print(raw_df["Order_ID"].duplicated().sum())

print(cleaned_df["Order_ID"].duplicated().sum())

print("Cleaned Dataframe shape:", cleaned_df.shape)
print("Original Dataframe shape:", raw_df.shape)

print("Cleaned Dataframe duplicated rows:", cleaned_df["Order_ID"].duplicated().sum())

print("Cleaned Dataframe total duplicates:", cleaned_df.duplicated().sum())

print(cleaned_df["Product"].str.strip().value_counts(dropna=False))

print(cleaned_df["Product"].unique().tolist())

print(cleaned_df[cleaned_df["Product"].isna()])

cleaned_df["Product"] = cleaned_df["Product"].fillna("Unknown").str.strip()

print(cleaned_df["Product"].value_counts(dropna=False))

print(cleaned_df["Quantity"].describe())

print(cleaned_df["Quantity"].isna().sum())

print(cleaned_df[cleaned_df["Quantity"] < 0])


print(cleaned_df["Quantity"].value_counts(dropna=False).sort_index())

print(cleaned_df[cleaned_df["Quantity"] < 0].shape)

print(cleaned_df["Price"].head(10))

print(cleaned_df["Price"].dtype)

print(cleaned_df["Price"].str.contains("₦|,").value_counts(dropna=False))

cleaned_df["Price"] = cleaned_df["Price"].str.replace("₦", "").str.replace(",", "").astype(float)

print(cleaned_df["Price"].head(10))

print(cleaned_df["Price"].dtype)

print(cleaned_df["Price"].describe())

print(cleaned_df["Price"].isna().sum())

print(cleaned_df.columns.tolist())

print(cleaned_df["Date"].isna().sum())

print(cleaned_df["Date"].dtype)

print(cleaned_df["Date"].unique()[:20])

print(cleaned_df[cleaned_df["Date"] == "invalid-date"])

print(cleaned_df["Date"].value_counts().loc[lambda x: x.index == "invalid-date"])

cleaned_df["Date"] = pd.to_datetime(cleaned_df["Date"], errors="coerce")

print(cleaned_df["Date"].isna().sum())

print(cleaned_df["Date"].dtype)

print(cleaned_df["City"].unique())

print(cleaned_df["City"].value_counts(dropna=False))

cleaned_df["City"] = cleaned_df["City"].str.strip().str.title()

print(cleaned_df["City"].value_counts(dropna=False))

print(cleaned_df[cleaned_df["City"].isna()])

cleaned_df["City"] = cleaned_df["City"].fillna("Unknown")

print(cleaned_df["City"].value_counts(dropna=False))

print(cleaned_df["City"].unique().tolist())

print(cleaned_df["City"].isna().sum())

print(cleaned_df["Payment_Method"].value_counts(dropna=False))

print(cleaned_df[cleaned_df["Payment_Method"].isna()])

print(cleaned_df["Payment_Method"].unique().tolist())

cleaned_df["Payment_Method"]= cleaned_df["Payment_Method"].fillna("unknown")

print(cleaned_df["Payment_Method"].value_counts(dropna=False))

print(cleaned_df["Payment_Method"].isna().sum())

print(cleaned_df["Payment_Method"].unique())

cleaned_df["Payment_Method"] = cleaned_df["Payment_Method"].replace("unknown","Unknown")

print(cleaned_df["Payment_Method"].value_counts(dropna=False))

print(cleaned_df["Payment_Method"].isna().sum())

print(cleaned_df["Payment_Method"].unique())

print(cleaned_df["Customer"].value_counts(dropna=False))

print(cleaned_df["Customer"].unique())

print(cleaned_df[cleaned_df["Customer"].isna() | (cleaned_df["Customer"] == "")])

cleaned_df["Customer"] = cleaned_df["Customer"].str.strip().str.title()

print(cleaned_df["Customer"].value_counts(dropna=False))

print(cleaned_df["Customer"].unique())

print(cleaned_df.dropna(subset=["Customer","Email"]).groupby("Email") ["Customer"].nunique())

customers_mapping= (
    cleaned_df[
        cleaned_df["Email"].notna()
        & (cleaned_df["Email"] != "invalid@email")
        & cleaned_df["Customer"].notna()
    ]
    .drop_duplicates(subset=["Email"])
    .set_index("Email")["Customer"]
    .to_dict()
)

print(customers_mapping)

cleaned_df["Customer"] = cleaned_df["Customer"].fillna(cleaned_df["Email"].map(customers_mapping))

print(cleaned_df["Customer"].isna().sum())

print(cleaned_df["Customer"].value_counts(dropna=False))

print(cleaned_df[cleaned_df["Customer"].isna()][["Order_ID","Customer","Email"]])

cleaned_df["Customer"]=cleaned_df["Customer"].fillna("Unknown")

print(cleaned_df["Customer"].isna().sum())

print(cleaned_df["Customer"].value_counts())

print(cleaned_df["Email"].isna().sum())

print(cleaned_df["Email"].value_counts(dropna=False))

print(cleaned_df["Email"].unique())

print(cleaned_df[cleaned_df["Email"].isna()][["Order_ID","Customer","Email"]])

print(cleaned_df[cleaned_df["Email"] == "invalid@email"][["Order_ID","Customer","Email"]])


print(
    cleaned_df[
        (cleaned_df["Email"].notna()) &
        (cleaned_df["Email"] != "invalid@email")
    ]
    .groupby("Customer")["Email"]
    .nunique()
)

email_mapping= (
    cleaned_df[(cleaned_df["Email"].notna())
               & (cleaned_df["Email"] != "invalid@email")
               & (cleaned_df["Customer"] != "Unknown")
               & (cleaned_df["Customer"].notna())]
            .drop_duplicates(subset=["Customer"])
            .set_index("Customer")["Email"]
            .to_dict()   
)  

print(email_mapping)

cleaned_df["Email"]= cleaned_df["Email"].replace("invalid@email", pd.NA)

cleaned_df["Email"]= cleaned_df["Email"].fillna(cleaned_df["Customer"].map(email_mapping))

print(cleaned_df["Email"].isna().sum())

print(cleaned_df["Email"].value_counts(dropna=False))

print(cleaned_df["Email"].unique())

print(
    cleaned_df[
        cleaned_df["Email"].isna()
    ][["Order_ID", "Customer", "Email"]]
)

print("Missing emails:", cleaned_df["Email"].isna().sum())
print("Invalid emails:", (cleaned_df["Email"] == "invalid@email").sum())
print("Unique emails:", cleaned_df["Email"].nunique())


print(
    cleaned_df[cleaned_df["Quantity"] < 0][
        ["Order_ID", "Customer", "Product",
         "Quantity", "Price", "Date"]
    ]
)

cleaned_df["Quantity_flag"] = (cleaned_df["Quantity"] < 0)

print(cleaned_df["Quantity_flag"].value_counts())

print(cleaned_df.groupby("Quantity_flag")["Quantity"].agg(["count","min","max"]))

print("Dataset shape:", cleaned_df.shape)

print("\nMissing values:")
print(cleaned_df.isna().sum())

print("\nDuplicate Order IDs:")
print(cleaned_df["Order_ID"].duplicated().sum())

print("\nDuplicate rows:")
print(cleaned_df.duplicated().sum())

print("\nColumn data types:")
print(cleaned_df.dtypes)

cleaned_df["Date_flag"] = cleaned_df["Date"].isna()

print(cleaned_df["Date_flag"].value_counts())

print(
    cleaned_df[
        cleaned_df["Email"].isna()
        |cleaned_df["Date"].isna()
        |cleaned_df["Date_flag"]
    ][
        ["Order_ID","Customer","Date","Quantity","Email","Quantity_flag"]
    ]
)


print("Negative quantities:",
      (cleaned_df["Quantity"] < 0).sum())

print("Flagged quantities:",
      cleaned_df["Quantity_flag"].sum())

print(
    cleaned_df.loc[
        cleaned_df["Quantity"] < 0,
        ["Order_ID", "Quantity", "Quantity_flag"]
    ]
)

print(cleaned_df["Date_flag"].value_counts())

cleaned_df=cleaned_df.drop(columns=["Date_flag"])

print(cleaned_df.columns)

print(cleaned_df.describe(include="all"))

#Aggregations

cleaned_df["Revenue"] = (cleaned_df["Price"] * cleaned_df["Quantity"])

print(cleaned_df[["Order_ID", "Customer", "Price", "Quantity", "Revenue", "Quantity_flag"]].head(15))

print(cleaned_df["Revenue"].describe())

print(cleaned_df.loc[cleaned_df["Quantity_flag"], ["Order_ID", "Customer", "Price", "Quantity", "Revenue"]])

print("\nTotal Revenue:",cleaned_df["Revenue"].sum())

print("\nRevenue from flagged transactions:", cleaned_df.loc[cleaned_df["Quantity_flag"],"Revenue"].sum())

print("\nRevenue from normal transactions:", cleaned_df.loc[~cleaned_df["Quantity_flag"],"Revenue"].sum())

cleaned_df["Transaction_value"] = cleaned_df["Quantity"].abs() * cleaned_df["Price"]

print(cleaned_df[["Order_ID", "Customer", "Price", "Quantity", "Revenue", "Transaction_value"]].head(15))

print(cleaned_df[cleaned_df["Quantity_flag"] == True][["Order_ID", "Price", "Quantity", "Revenue", "Transaction_value"]].head(15))

print((cleaned_df["Transaction_value"] == cleaned_df["Price"] * cleaned_df["Quantity"].abs()).all())


cleaned_df= cleaned_df.rename(columns={"Transaction_value": "Transaction_Value"})

print(cleaned_df.columns)

cleaned_df["Year"] = cleaned_df["Date"].dt.year
cleaned_df["Year"].describe()

print(cleaned_df[["Order_ID", "Year","Date"]].head(15))

print("\nMissing Dates:", cleaned_df["Date"].isna().sum())
print("\nMissing years:", cleaned_df["Year"].isna().sum())

cleaned_df["Month"] = cleaned_df["Date"].dt.month
cleaned_df["Month"].describe()

print(cleaned_df[["Order_ID", "Month","Year","Date"]].head(15))

print("\nMissing Dates:", cleaned_df["Date"].isna().sum())
print("\nMissing months:", cleaned_df["Month"].isna().sum())

print(cleaned_df.groupby("Month")["Revenue"].sum().sort_index())

cleaned_df["Month_name"] = cleaned_df["Date"].dt.month_name()

print(cleaned_df[["Order_ID","Month","Month_name","Year","Date"]].head(15))

print("\nMissing Month Names:", cleaned_df["Month_name"].isna().sum())

cleaned_df["Day_Name"] = cleaned_df["Date"].dt.day_name()

print(cleaned_df[["Order_ID","Day_Name","Month_name","Year","Date"]].head(15))

print("\nMissing Day Names:", cleaned_df["Day_Name"].isna().sum())

print(cleaned_df["Day_Name"].value_counts(dropna=False))

cleaned_df=cleaned_df.rename(columns={"Month_name": "Month_Name"})

cleaned_df["Quarter"] = cleaned_df["Date"].dt.quarter

print(cleaned_df[["Order_ID","Quarter","Month_Name","Year","Date"]].head(15))

print("\nMissing Quarters:", cleaned_df["Quarter"].isna().sum())\

print(cleaned_df["Quarter"].value_counts(dropna=False))

print(cleaned_df[["Order_ID","Quarter","Month_Name","Year","Date"]].tail(15))

cleaned_df = cleaned_df.reset_index(drop=True)

print(cleaned_df.shape)
print(cleaned_df.index)

cleaned_df.info()

print(cleaned_df.isna().sum())

print(cleaned_df["Order_ID"].duplicated().sum())

print(cleaned_df.duplicated().sum())

print(cleaned_df["Order_ID"].nunique())

print(cleaned_df["Order_ID"].value_counts().sum())

print(cleaned_df["Order_ID"].count())

print(cleaned_df["Quantity"].describe())

print(
    (
        (cleaned_df["Quantity"] < 0)
        == cleaned_df["Quantity_flag"]
    ).all()
)

print(
    (cleaned_df["Quantity"] < 0).equals(
        cleaned_df["Quantity_flag"]
    )
)

print((cleaned_df["Revenue"]).equals(cleaned_df["Price"] * cleaned_df["Quantity"]))

print((cleaned_df["Transaction_Value"]).equals(cleaned_df["Price"] * cleaned_df["Quantity"].abs()))

print(cleaned_df["Quantity"].min())
print(cleaned_df["Quantity"].max())
print(cleaned_df["Quantity"].isna().sum())

print(cleaned_df["Price"].min())
print(cleaned_df["Price"].max())
print(cleaned_df["Price"].isna().sum())

print("Negative Revenue:", (cleaned_df["Revenue"] < 0).sum())
print("Zero Revenue:", (cleaned_df["Revenue"] == 0).sum())
print("Missing Revenue:", cleaned_df["Revenue"].isna().sum())

print("Earliest date:", cleaned_df["Date"].min())
print("Latest date:", cleaned_df["Date"].max())
print("Missing dates:", cleaned_df["Date"].isna().sum())

print(cleaned_df.shape)
print(cleaned_df.columns.tolist())

print(cleaned_df.groupby("Product")["Order_ID"].count())

print(cleaned_df["Product"].value_counts(dropna=False))

print(cleaned_df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

print(cleaned_df.groupby("Product")["Revenue"].mean().sort_values(ascending=False))

average_revenue = (
    cleaned_df.groupby("Product")["Revenue"]
    .mean()
    .sort_values(ascending=False)
)

print(average_revenue.round(2))

product_analysis = (cleaned_df.groupby("Product").agg(
    Total_Orders=("Order_ID", "count"),
    Total_Revenue=("Revenue", "sum"),
    Average_Revenue=("Revenue", "mean")
))

print(product_analysis.sort_values(by="Total_Revenue", ascending=False).round(2))

city_analysis = (cleaned_df.groupby("City").agg(
    Total_Orders=("Order_ID", "count"),
    Total_Revenue=("Revenue", "sum"),
    Average_Revenue=("Revenue", "mean")
))

print(city_analysis.sort_values(by="Total_Orders", ascending=False).round(2)) 

month_analysis = (cleaned_df.groupby("Month_Name").agg(
    Total_Orders=("Order_ID", "count"),
    Total_Revenue=("Revenue", "sum"),
    Average_Revenue=("Revenue", "mean")
))

print(month_analysis.sort_values(by="Total_Revenue", ascending=False).round(2)) 

quarter_analysis = (cleaned_df.groupby("Quarter").agg(
    Total_Orders=("Order_ID", "count"),
    Total_Revenue=("Revenue", "sum"),
    Average_Revenue=("Revenue", "mean")
))

print(quarter_analysis.sort_values(by="Total_Revenue", ascending=False).round(2))   

monthly_revenue_diff = (
    cleaned_df.dropna(subset=["Date"])
    .groupby("Month")["Revenue"]
    .sum()
    .sort_index()
)

print(monthly_revenue_diff.diff().round(2))

monthly_revenue_pct_change = monthly_revenue_diff.pct_change().round(4) * 100

print(monthly_revenue_pct_change)

payment_analysis = (cleaned_df.groupby("Payment_Method").agg(
    Total_Orders=("Order_ID", "count"),
    Total_Revenue=("Revenue", "sum"),
    Average_Revenue=("Revenue", "mean")
))  

print(payment_analysis.sort_values(by="Total_Revenue", ascending=False).round(2))

customer_analysis = (cleaned_df.groupby("Customer").agg(
    Total_Orders=("Order_ID", "count"),
    Total_Revenue=("Revenue", "sum"),
    Average_Revenue=("Revenue", "mean")
))      

print(customer_analysis.sort_values(by="Total_Revenue", ascending=False).round(2).head(10))

customer_revenue_contribution = (cleaned_df.groupby("Customer")["Revenue"].sum()/cleaned_df["Revenue"].sum() * 100).sort_values(ascending=False)

print(customer_revenue_contribution.round(2))

order_counts=cleaned_df.groupby("Customer")["Order_ID"].count().sort_values(ascending=False)

repeat_customers = order_counts[order_counts > 150].sort_values(ascending=False)

print("\nRepeat Customers (more than 150 orders):")
print(repeat_customers)

order_counts=cleaned_df.groupby("Customer")["Order_ID"].count().sort_values(ascending=False).drop("Unknown", errors='ignore')

High_frequency_customers = order_counts[order_counts > 170].sort_values(ascending=False)
Medium_frequency_customers = order_counts[(order_counts > 150) & (order_counts <= 170)].sort_values(ascending=False)
Low_frequency_customers = order_counts[order_counts < 150].sort_values(ascending=False)

print("\nHigh-Frequency Customers (more than 170 orders):")
print(High_frequency_customers)
print("\nMedium-Frequency Customers (150-170 orders):")
print(Medium_frequency_customers)
print("\nLow-Frequency Customers (less than 150 orders):")
print(Low_frequency_customers)


customer_revenue = customer_analysis["Total_Revenue"].sort_values(
    ascending=False
)

cumulative_revenue = customer_revenue.cumsum()

print(cumulative_revenue)

print(cumulative_revenue.head(3) / cleaned_df["Revenue"].sum() * 100)

customer_analysis= cleaned_df.groupby("Customer").agg(
    Total_Orders=("Order_ID", "count"),
    Total_Revenue=("Revenue", "sum"),
    Average_Revenue=("Revenue", "mean")
)

print("\n Top 5 Customers:",customer_analysis.sort_values(by="Total_Revenue", ascending=False).round(2).head(5))

cleaned_df.to_csv("data/naijamart_cleaned_sales.csv", index=False)

import os

print(os.getcwd())

output_path = os.path.join(
    os.getcwd(),
    "naijamart_cleaned_sales.csv"
)

cleaned_df.to_csv(output_path, index=False)

print("Saved to:", output_path)
print("File exists:", os.path.exists(output_path))

verification_df = pd.read_csv(output_path)

print("Original shape:", cleaned_df.shape)
print("Saved shape:", verification_df.shape)
print(verification_df.head())

verification_df = pd.read_csv(
    output_path,
    parse_dates=["Date"]
)

verification_df["Year"] = verification_df["Year"].astype("Int64")
verification_df["Month"] = verification_df["Month"].astype("Int64")
verification_df["Quarter"] = verification_df["Quarter"].astype("Int64")


# =====================================
# FINAL DATA QUALITY VALIDATION
# =====================================

print("\n===== FINAL DATA QUALITY REPORT =====")

# 1. Dataset dimensions
print("\n1. Dataset Shape:")
print(cleaned_df.shape)

# 2. Duplicate Order IDs
print("\n2. Duplicate Order IDs:")
print(cleaned_df["Order_ID"].duplicated().sum())

# 3. Missing values
print("\n3. Missing Values by Column:")
print(cleaned_df.isna().sum()[cleaned_df.isna().sum() > 0])

# 4. Data types
print("\n4. Data Types:")
print(cleaned_df.dtypes)

# 5. Negative quantities
print("\n5. Negative Quantity Records:")
print((cleaned_df["Quantity"] < 0).sum())

# 6. Invalid/missing dates
print("\n6. Missing Dates:")
print(cleaned_df["Date"].isna().sum())

# 7. Revenue consistency
expected_revenue = cleaned_df["Quantity"] * cleaned_df["Price"]

revenue_mismatches = (
    cleaned_df["Revenue"] - expected_revenue
).abs().gt(0.01).sum()

print("\n7. Revenue Calculation Mismatches:")
print(revenue_mismatches)

print("\n===== VALIDATION COMPLETE =====")


