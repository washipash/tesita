# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscar_venta.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venta_emergente(object):
    def setupUi(self, venta_emergente):
        venta_emergente.setObjectName("venta_emergente")
        venta_emergente.resize(840, 747)
        self.horizontalLayout = QtWidgets.QHBoxLayout(venta_emergente)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(venta_emergente)
        self.frame.setStyleSheet("background-color: rgb(0, 145, 217);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("\n"
"\n"
"QLabel{\n"
"font-size: 12pt;\n"
"font: 87 12pts \"Arial Black\";\n"
"background-color:#000000ff;\n"
"color:rgb(0, 0, 127);\n"
"border: 0px solid #14C80C; \n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("\n"
"\n"
"QLabel{\n"
"font-size: 12pt;\n"
"font: 87 12pts \"Arial Black\";\n"
"background-color:#000000ff;\n"
"color:rgb(0, 0, 127);\n"
"border: 0px solid #14C80C; \n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"\n"
"border: 0px;\n"
"    background-color: rgb(255, 255, 255);\n"
"border-bottom:2px solid rgb(61, 61, 61);\n"
"font:75 12pt \"Times New Roman\" ;\n"
"\n"
"}\n"
"\n"
"QTextEdit{\n"
"\n"
"border: 0px;\n"
"    background-color: rgb(255, 255, 255);\n"
"border-bottom:2px solid rgb(61, 61, 61);\n"
"font:75 12pt \"Times New Roman\" ;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 206, 151);\n"
"color: rgb(0, 0, 0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"    background-color: rgb(198, 198, 198);\n"
"gridine-color: rgb(0, 206, 151);\n"
"font-size: 12pt;\n"
"color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"\n"
"background-color: rgb(0, 206, 151);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"font-size:12pt;\n"
"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"border:1px solid rgb(0, 206, 151);\n"
"}\n"
"\n"
"QDateEdit {\n"
"                background-color: white;\n"
"                border: 2px solid gray;\n"
"                border-radius: 10px;\n"
"                padding: 2px;\n"
"            }\n"
"\n"
"QDateTimeEdit {\n"
"                background-color: white;\n"
"                border: 2px solid gray;\n"
"                border-radius: 10px;\n"
"                padding: 2px;\n"
"            }\n"
"            QDateEdit::drop-down {\n"
"                width: 20px;\n"
"\n"
"    }\n"
"\n"
"            QScrollBar:vertical {\n"
"                background-color: #333333;\n"
"                width: 10px;\n"
"                margin: 0px 0px 0px 0px;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QScrollBar:horizontal {\n"
"                background-color: #333333;\n"
"                height: 10px;\n"
"                margin: 0px 0px 0px 0px;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QScrollBar::handle:vertical {\n"
"                background-color: #B0B0B0;\n"
"                min-height: 20px;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QScrollBar::handle:horizontal {\n"
"                background-color: #B0B0B0;\n"
"                min-width: 20px;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QScrollBar::sub-line:vertical, QScrollBar::sub-line:horizontal {\n"
"                background-color: white;\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"            }\n"
"            QScrollBar::add-line:vertical, QScrollBar::add-line:horizontal {\n"
"                background-color: white;\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"            }\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.ci_line = QtWidgets.QLineEdit(self.frame_2)
        self.ci_line.setObjectName("ci_line")
        self.horizontalLayout_4.addWidget(self.ci_line)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.timedate_line = QtWidgets.QDateTimeEdit(self.frame_2)
        self.timedate_line.setStyleSheet("            Qtimedatet {\n"
"                background-color: white;\n"
"                border: 2px solid gray;\n"
"                border-radius: 10px;\n"
"                padding: 2px;\n"
"            }\n"
"            QTimeEdit::down-button, QTimeEdit::up-button {\n"
"                width: 20px;\n"
"                border: none;\n"
"                background: white;\n"
"                subcontrol-position: right;\n"
"                subcontrol-origin: margin;\n"
"            }")
        self.timedate_line.setObjectName("timedate_line")
        self.horizontalLayout_3.addWidget(self.timedate_line)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.name_line = QtWidgets.QLineEdit(self.frame_2)
        self.name_line.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_line.setObjectName("name_line")
        self.horizontalLayout_5.addWidget(self.name_line)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.apellido_line = QtWidgets.QLineEdit(self.frame_2)
        self.apellido_line.setMaximumSize(QtCore.QSize(170, 16777215))
        self.apellido_line.setObjectName("apellido_line")
        self.horizontalLayout_6.addWidget(self.apellido_line)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_8.addWidget(self.lineEdit)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.verticalLayout_13.addLayout(self.verticalLayout_10)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.obj_comprados_table = QtWidgets.QTableWidget(self.frame_2)
        self.obj_comprados_table.setMaximumSize(QtCore.QSize(700, 600))
        self.obj_comprados_table.setObjectName("obj_comprados_table")
        self.obj_comprados_table.setColumnCount(8)
        self.obj_comprados_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.obj_comprados_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.obj_comprados_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.obj_comprados_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.obj_comprados_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.obj_comprados_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.obj_comprados_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.obj_comprados_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.obj_comprados_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.obj_comprados_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.obj_comprados_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.obj_comprados_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.obj_comprados_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.obj_comprados_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.obj_comprados_table.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(202, 202, 0))
        brush.setStyle(QtCore.Qt.Dense3Pattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.obj_comprados_table.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 203, 98))
        brush.setStyle(QtCore.Qt.Dense3Pattern)
        item.setBackground(brush)
        self.obj_comprados_table.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.obj_comprados_table.setItem(0, 7, item)
        self.verticalLayout_3.addWidget(self.obj_comprados_table)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.tasa_line = QtWidgets.QLineEdit(self.frame_2)
        self.tasa_line.setMinimumSize(QtCore.QSize(130, 0))
        self.tasa_line.setMaximumSize(QtCore.QSize(130, 16777215))
        self.tasa_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tasa_line.setObjectName("tasa_line")
        self.verticalLayout_4.addWidget(self.tasa_line)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem10)
        self.verticalLayout_12.addLayout(self.verticalLayout_9)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem11)
        self.cancel_btn = QtWidgets.QPushButton(self.frame_2)
        self.cancel_btn.setMinimumSize(QtCore.QSize(120, 30))
        self.cancel_btn.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 27, 6);\n"
"color: rgb(0, 0, 0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"")
        self.cancel_btn.setObjectName("cancel_btn")
        self.verticalLayout_11.addWidget(self.cancel_btn)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem12)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.horizontalLayout_10.addLayout(self.verticalLayout_12)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(venta_emergente)
        QtCore.QMetaObject.connectSlotsByName(venta_emergente)

    def retranslateUi(self, venta_emergente):
        _translate = QtCore.QCoreApplication.translate
        venta_emergente.setWindowTitle(_translate("venta_emergente", "Agregar venta"))
        self.label.setText(_translate("venta_emergente", "BUSCAR VENTA"))
        self.label_2.setText(_translate("venta_emergente", "CEDULA CLIENTE"))
        self.label_3.setText(_translate("venta_emergente", "FECHA Y HORA"))
        self.label_4.setText(_translate("venta_emergente", "NOMBRE"))
        self.label_5.setText(_translate("venta_emergente", "APELLIDO"))
        self.label_6.setText(_translate("venta_emergente", "N° DE VENTA"))
        self.label_7.setText(_translate("venta_emergente", "PRODUCTOS COMPRADOS"))
        item = self.obj_comprados_table.horizontalHeaderItem(0)
        item.setText(_translate("venta_emergente", "NOMBRE"))
        item = self.obj_comprados_table.horizontalHeaderItem(1)
        item.setText(_translate("venta_emergente", "MARCA"))
        item = self.obj_comprados_table.horizontalHeaderItem(2)
        item.setText(_translate("venta_emergente", "MODELO"))
        item = self.obj_comprados_table.horizontalHeaderItem(3)
        item.setText(_translate("venta_emergente", "CANT"))
        item = self.obj_comprados_table.horizontalHeaderItem(4)
        item.setText(_translate("venta_emergente", "PRECIO UNIT"))
        item = self.obj_comprados_table.horizontalHeaderItem(5)
        item.setText(_translate("venta_emergente", "PRECIO VENTA"))
        item = self.obj_comprados_table.horizontalHeaderItem(6)
        item.setText(_translate("venta_emergente", "PRECIO Bs"))
        __sortingEnabled = self.obj_comprados_table.isSortingEnabled()
        self.obj_comprados_table.setSortingEnabled(False)
        item = self.obj_comprados_table.item(0, 5)
        item.setText(_translate("venta_emergente", "$"))
        item = self.obj_comprados_table.item(0, 6)
        item.setText(_translate("venta_emergente", "Bs"))
        item = self.obj_comprados_table.item(0, 7)
        item.setText(_translate("venta_emergente", "TOTAL"))
        self.obj_comprados_table.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("venta_emergente", "TASA USADA"))
        self.tasa_line.setPlaceholderText(_translate("venta_emergente", "$"))
        self.cancel_btn.setText(_translate("venta_emergente", "SALIR"))