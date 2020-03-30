# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employee_screen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow_2(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(850, 750)
        mainWindow.setMinimumSize(QtCore.QSize(850, 750))
        mainWindow.setMaximumSize(QtCore.QSize(850, 750))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 10, 800, 750))
        self.tabWidget.setMinimumSize(QtCore.QSize(800, 750))
        self.tabWidget.setMaximumSize(QtCore.QSize(800, 750))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(30, 40, 181, 41))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(200, 50, 411, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(30, 156, 181, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(200, 160, 411, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 214, 411, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 210, 181, 41))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 274, 411, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 270, 181, 41))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(650, 110, 131, 34))
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 170, 131, 34))
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
        self.pushButton_2.setPalette(palette)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 230, 131, 34))
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
        self.pushButton_3.setPalette(palette)
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(200, 330, 411, 181))
        self.textBrowser.setObjectName("textBrowser")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(30, 106, 181, 41))
        self.label_17.setObjectName("label_17")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(200, 110, 411, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 151, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 171, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 240, 171, 41))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 70, 321, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 130, 321, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 250, 321, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 80, 131, 34))
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
        self.pushButton_4.setPalette(palette)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 140, 131, 34))
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
        self.pushButton_5.setPalette(palette)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(620, 200, 131, 34))
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
        self.pushButton_6.setPalette(palette)
        self.pushButton_6.setObjectName("pushButton_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(240, 310, 321, 161))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 190, 321, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(30, 180, 171, 41))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 31))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "                                                  EMPLOYEE SCREEN"))
        self.label.setText(_translate("mainWindow", "Type"))
        self.comboBox.setItemText(0, _translate("mainWindow", "Groceries"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Meat Products"))
        self.comboBox.setItemText(2, _translate("mainWindow", "Cleaning Products"))
        self.comboBox.setItemText(3, _translate("mainWindow", "Legumes"))
        self.label_2.setText(_translate("mainWindow", "Stock Code"))
        self.label_3.setText(_translate("mainWindow", "Quantity"))
        self.label_4.setText(_translate("mainWindow", "Price"))
        self.pushButton.setText(_translate("mainWindow", "Query"))
        self.pushButton_2.setText(_translate("mainWindow", "Save"))
        self.pushButton_3.setText(_translate("mainWindow", "Delete"))
        self.label_17.setText(_translate("mainWindow", "Product"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "Stock Operations"))
        self.label_5.setText(_translate("mainWindow", "Employee ID"))
        self.label_6.setText(_translate("mainWindow", "Employee Name"))
        self.label_7.setText(_translate("mainWindow", "Position"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "Store Manager"))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "Cashier"))
        self.pushButton_4.setText(_translate("mainWindow", "Query"))
        self.pushButton_5.setText(_translate("mainWindow", "Save"))
        self.pushButton_6.setText(_translate("mainWindow", "Delete"))
        self.label_8.setText(_translate("mainWindow", "Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "Employee Operations"))

        ############################################################
        # We activate the pushButtons of Employee Operations and refer to the functions defined below.
        self.pushButton_4.clicked.connect(self.Query)
        self.pushButton_5.clicked.connect(self.Save)
        self.pushButton_6.clicked.connect(self.Delete)

        ###########################################################
        # We activate the pushButtons of Stock Operations and refer to the functions defined below.
        self.pushButton.clicked.connect(self.SQuery)
        self.pushButton_2.clicked.connect(self.SSave)
        self.pushButton_3.clicked.connect(self.SDelete)
        ######################################################

    def Query(self):  # We define a function to retrieve the info of a employee.
        self.connection = sqlite3.connect("stock.db")  # We connect to our database file (stock.db).
        self.cur = self.connection.cursor()  # We define the cursor.

        self.cur.execute("SELECT * FROM user")  # We select all the info of the user from database.
        data = self.cur.fetchall()  # We define a variable called data and record the user ID and password.
        print(data)

        id = self.lineEdit_4.text()  # We define a variable to call entered into lineEdit_4 as ID.

        k = 1
        for i in data:  # We define a for loop to retrieve the concerning info to the related lines in employee screen.
            if id == str(i[2]):
                # print(i)
                self.lineEdit_5.setText(str(i[0]))  # We write employee name to lineEdit_5.
                self.lineEdit_6.setText(str(i[1]))  # We write employee password to lineEdit_6.
                self.textBrowser_2.setText("")  #

                if i[3] == 'M':  # If the user's position is manager, the combobox shows manager.
                    self.comboBox_2.setCurrentText("Store Manager")
                else:  # Otherwise, the combobox show the cashier.
                    self.comboBox_2.setCurrentText("Cashier")
                break

            if k == len(data):  # The loop looks into the whole data and it breaks when it does not match any ID.
                self.lineEdit_5.setText("")  # We clear the lines and write nothing to the related lines.
                self.lineEdit_6.setText("")
                self.textBrowser_2.setText("This ID doesn't belong to anyone.")  # We give a warning message.
            k += 1

    def Save(self):  # We define a function to update user info or enter a new user.
        self.connection_ = sqlite3.connect("stock.db")
        self.cur_ = self.connection_.cursor()

        id_ = []  # We define a list to record the id's of the users.
        self.cur_.execute("SELECT * FROM user")
        data_ = self.cur_.fetchall()

        for i in data_:  # We add the id's of the current users into the list defined above.
            id_.append(i[2])
        print(id_)

        # We define the related variables to update or save the info of a user.
        id = self.lineEdit_4.text()
        name = self.lineEdit_5.text()
        password = self.lineEdit_6.text()
        position = self.comboBox_2.currentText()

        if position == "Cashier":
            position_ = "C"

        else:
            position_ = "M"

        # print(position)

        if int(id) in id_:  # If the entered id is in the database, then we activate the update method.
            # We write a command to update the name,password,position that matches the entered id.
            self.cur_.execute("UPDATE user SET name=?, password=?, position=? WHERE id=?", (name, int(password),
                                                                                            position_, int(id)))
            self.connection_.commit()  # We commit to record the changes.

            self.lineEdit_4.setText("")  # We clear the related lines and give a message to the user.
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.textBrowser_2.setText("User data updated successfully")

        else:  # If the entered id is not in the database, then we activate the new entry method.
            # We write a command to enter id,name,password,position in accordance with the columns in the database.
            self.cur_.execute("INSERT INTO user VALUES (?,?,?,?)", (name, int(password), int(id), position_))
            self.connection_.commit()
            self.lineEdit_4.setText("")  # We clear the related lines and give a message to the user.
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.textBrowser_2.setText("New user added successfully")

    def Delete(self):  # We define a function to delete a user.
        self._connection_ = sqlite3.connect("stock.db")
        self._cur_ = self._connection_.cursor()

        id = self.lineEdit_4.text()

        # We write a command to delete a user that matches with the id in the database.
        self._cur_.execute("DELETE FROM user WHERE id=?", (int(id),))  # !!!Be careful about the comma at the end.
        self._connection_.commit()
        self.textBrowser_2.setText("User deleted successfully")  # We give a message to the user.

    def SQuery(self):  # We define a function to search for a product in the database.
        self.connection_1 = sqlite3.connect("stock.db")
        self.cur_1 = self.connection_1.cursor()

        type = self.comboBox.currentText()  # We define a variable to match the type in the combobox and the database.
        print(type)
        stock = self.lineEdit.text()  # We define a variable to call entered data into the stock code line.

        if type == "Groceries":  # If the selected type matches the term defined in our screen, we proceed.
            self.cur_1.execute("SELECT * FROM groceries")  # We take all the related data from groceries.
            data_1 = self.cur_1.fetchall()  # We record the info to our variable.
            print(data_1)

            id_ = []  # We define a list to record the id's of the products.

            for i in data_1:  # We use a for loop to add id's of the product into the defined list.
                id_.append(i[0])
            print(id_)

            if int(stock) in id_:  # If the entered id into the related line on the screen, we proceed.
                for i in data_1:  # We use a for loop to look for the product with the entered id.
                    if int(stock) == i[0]:  # If the entered id matches, we call the related info to the related lines.
                        self.lineEdit_13.setText(i[3])
                        self.lineEdit_2.setText(str(i[1]))
                        self.lineEdit_3.setText(str(i[2]))
                        self.textBrowser.setText("")
                        break
            else:
                self.lineEdit_13.setText("")  # If the entered id does not match, we give a warning to the user.
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("This product is not found in the stock.")

        elif type == "Meat Products":
            self.cur_1.execute("SELECT * FROM meat_products")
            data_1 = self.cur_1.fetchall()
            print(data_1)

            id_ = []

            for i in data_1:
                id_.append(i[0])
            print(id_)

            if int(stock) in id_:
                for i in data_1:
                    if int(stock) == i[0]:
                        self.lineEdit_13.setText(i[3])
                        self.lineEdit_2.setText(str(i[1]))
                        self.lineEdit_3.setText(str(i[2]))
                        self.textBrowser.setText("")
                        break
            else:
                self.lineEdit_13.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("This product is not found in the stock.")

        elif type == "Cleaning Products":
            self.cur_1.execute("SELECT * FROM cleaning_products")
            data_1 = self.cur_1.fetchall()
            print(data_1)

            id_ = []

            for i in data_1:
                id_.append(i[0])
            print(id_)

            if int(stock) in id_:
                for i in data_1:
                    if int(stock) == i[0]:
                        self.lineEdit_13.setText(i[3])
                        self.lineEdit_2.setText(str(i[1]))
                        self.lineEdit_3.setText(str(i[2]))
                        self.textBrowser.setText("")
                        break
            else:
                self.lineEdit_13.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("This product is not found in the stock.")

        elif type == "Legumes":
            self.cur_1.execute("SELECT * FROM legumes")
            data_1 = self.cur_1.fetchall()
            print(data_1)

            id_ = []

            for i in data_1:
                id_.append(i[0])
            print(id_)

            if int(stock) in id_:
                for i in data_1:
                    if int(stock) == i[0]:
                        self.lineEdit_13.setText(i[3])
                        self.lineEdit_2.setText(str(i[1]))
                        self.lineEdit_3.setText(str(i[2]))
                        self.textBrowser.setText("")
                        break
            else:
                self.lineEdit_13.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("This product is not found in the stock.")

    def SSave(self):  # We define a function to update a product or add a new product.
        self.connection_2 = sqlite3.connect("stock.db")
        self.cur_2 = self.connection_2.cursor()

        # We define a variable for each related line in the screen to call them.
        type = self.comboBox.currentText()
        product = self.lineEdit_13.text()
        stock = self.lineEdit.text()
        quantity = self.lineEdit_2.text()
        price = self.lineEdit_3.text()

        if type == "Groceries":  # We retrieve data of each type from the database.
            self.cur_2.execute("SELECT * FROM groceries")
            data_1 = self.cur_2.fetchall()

            id_1 = []

            for i in data_1:
                id_1.append(i[0])

            if int(stock) in id_1:  # If the stock code entered matches with the product id, we update the product info.
                # We use the command below to update the info of a product.
                self.cur_2.execute("UPDATE groceries SET quantity=?,price=?,product=? WHERE code=?", (int(quantity), int(price), product, int(stock)))
                self.connection_2.commit()
                self.lineEdit_13.setText("")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("The product has been updated.")  # We give a message to the user.

            else:  # If the we have a new stock code entered, then we create a new product with the command below.
                self.cur_2.execute("INSERT INTO groceries VALUES (?,?,?,?)", (int(stock), int(quantity), int(price), product))
                self.connection_2.commit()
                self.lineEdit_13.setText("")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("New product has been added.") # We give a message to the user.

        elif type == "Meat Products":
            self.cur_2.execute("SELECT * FROM meat_products")
            data_1 = self.cur_2.fetchall()

            id_1 = []

            for i in data_1:
                id_1.append(i[0])

            if int(stock) in id_1:
                self.cur_2.execute("UPDATE meat_products SET quantity=?,price=?,product=? WHERE code=?", (int(quantity), int(price), product, int(stock)))
                self.connection_2.commit()
                self.lineEdit_13.setText("")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("The product has been updated.")

            else:
                self.cur_2.execute("INSERT INTO meat_products VALUES (?,?,?,?)", (int(stock), int(quantity), int(price), product))
                self.connection_2.commit()
                self.lineEdit_13.setText("")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("New product has been added.")

        elif type == "Cleaning Products":
            self.cur_2.execute("SELECT * FROM cleaning_products")
            data_1 = self.cur_2.fetchall()

            id_1 = []

            for i in data_1:
                id_1.append(i[0])

            if int(stock) in id_1:
                self.cur_2.execute("UPDATE cleaning_products SET quantity=?,price=?,product=? WHERE code=?", (int(quantity), int(price), product, int(stock)))
                self.connection_2.commit()
                self.lineEdit_13.setText("")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("The product has been updated.")

            else:
                self.cur_2.execute("INSERT INTO cleaning_products VALUES (?,?,?,?)", (int(stock), int(quantity), int(price), product))
                self.connection_2.commit()
                self.lineEdit_13.setText("")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("New product has been added.")

        elif type == "Legumes":
            self.cur_2.execute("SELECT * FROM legumes")
            data_1 = self.cur_2.fetchall()

            id_1 = []

            for i in data_1:
                id_1.append(i[0])

            if int(stock) in id_1:
                self.cur_2.execute("UPDATE legumes SET quantity=?,price=?,product=? WHERE code=?", (int(quantity), int(price), product, int(stock)))
                self.connection_2.commit()
                self.lineEdit_13.setText("")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("The product has been updated.")

            else:
                self.cur_2.execute("INSERT INTO legumes VALUES (?,?,?,?)", (int(stock), int(quantity), int(price), product))
                self.connection_2.commit()
                self.lineEdit_13.setText("")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.textBrowser.setText("New product has been added.")

    def SDelete(self):  # We define a function to delete a product from the database.
        self.connection_3 = sqlite3.connect("stock.db")
        self.cur_3 = self.connection_3.cursor()

        type = self.comboBox.currentText()
        stock = self.lineEdit.text()

        if type == "Groceries":
            self.cur_3.execute("DELETE FROM groceries WHERE code=?", (int(stock),))
            self.connection_3.commit()
            self.lineEdit_13.setText("")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.textBrowser.setText("Product has been deleted.")

        elif type == "Meat Products":
            self.cur_3.execute("DELETE FROM meat_products WHERE code=?", (int(stock),))
            self.connection_3.commit()
            self.lineEdit_13.setText("")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.textBrowser.setText("Product has been deleted.")

        elif type == "Cleaning Products":
            self.cur_3.execute("DELETE FROM cleaning_products WHERE code=?", (int(stock),))
            self.connection_3.commit()
            self.lineEdit_13.setText("")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.textBrowser.setText("Product has been deleted.")

        elif type == "Legumes":
            self.cur_3.execute("DELETE FROM legumes WHERE code=?", (int(stock),))
            self.connection_3.commit()
            self.lineEdit_13.setText("")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.textBrowser.setText("Product has been deleted.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_2()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())