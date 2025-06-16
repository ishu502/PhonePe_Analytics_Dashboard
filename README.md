# PhonePe_Analytics_Dashboard
Power BI dashboard using python and SQL for PhonePe transactions and user insights

# 📊 PhonePe Analytics Dashboard
This repository showcases a complete PhonePe-style analytics dashboard built using **Power BI**, **Python**, and **MySQL**. The project visualizes user and transaction data to provide insights into revenue, user demographics, payment behavior, and more.

## 🛠️ Tools Used
- 📌 **Power BI** – for dashboard creation and data visualization  
- 🐍 **Python (Pandas, MySQL Connector)** – for loading CSVs, inserting into MySQL, and data preprocessing  
- 🧮 **MySQL** – for relational database structure and queries  
- 📂 **CSV Files** – users and transactions sample datasets

---

## 📁 Files Included

| File/Folder              | Description                              |
|--------------------------|------------------------------------------|
| `PhonePeDashboard.pbix`  | Power BI dashboard file                  |
| `users.csv`              | User-level data                          |
| `transactions.csv`       | Transaction-level data                   |
| `dashboard_script.py`    | Python script for MySQL upload & analysis|
| `queries.sql`            | SQL queries used for insights            |
| `screenshots/` (optional)| Dashboard preview images (if added)      |

## 📌 Key Insights Visualized
- ✅ **Total Revenue**
- 👥 **Total Users by State**
- 💳 **Transactions by Payment Type**
- 📈 **Revenue Trend by Year**
- 🗺️ **Geographical User Distribution**
- 👨‍👩‍👧‍👦 **UPI Usage by Age Group**
- 📋 **Detailed Transaction Table**

## ⚙️ How It Works
1. Load `users.csv` and `transactions.csv` into MySQL using either:
   - Python script `dashboard_script.py`, or
   - SQL `LOAD DATA INFILE` commands

2. Use Python to:
   - Preprocess data
   - Add calculated columns (like Age Groups)

3. Connect Power BI to MySQL or use the CSVs directly

4. Create visualizations in Power BI using:
   - Cards (KPIs)
   - Donut, bar, line, and map charts
   - DAX measures (for calculated insights)

## 💡 Inspiration
This project was inspired by the way modern apps like PhonePe use data-driven decisions to understand users and improve digital payment experiences.

## 🔗 Author
**Iswarya Reddy**  
Connect with me on [LinkedIn](https://www.linkedin.com/in/iswarya-kummathi-2a999b205)  
📧 iswaryareddy4@email.com

## ⭐️ If you liked this project, feel free to give it a star!

