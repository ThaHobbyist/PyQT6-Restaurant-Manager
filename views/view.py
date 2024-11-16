# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(926, 600)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 9, 901, 541))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.horizontalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget = QWidget(self.tab_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 551, 314))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(100, 100))

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        for row in range(3):
            for col in range(3):
                tnum = row * 3 + col + 1
                btn = QPushButton(f"Table {tnum}", self.gridLayoutWidget)
                btn.setObjectName(f"Table {tnum}")
                btn.setStyleSheet("color: black; background-color: green")
                btn.clicked.connect(lambda _, tn=tnum: self.manage_table(tn))

                sizePolicy.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
                btn.setSizePolicy(sizePolicy)
                btn.setMinimumSize(QSize(100, 100))

                font = QFont()
                font.setFamilies(["Ubuntu"])
                btn.setFont(font)

                self.table_buttons[tnum] = {
                    "button": btn,
                    "status": self.TableStatus.AVAILABLE,
                }

                self.gridLayout.addWidget(btn, row, col, 1, 1)

        # self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_6.setObjectName(u"pushButton_6")
        # sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        # self.pushButton_6.setSizePolicy(sizePolicy)
        # self.pushButton_6.setMinimumSize(QSize(100, 100))
        

        # self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)

        # self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_5.setObjectName(u"pushButton_5")
        # sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        # self.pushButton_5.setSizePolicy(sizePolicy)
        # self.pushButton_5.setMinimumSize(QSize(100, 100))

        # self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        # self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_3.setObjectName(u"pushButton_3")
        # sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        # self.pushButton_3.setSizePolicy(sizePolicy)
        # self.pushButton_3.setMinimumSize(QSize(100, 100))

        # self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        # self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_2.setObjectName(u"pushButton_2")
        # sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        # self.pushButton_2.setSizePolicy(sizePolicy)
        # self.pushButton_2.setMinimumSize(QSize(100, 100))

        # self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        # self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_4.setObjectName(u"pushButton_4")
        # sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        # self.pushButton_4.setSizePolicy(sizePolicy)
        # self.pushButton_4.setMinimumSize(QSize(100, 100))

        # self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)

        # self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_7.setObjectName(u"pushButton_7")
        # sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        # self.pushButton_7.setSizePolicy(sizePolicy)
        # self.pushButton_7.setMinimumSize(QSize(100, 100))

        # self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)

        # self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_8.setObjectName(u"pushButton_8")
        # sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        # self.pushButton_8.setSizePolicy(sizePolicy)
        # self.pushButton_8.setMinimumSize(QSize(100, 100))

        # self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)

        # self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        # self.pushButton_9.setObjectName(u"pushButton_9")
        # sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        # self.pushButton_9.setSizePolicy(sizePolicy)
        # self.pushButton_9.setMinimumSize(QSize(100, 100))

        # self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 480, 66, 18))
        self.earning_label = QLabel(self.tab_3)
        self.earning_label.setObjectName(u"earning_label")
        self.earning_label.setGeometry(QRect(60, 480, 66, 18))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")

        self.sales_table = QTableView(self.tab_4)
        self.sales_table.setObjectName(u"sales_table")
        self.sales_table.setModel(self.sales_model)
        self.sales_table.setGeometry(QRect(10, 10, 561, 481))

        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.widget = QWidget(self.horizontalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 0))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 18))
        self.label_table_num = QLabel(self.widget)
        self.label_table_num.setObjectName(u"label_table_num")
        self.label_table_num.setGeometry(QRect(120, 10, 66, 18))
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 91, 18))
        self.label_status = QLabel(self.widget)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(110, 40, 66, 18))
        self.btn_set_occ = QPushButton(self.widget)
        self.btn_set_occ.setObjectName(u"btn_set_occ")
        self.btn_set_occ.setGeometry(QRect(10, 70, 171, 26))
        self.btn_set_occ.clicked.connect(self.markOccupied)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 110, 66, 18))

        self.menu_comboBox = QComboBox(self.widget)
        self.menu_comboBox.setObjectName(u"menu_comboBox")
        self.menu_comboBox.setGeometry(QRect(60, 110, 86, 26))
        self.load_menu_items()

        self.order_quantity = QSpinBox(self.widget)
        self.order_quantity.setObjectName(u"order_quantity")
        self.order_quantity.setGeometry(QRect(150, 110, 44, 27))
        self.add_order_button = QPushButton(self.widget)
        self.add_order_button.setObjectName(u"add_order_button")
        self.add_order_button.setGeometry(QRect(200, 110, 88, 26))
        self.add_order_button.clicked.connect(self.add_order)
        
        self.table_orders_view = QTableWidget(0, 3, self.widget)
        self.table_orders_view.setObjectName(u"table_orders_view")
        self.table_orders_view.setGeometry(QRect(10, 150, 281, 281))

        self.place_orders_btn = QPushButton(self.widget)
        self.place_orders_btn.setObjectName(u"place_orders_btn")
        self.place_orders_btn.setGeometry(QRect(177, 440, 111, 26))
        self.place_orders_btn.clicked.connect(self.place_order)

        self.generate_bill_btn = QPushButton(self.widget)
        self.generate_bill_btn.setObjectName(u"generate_bill_btn")
        self.generate_bill_btn.setGeometry(QRect(177, 490, 111, 26))
        self.generate_bill_btn.clicked.connect(self.generate_bill)

        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 926, 23))
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuView.menuAction())
        self.menuView.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        # self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        # self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sales", None))
        self.earning_label.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tables", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Sales", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Table Number", None))
        self.label_table_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Table Status", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Available", None))
        self.btn_set_occ.setText(QCoreApplication.translate("MainWindow", u"Mark Occupied", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Order:", None))
        self.add_order_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.place_orders_btn.setText(QCoreApplication.translate("MainWindow", u"Place Order", None))
        self.generate_bill_btn.setText(QCoreApplication.translate("MainWindow", u"Finish and Bill", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

