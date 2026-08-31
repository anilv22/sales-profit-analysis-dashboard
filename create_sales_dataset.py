import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

# -----------------------------
# MASTER DATA
# -----------------------------

first_names = [
    "Amit", "Rahul", "Anil", "Rohit", "Vikas",
    "Sanjay", "Manish", "Deepak", "Arjun", "Varun",
    "Priya", "Neha", "Pooja", "Anjali", "Kavita",
    "Sneha", "Ritu", "Nisha", "Shweta", "Meena"
]

last_names = [
    "Sharma", "Verma", "Singh", "Gupta", "Kumar",
    "Mishra", "Yadav", "Agarwal", "Jain", "Patel"
]

locations = {
    "North": {
        "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Noida", "Prayagraj"],
        "Delhi": ["New Delhi", "Delhi"],
        "Punjab": ["Ludhiana", "Amritsar", "Jalandhar"],
        "Haryana": ["Gurugram", "Faridabad", "Panipat"],
        "Rajasthan": ["Jaipur", "Jodhpur", "Kota"]
    },

    "South": {
        "Karnataka": ["Bengaluru", "Mysuru", "Mangaluru"],
        "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
        "Telangana": ["Hyderabad", "Warangal"],
        "Kerala": ["Kochi", "Thiruvananthapuram"],
        "Andhra Pradesh": ["Vijayawada", "Visakhapatnam"]
    },

    "West": {
        "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik"],
        "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
        "Goa": ["Panaji", "Margao"],
        "Madhya Pradesh": ["Bhopal", "Indore"]
    },

    "East": {
        "West Bengal": ["Kolkata", "Siliguri"],
        "Bihar": ["Patna", "Gaya"],
        "Odisha": ["Bhubaneswar", "Cuttack"],
        "Jharkhand": ["Ranchi", "Jamshedpur"]
    }
}

products = {
    "Electronics": {
        "Laptops": ["HP Laptop", "Dell Laptop", "Lenovo Laptop", "ASUS Laptop"],
        "Smartphones": ["Samsung Galaxy", "OnePlus Phone", "iPhone", "Redmi Phone"],
        "Monitors": ["Dell Monitor", "LG Monitor", "Samsung Monitor"],
        "Accessories": ["Keyboard", "Mouse", "Headphones"]
    },

    "Furniture": {
        "Office Furniture": ["Office Chair", "Office Desk", "Bookshelf"],
        "Storage": ["Filing Cabinet", "Storage Cabinet"],
        "Lighting": ["Table Lamp", "LED Desk Lamp"]
    },

    "Office Supplies": {
        "Stationery": ["Notebook", "Pen Set", "Stapler"],
        "Paper": ["Printer Paper", "Copy Paper"],
        "Equipment": ["Calculator", "Paper Shredder"]
    },

    "Home Appliances": {
        "Kitchen": ["Mixer Grinder", "Microwave", "Electric Kettle"],
        "Cleaning": ["Vacuum Cleaner"],
        "Cooling": ["Air Cooler"]
    }
}

payment_modes = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

order_statuses = [
    "Delivered",
    "Delivered",
    "Delivered",
    "Delivered",
    "Shipped",
    "Cancelled",
    "Returned"
]

# -----------------------------
# PRICE RANGE
# -----------------------------

price_ranges = {
    "HP Laptop": (45000, 75000),
    "Dell Laptop": (50000, 85000),
    "Lenovo Laptop": (40000, 75000),
    "ASUS Laptop": (45000, 80000),

    "Samsung Galaxy": (18000, 65000),
    "OnePlus Phone": (25000, 60000),
    "iPhone": (55000, 120000),
    "Redmi Phone": (10000, 30000),

    "Dell Monitor": (10000, 30000),
    "LG Monitor": (9000, 28000),
    "Samsung Monitor": (10000, 35000),

    "Keyboard": (800, 4000),
    "Mouse": (500, 3000),
    "Headphones": (1000, 8000),

    "Office Chair": (5000, 18000),
    "Office Desk": (8000, 25000),
    "Bookshelf": (4000, 15000),
    "Filing Cabinet": (5000, 16000),
    "Storage Cabinet": (6000, 18000),
    "Table Lamp": (800, 3000),
    "LED Desk Lamp": (1000, 4000),

    "Notebook": (100, 500),
    "Pen Set": (100, 800),
    "Stapler": (150, 700),
    "Printer Paper": (250, 700),
    "Copy Paper": (250, 650),
    "Calculator": (500, 2500),
    "Paper Shredder": (4000, 12000),

    "Mixer Grinder": (2500, 7000),
    "Microwave": (7000, 18000),
    "Electric Kettle": (1000, 3500),
    "Vacuum Cleaner": (5000, 15000),
    "Air Cooler": (6000, 18000)
}

# -----------------------------
# GENERATE 5000 ORDERS
# -----------------------------

data = []

start_date = datetime(2025, 1, 1)

for i in range(5000):

    order_id = f"ORD-{10001 + i}"

    order_date = start_date + timedelta(
        days=random.randint(0, 364)
    )

    customer_id = f"CUST-{random.randint(1001, 1800)}"

    customer_name = (
        random.choice(first_names)
        + " "
        + random.choice(last_names)
    )

    region = random.choice(list(locations.keys()))

    state = random.choice(
        list(locations[region].keys())
    )

    city = random.choice(
        locations[region][state]
    )

    category = random.choice(
        list(products.keys())
    )

    sub_category = random.choice(
        list(products[category].keys())
    )

    product = random.choice(
        products[category][sub_category]
    )

    quantity = random.randint(1, 5)

    min_price, max_price = price_ranges[product]

    unit_price = random.randint(
        min_price,
        max_price
    )

    discount = random.choice([
        0,
        0.05,
        0.10,
        0.15,
        0.20
    ])

    sales = (
        unit_price
        * quantity
        * (1 - discount)
    )

    cost = sales * random.uniform(
        0.60,
        0.85
    )

    payment_mode = random.choice(
        payment_modes
    )

    order_status = random.choice(
        order_statuses
    )

    data.append([
        order_id,
        order_date.strftime("%Y-%m-%d"),
        customer_id,
        customer_name,
        category,
        sub_category,
        product,
        region,
        state,
        city,
        round(sales, 2),
        quantity,
        discount,
        round(cost, 2),
        payment_mode,
        order_status
    ])

# -----------------------------
# CREATE DATAFRAME
# -----------------------------

columns = [
    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Customer_Name",
    "Category",
    "Sub_Category",
    "Product",
    "Region",
    "State",
    "City",
    "Sales",
    "Quantity",
    "Discount",
    "Cost",
    "Payment_Mode",
    "Order_Status"
]

df = pd.DataFrame(
    data,
    columns=columns
)

# -----------------------------
# ADD REALISTIC DATA QUALITY ISSUES
# -----------------------------

missing_rows = random.sample(range(5000), 20)

for row in missing_rows[:7]:
    df.loc[row, "Customer_Name"] = None

for row in missing_rows[7:14]:
    df.loc[row, "City"] = None

for row in missing_rows[14:20]:
    df.loc[row, "Discount"] = None

# -----------------------------
# SAVE EXCEL FILE
# -----------------------------

output_file = "Sales_Business_Performance_Analytics.xlsx"

with pd.ExcelWriter(
    output_file,
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer,
        sheet_name="Sales_Data",
        index=False
    )

    project_info = pd.DataFrame({
        "Project": [
            "Sales & Business Performance Analytics"
        ],
        "Purpose": [
            "Data Analyst Portfolio Project"
        ],
        "Technology": [
            "Excel, SQL Server, Power BI, DAX"
        ],
        "Records": [
            5000
        ],
        "Period": [
            "January 2025 - December 2025"
        ]
    })

    project_info.to_excel(
        writer,
        sheet_name="Project_Info",
        index=False
    )

print()
print("==========================================")
print("DATASET CREATED SUCCESSFULLY")
print("==========================================")
print(f"Total Records : {len(df)}")
print(f"Excel File    : {output_file}")
print("==========================================")