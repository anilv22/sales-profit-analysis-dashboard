import pandas as pd

input_file = "Sales_Business_Performance_Analytics.xlsx"

df = pd.read_excel(
    input_file,
    sheet_name="Sales_Data"
)

print("Raw data loaded successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Customer_Name"] = df["Customer_Name"].fillna("Unknown Customer")
df["City"] = df["City"].fillna("Unknown")
print("Missing City handled")
print("Remaining missing City:", df["City"].isna().sum())
print("Missing Customer_Name handled")
print("Remaining missing Customer_Name:", df["Customer_Name"].isna().sum())

print("Order_Date converted to datetime")
print(df["Order_Date"].dtype)

output_file = "Sales_Business_Performance_Analytics_Cleaned.xlsx"

df.to_excel(
    output_file,
    sheet_name="Sales_Data",
    index=False
)

print("Cleaned data saved successfully")
print("Output file:", output_file)
print("Rows:", len(df))
print("Columns:", len(df.columns))