# 🚀 Retail Analytics Platform

A production-style Data Engineering project that demonstrates how to build an end-to-end ETL pipeline using **Apache Spark**, perform data validation and transformations, create an analytical **Fact Sales** table, generate business insights, and store optimized datasets in **Apache Parquet** format.

---

## 📌 Project Overview

This project simulates a real-world retail company's data pipeline.

Synthetic retail datasets are generated using the **Faker** library, processed using **Apache Spark**, validated, transformed, joined into a single analytical dataset, and stored in **Parquet** format for efficient querying.

The project also includes multiple business analytics reports and Spark performance optimizations.

---



# 🔄 Pipeline Flow

```
Raw CSV Files
       │
       ▼
Apache Spark Session
       │
       ▼
Data Validation
       │
       ▼
Data Cleaning
       │
       ▼
Data Transformation
       │
       ▼
Multi-table Joins
       │
       ▼
Fact Sales DataFrame
       │
       ├─────────────► Business Analytics
       │
       ├─────────────► Spark SQL
       │
       ▼
Apache Parquet
```

---

# 📂 Project Structure

```
Retail-Data-Lakehouse-Pipeline
│
├── data
│   ├── raw
│   └── processed
│
├── experiments
│
├── logs
│
├── sql
│
├── src
│   ├── analytics
│   ├── config
│   ├── extract
│   ├── generate
│   ├── load
│   ├── transform
│   └── validate
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Processing Engine | Apache Spark |
| Storage Format | Apache Parquet |
| Synthetic Data | Faker |
| Data Processing | PySpark |
| Version Control | Git & GitHub |

---

# 📊 Datasets

The project generates synthetic retail datasets.

- Customers
- Orders
- Order Items
- Products
- Payments

Total Records:

- Customers : 1,000
- Orders : 1,000
- Order Items : 1,000
- Products : 1,000
- Payments : 1,000

---

# ⚙ Features

## Data Generation

- Generate synthetic retail datasets
- Maintain primary and foreign key relationships
- Modular data generators

---

## Data Validation

- Missing Value Detection
- Duplicate Row Detection
- Duplicate Primary Key Detection

---

## Data Cleaning

- Remove whitespace
- Standardize text case
- Email cleaning
- Phone number cleaning
- Data type conversion

---

## Data Transformation

- Multi-table joins
- Fact Sales table creation
- Sales Amount calculation

---



## Spark Optimizations

- Lazy Evaluation
- Cache
- Persist
- Repartition
- Coalesce
- Broadcast Join
- Explain Plan
- Spark SQL

---

# 💾 Storage

Final analytical data is stored in **Apache Parquet** format for:

- Faster reads
- Compression
- Columnar storage
- Schema preservation

---





# 📚 Spark Concepts Covered

- Spark Session
- DataFrames
- Transformations
- Actions
- Lazy Evaluation
- Joins
- Aggregations
- Broadcast Join
- Cache
- Persist
- Repartition
- Coalesce
- Explain Plan
- Spark SQL
- Apache Parquet

---





# 👨‍💻 Author

**Lucky Jha**

GitHub: https://github.com/jhalucky

LinkedIn: https://www.linkedin.com/in/theluckyjha

---
