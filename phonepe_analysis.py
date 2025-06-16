import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load CSV files
users_df = pd.read_csv("users.csv")
transactions_df = pd.read_csv("transactions.csv")

# Step 2: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iswarya#01",
    database="phonepeDB"
)
cursor = conn.cursor()

# Step 3: Create Tables (if not exists)
cursor.execute("DROP TABLE IF EXISTS transactions")
cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("""
CREATE TABLE users (
    UserID VARCHAR(10) PRIMARY KEY,
    State VARCHAR(50),
    Age INT,
    Gender VARCHAR(10)
)
""")

cursor.execute("""
CREATE TABLE transactions (
    TransactionID VARCHAR(15) PRIMARY KEY,
    UserID VARCHAR(10),
    Amount DECIMAL(10,2),
    PaymentType VARCHAR(20),
    TransactionDate DATE,
    FOREIGN KEY (UserID) REFERENCES users(UserID)
)
""")

# Step 4: Insert Data into `users`
for _, row in users_df.iterrows():
    cursor.execute("""
        INSERT INTO users (UserID, State, Age, Gender)
        VALUES (%s, %s, %s, %s)
    """, (row['UserID'], row['State'], row['Age'], row['Gender']))

# Step 5: Insert Data into `transactions`
for _, row in transactions_df.iterrows():
    cursor.execute("""
        INSERT INTO transactions (TransactionID, UserID, Amount, PaymentType, TransactionDate)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        row['TransactionID'],
        row['UserID'],
        row['Amount'],
        row['PaymentType'],
        row['TransactionDate']
    ))

# Commit changes
conn.commit()

# Step 6: Read back for analysis
query = """
SELECT u.Gender, u.State, t.PaymentType, t.Amount, t.TransactionDate
FROM users u
JOIN transactions t ON u.UserID = t.UserID
"""
df = pd.read_sql(query, conn)

# Step 7: Analysis

# Total Revenue
total_revenue = df["Amount"].sum()
print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")

# Revenue by Gender
print("\nRevenue by Gender:")
print(df.groupby("Gender")["Amount"].sum().reset_index())

# Transactions by Payment Type
print("\nTransactions by Payment Type:")
print(df["PaymentType"].value_counts().reset_index().rename(columns={"index": "PaymentType", "PaymentType": "Count"}))

# Users by State
print("\nUsers by State:")
print(df.groupby("State")["Gender"].count().reset_index().rename(columns={"Gender": "UserCount"}))

# Step 8: Visualizations
sns.set(style="whitegrid")

# Revenue by Gender
plt.figure(figsize=(6, 4))
sns.barplot(data=df.groupby("Gender")["Amount"].sum().reset_index(),
            x="Gender", y="Amount", hue="Gender", palette="pastel", legend=False)
plt.title("Revenue by Gender")
plt.tight_layout()
plt.show()

# Transactions by Payment Type
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="PaymentType", hue="PaymentType", palette="Set2", legend=False)
plt.title("Transactions by Payment Type")
plt.tight_layout()
plt.show()

# Revenue by Year
df["Year"] = pd.to_datetime(df["TransactionDate"]).dt.year
plt.figure(figsize=(6, 4))
sns.barplot(data=df.groupby("Year")["Amount"].sum().reset_index(),
            x="Year", y="Amount", hue="Year", palette="coolwarm", legend=False)
plt.title("Yearly Revenue")
plt.tight_layout()
plt.show()

# Step 9: Clean Up
cursor.close()
conn.close()


