"""
Structured Data ETL Practical Exam
Topic: Load structured CSV data into SQLite3 using Python

Student Task:
Complete only the SQLite3 parts:

1. CREATE TABLE
2. INSERT INTO
3. SELECT FROM

The extraction and transformation code is already provided.
"""

import csv
import sqlite3

CSV_FILE = "sales_data.csv"
DB_FILE = "sales_etl.db"


def extract_data():
    records = []

    with open(CSV_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    return records


def transform_data(records):
    transformed_records = []

    for record in records:
        quantity = int(record["quantity"])
        unit_price = float(record["unit_price"])
        total_sales = quantity * unit_price

        transformed_record = {
            "date": record["date"],
            "product": record["product"],
            "category": record["category"],
            "quantity": quantity,
            "unit_price": unit_price,
            "total_sales": total_sales,
            "payment_method": record["payment_method"]
        }

        transformed_records.append(transformed_record)

    return transformed_records


def connect_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    return conn, cursor


def create_table(cursor):
    """
    TODO #1:
    Write the SQLite3 CREATE TABLE statement.

    Table name:
    sales_records

    Columns:
    id INTEGER PRIMARY KEY AUTOINCREMENT
    date TEXT
    product TEXT
    category TEXT
    quantity INTEGER
    unit_price REAL
    total_sales REAL
    payment_method TEXT
    """

    # Write CREATE TABLE code here
Create TABLE sales_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    unit_price REAL,
    total_sales REAL,
    payment_method TEXT
);
    
    pass


def insert_records(cursor, records):
    """
    TODO #2:
    Write the SQLite3 INSERT INTO statement.

    Insert the following fields:
    date
    product
    category
    quantity
    unit_price
    total_sales
    payment_method
    """

    # Write INSERT INTO code here
    Insert into sales_records (date, product, category, quantity, unit_price, total_sales, payment_method);
    pass


def select_records(cursor):
    """
    TODO #3:
    Write the SQLite3 SELECT statement.

    Select and display all records from sales_records.

    Expected columns:
    id, date, product, category, quantity, unit_price, total_sales, payment_method
    """

    # Write SELECT code here
SELECT * from sales_records where id, date, product, category, quantity, unit_price, total_sales, payment_method FROM sales_records;

    pass


def main():
    raw_records = extract_data()
    clean_records = transform_data(raw_records)

    conn, cursor = connect_database()

    create_table(cursor)
    insert_records(cursor, clean_records)
    conn.commit()

    select_records(cursor)

    conn.close()


if __name__ == "__main__":
    main()
