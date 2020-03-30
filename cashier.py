# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cashier.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow_3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 734)
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 20, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 130, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 190, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 250, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 70, 401, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 70, 181, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(160, 300, 621, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 510, 361, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 570, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 570, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 510, 231, 141))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(590, 180, 181, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_5.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "                                                   CASHIER SCREEN"))
        self.label.setText(_translate("MainWindow", "Barcode"))
        self.label_2.setText(_translate("MainWindow", "Product"))
        self.label_3.setText(_translate("MainWindow", "Price"))
        self.label_4.setText(_translate("MainWindow", "Quantity"))
        self.pushButton.setText(_translate("MainWindow", "Query"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total"))
        self.pushButton_3.setText(_translate("MainWindow", "Calculate"))
        self.label_5.setText(_translate("MainWindow", "Total Amount"))
        self.pushButton_4.setText(_translate("MainWindow", "PAID"))
        self.pushButton_5.setText(_translate("MainWindow", "Purchase"))


        #########################################################
        # We activate the pushButtons of Cashier and refer to the functions defined below.
        self.pushButton.clicked.connect(self.Query)
        self.pushButton_5.clicked.connect(self.CList)
        self.pushButton_3.clicked.connect(self.CBuy)
        self.pushButton_4.clicked.connect(self.CPayment)
        self.pushButton_2.clicked.connect(self.CClean)
        ##########################################################

    def Query(self):  # We define a function to retrieve the info of a product.
        self.connection = sqlite3.connect("stock.db")
        self.cur = self.connection.cursor()

        barcode = self.lineEdit.text()  # We define a variable to call entered code into lineEdit.

        # We write a command to retrieve price and product of all types based on the code of each product.
        self.cur.execute("SELECT 'cleaning_products' AS tablo,price,product FROM cleaning_products WHERE code=? UNION ALL SELECT 'groceries' AS tablo,price,product FROM groceries WHERE code=? UNION ALL SELECT 'legumes' AS tablo,price,product FROM legumes WHERE code=? UNION ALL SELECT 'meat_products' AS tablo,price,product FROM meat_products WHERE code=?", (int(barcode), int(barcode), int(barcode), int(barcode)))
        data = self.cur.fetchall()  # We record all the data to a variable as tuples in a list.

        print(data)

        # We display the price and product name in the related lines of the cashier screen.
        self.lineEdit_2.setText(str(data[0][2]))
        self.lineEdit_3.setText(str(data[0][1]))

    def CList(self):  # We define a function to add info of purchased products to tableWidget.
        product = self.lineEdit_2.text()  # We define a variable to call info of a product name.
        price = self.lineEdit_3.text()  # We define a variable to call price of a product.
        quantity = self.lineEdit_4.text()  # We define a variable to call quantity of a product to be purchased.
        table = []  # We define a list to record product,price,quantity and price*quantity of a purchased product.
        table_ = []  # We define another list to record each purchase as a tuple.
        table.append(product)
        table.append(price)
        table.append(quantity)
        table.append(int(price) * int(quantity))
        table = tuple(table)
        table_.append(table)

        self.tableWidget.insertRow(0)  # First, we retrieve with the first row.
        # We use two for loops to locate the coordinates of each row and columns and insert the info to related coord.
        for row, form in enumerate(table_):
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
                column += 1
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

        self.lineEdit.setText("")  # After each purchase of a product, we clear the screen.
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")

    def CBuy(self):  # We define a function to calculate the total amount of purchased products.
        # Our code above creates 2 rows at each purchase in the tableWidget, therefore we divide rows into two.
        number_rows = self.tableWidget.rowCount() / 2
        payment = 0  # We define a variable to record total amount.

        # print(number_rows)

        for i in range(int(number_rows)):  # We use a for loop that will rotate in the table of purchased items.
            pay = int(self.tableWidget.item(i, 3).text())  # We locate the row, column of amount for each item.
            payment += pay  # We add each amount to the total amount.
        self.textBrowser.setText(str(payment))  # We display total calculated amount to textBrowser.

    def CPayment(self):  # We define a function to record paid amount and update the quantity of products in stock.
        from datetime import datetime
        date = datetime.now().strftime("%x")  # We define a variable to record date of purchase.
        time = datetime.now().strftime("%X")  # We define a variable to record time of purchase.
        # print(date)
        # print(time)

        self.connection_2 = sqlite3.connect("stock.db")
        self.cur_2 = self.connection_2.cursor()

        payment = self.textBrowser.toPlainText()  # We call the total amount paid from textBrowser.

        # We send paid amount, date and time to our total amount table in our database.
        self.cur_2.execute("INSERT INTO total_amount VALUES (?,?,?)", (int(payment), str(date), str(time)))
        self.connection_2.commit()

        data = []  # We define a list to record purchased products and their quantity.
        allRows = self.tableWidget.rowCount()/2
        for row in range(int(allRows)):
            c = []  # We define a list in the loop to record product,quantity of each purchased item.
            product = self.tableWidget.item(row, 0).text()  # We define a variable to record price of purchased product.
            quantity = self.tableWidget.item(row, 2).text()  # We define a variable to record quantity of purchased product.
            c.append(product)  # We add them to our list in the loop.
            c.append(quantity)
            data.append(c)  # We add our each list as a nested list to our data list.

        print(data)

        for i in data:  # We use a for loop to reach product and total quantity and update the quantity of products.
            product = i[0]  # We index the product in our data list.

            # We retrieve the purchased product code,quantity from our database based on the product in our data list.
            self.cur_2.execute("SELECT 'cleaning_products' AS tablo,code,quantity FROM cleaning_products WHERE product=? UNION ALL SELECT 'groceries' AS tablo,code,quantity FROM groceries WHERE product=? UNION ALL SELECT 'legumes' AS tablo,code,quantity FROM legumes WHERE product=? UNION ALL SELECT 'meat_products' AS tablo,code,quantity FROM meat_products WHERE product=?", (product, product, product, product))
            data_ = self.cur_2.fetchall()
            print(data_)

            # If the type matches with the purchased type of a product, we update the quantity of the product.
            if data_[0][0] == "cleaning_products":
                self.cur_2.execute("UPDATE cleaning_products SET quantity=quantity-? WHERE code=?", (int(i[1]), data_[0][1]))
                self.connection_2.commit()
            elif data_[0][0] == "groceries":
                self.cur_2.execute("UPDATE groceries SET quantity=quantity-? WHERE code=?", (int(i[1]), data_[0][1]))
                self.connection_2.commit()
            elif data_[0][0] == "legumes":
                self.cur_2.execute("UPDATE legumes SET quantity=quantity-? WHERE code=?", (int(i[1]), data_[0][1]))
                self.connection_2.commit()
            elif data_[0][0] == "meat_products":
                self.cur_2.execute("UPDATE meat_products SET quantity=quantity-? WHERE code=?", (int(i[1]), data_[0][1]))
                self.connection_2.commit()

        self.statusbar.showMessage("The operation was successful.")  # We send a message to statusbar.

    def CClean(self):  # We define a function to clear the screen as the operation completed.
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        self.textBrowser.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

