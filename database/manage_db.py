import sqlite3
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel

def create_tables():
    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                      id INTEGER PRIMARY KEY,
                      table_number INTEGER,
                      items TEXT,
                      total_amount REAL,
                      feedback TEXT,
                      rating INTEGER,
                      timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)'''
    )
    cursor.execute('''CREATE TABLE IF NOT EXISTS earnings (
                      date DATE PRIMARY KEY,
                      total_earnings REAL DEFAULT 0)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS menu (
                      id INTEGER PRIMARY KEY,
                      item_name TEXT,
                      price REAL)''')
    conn.commit()
    conn.close()

def add_menu_item(item_name, price):
    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO menu (item_name, price) VALUES (? , ?)", (item_name, price))

    conn.commit()
    conn.close()

def get_menu_items():
    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()

    cursor.execute("SELECT item_name, price FROM menu")
    items = cursor.fetchall()

    conn.close()
    return items

def store_order(table_number, items, total_amount, feedback, rating):
    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO orders (table_number, items, total_amount, feedback, rating) VALUES (?, ?, ?, ?, ?)",
    (table_number, items, total_amount, feedback, rating))

    conn.commit()
    conn.close()

def update_earnings(amount):
    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()

    cursor.execute("INSERT OR IGNORE INTO earnings (date, total_earnings) VALUES (CURRENT_DATE, 0)")
    cursor.execute("UPDATE earnings SET total_earnings = total_earnings + ? WHERE date = CURRENT_DATE", (amount,))

    conn.commit()
    conn.close()

def get_total_earnings():
    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()

    cursor.execute("SELECT total_earnings FROM earnings WHERE date = CURRENT_DATE")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0

def get_sales_model():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("restaurant.db")
    db.open()

    model = QSqlTableModel(None, db)
    model.setTable("orders")

    # query = QSqlQuery()
    # query.exec_("SELECT * FROM orders")
    # model.setQuery(query)

    model.select()
    return model

create_tables()

