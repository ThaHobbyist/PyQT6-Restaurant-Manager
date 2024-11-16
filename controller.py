from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QTableView, QTableWidget,
    QTableWidgetItem, QWidget)
from enum import Enum

from views.view import Ui_MainWindow
from database.manage_db import *


class AppWindow(Ui_MainWindow):

    class TableStatus(Enum):
        AVAILABLE = 1
        OCCUPIED = 2
        ORDERED = 3

    def __init__(self):
        super().__init__()

        self.table_buttons = {}
        self.table_orders = {}
        self.currTable = None

        self.set_sales_table()
    
    def manage_table(self, table_num):
        print(f"Table {table_num} is managed")

        # 1. Set the selected Table Number
        self.currTable = table_num
        # 2. Check and Display the status of the current table
        self.updateTableWindow()
    
    def updateTableWindow(self):
        tnum = self.currTable
        self.label_table_num.setText(f"{tnum}")

        status = self.table_buttons[tnum]["status"]

        match status:
            case self.TableStatus.AVAILABLE:
                self.label_status.setText(f"Available")
                self.table_buttons[tnum]["button"].setStyleSheet(
                    "background-color: green; color: black"
                )
            case self.TableStatus.OCCUPIED:
                self.label_status.setText(f"Occupied")
                self.table_buttons[tnum]["button"].setStyleSheet(
                    "background-color: yellow; color: black"
                )
            case self.TableStatus.ORDERED:
                self.label_status.setText(f"Ordered")
                self.table_buttons[tnum]["button"].setStyleSheet(
                    "background-color: red; color: black"
                )
            case _:
                self.label_status.setText(f"Available")
                self.table_buttons[tnum]["button"].setStyleSheet(
                    "background-color: green; color: black"
                )
        
        earning = get_total_earnings()
        self.earning_label.setText(f"{earning:.2f}")
        self.updateTableOrders()
        
    def markOccupied(self):
        if self.table_buttons[self.currTable]["status"] == self.TableStatus.AVAILABLE:
            self.table_buttons[self.currTable]["status"] = self.TableStatus.OCCUPIED
            self.table_orders[self.currTable] = {"items": {}, "total": 0}

            self.updateTableWindow()
    
    def load_menu_items(self):
        menu_items = get_menu_items()
        self.menu_comboBox.clear()

        for item_name, price in menu_items:
            self.menu_comboBox.addItem(f"{item_name} - ${price}", (item_name, price))
    
    def add_order(self):
        if self.table_buttons[self.currTable]["status"] != self.TableStatus.AVAILABLE:
            print("Order Added")

            item_name, item_price = self.menu_comboBox.currentData()
            quantity = self.order_quantity.value()

            total_price = item_price * quantity

            self.table_orders[self.currTable]["items"][item_name] = {
                "price": item_price,
                "quantity": quantity,
                "total_price": total_price
            }
            self.updateTableOrders()
        else: 
            print("Table not occupied!")
    
    def updateTableOrders(self):
        if self.table_buttons[self.currTable]["status"] == self.TableStatus.AVAILABLE:
            self.table_orders_view.clear()
            self.table_orders_view.setRowCount(0)
        else:
            self.table_orders_view.setRowCount(0)
            self.table_orders_view.setHorizontalHeaderLabels(
                ["Item", "Quantity", "Total Price"]
            )

            for row, (item_name, data) in enumerate(
                self.table_orders[self.currTable]["items"].items()
            ):
                self.table_orders_view.insertRow(row)
                self.table_orders_view.setItem(row, 0, QTableWidgetItem(item_name))
                self.table_orders_view.setItem(
                    row, 1, QTableWidgetItem(str(data["quantity"]))
                )
                self.table_orders_view.setItem(
                    row, 2, QTableWidgetItem(f"${data['total_price']:.2f}")
                )
    
    def place_order(self):
        print("order placed")
        self.table_buttons[self.currTable]["status"] = self.TableStatus.ORDERED
        self.updateTableWindow()

    def generate_bill(self):
        if self.table_buttons[self.currTable]["status"] == self.TableStatus.ORDERED:
            items_str = "; ".join(
                [
                    f"{item_name} x {data['quantity']}"
                    for item_name, data in self.table_orders[self.currTable]["items"].items() # [(key, value)]
                ]
            )

            total_amount = sum(
                data["total_price"]
                for data in self.table_orders[self.currTable]["items"].values() # [value]
            )

            store_order(self.currTable, items_str, total_amount, "", 5)
            update_earnings(total_amount)
            
            self.table_orders[self.currTable] = {}
            self.table_buttons[self.currTable]["status"] = self.TableStatus.AVAILABLE
            self.updateTableWindow()
            self.set_sales_table()
    
    def set_sales_table(self):
        self.sales_model = get_sales_model()

