# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'actualizar_prod.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UP_PROD(object):
    def setupUi(self, UP_PROD):
        UP_PROD.setObjectName("UP_PROD")
        UP_PROD.resize(500, 400)
        UP_PROD.setMinimumSize(QtCore.QSize(500, 400))
        UP_PROD.setMaximumSize(QtCore.QSize(500, 400))
        self.horizontalLayout = QtWidgets.QHBoxLayout(UP_PROD)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(UP_PROD)
        self.frame.setStyleSheet("QFrame{\n"
"\n"
"background-color: rgb(0, 145, 217);\n"
"\n"
"}\n"
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
"QLineedit{\n"
"\n"
"border: 0px;\n"
"color: rgb(255, 255, 255);\n"
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
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.line_edit_buscar = QtWidgets.QLineEdit(self.frame)
        self.line_edit_buscar.setObjectName("line_edit_buscar")
        self.horizontalLayout_7.addWidget(self.line_edit_buscar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.btn_edit_buscar = QtWidgets.QPushButton(self.frame)
        self.btn_edit_buscar.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_edit_buscar.setObjectName("btn_edit_buscar")
        self.horizontalLayout_7.addWidget(self.btn_edit_buscar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_name_insert_2 = QtWidgets.QLabel(self.frame)
        self.label_name_insert_2.setObjectName("label_name_insert_2")
        self.horizontalLayout_2.addWidget(self.label_name_insert_2)
        self.line_edit_nombre = QtWidgets.QLineEdit(self.frame)
        self.line_edit_nombre.setObjectName("line_edit_nombre")
        self.horizontalLayout_2.addWidget(self.line_edit_nombre)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_marca_insert_2 = QtWidgets.QLabel(self.frame)
        self.label_marca_insert_2.setObjectName("label_marca_insert_2")
        self.horizontalLayout_4.addWidget(self.label_marca_insert_2)
        self.line_edit_marca = QtWidgets.QLineEdit(self.frame)
        self.line_edit_marca.setObjectName("line_edit_marca")
        self.horizontalLayout_4.addWidget(self.line_edit_marca)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_modelo_insert_2 = QtWidgets.QLabel(self.frame)
        self.label_modelo_insert_2.setObjectName("label_modelo_insert_2")
        self.horizontalLayout_5.addWidget(self.label_modelo_insert_2)
        self.line_edit_modelo = QtWidgets.QLineEdit(self.frame)
        self.line_edit_modelo.setObjectName("line_edit_modelo")
        self.horizontalLayout_5.addWidget(self.line_edit_modelo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_cant_insert_2 = QtWidgets.QLabel(self.frame)
        self.label_cant_insert_2.setObjectName("label_cant_insert_2")
        self.horizontalLayout_6.addWidget(self.label_cant_insert_2)
        self.spin_edit_cant = QtWidgets.QSpinBox(self.frame)
        self.spin_edit_cant.setObjectName("spin_edit_cant")
        self.horizontalLayout_6.addWidget(self.spin_edit_cant)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_precio_insert_2 = QtWidgets.QLabel(self.frame)
        self.label_precio_insert_2.setObjectName("label_precio_insert_2")
        self.horizontalLayout_9.addWidget(self.label_precio_insert_2)
        self.line_edit_precio = QtWidgets.QLineEdit(self.frame)
        self.line_edit_precio.setObjectName("line_edit_precio")
        self.horizontalLayout_9.addWidget(self.line_edit_precio)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_edit_back = QtWidgets.QPushButton(self.frame)
        self.btn_edit_back.setMinimumSize(QtCore.QSize(120, 30))
        self.btn_edit_back.setStyleSheet("QPushButton:hover{\n"
"background-color: rgb(255, 27, 6);\n"
"color: rgb(0, 0, 0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"")
        self.btn_edit_back.setObjectName("btn_edit_back")
        self.horizontalLayout_8.addWidget(self.btn_edit_back)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.btn_edit_aceptar = QtWidgets.QPushButton(self.frame)
        self.btn_edit_aceptar.setMinimumSize(QtCore.QSize(120, 30))
        self.btn_edit_aceptar.setObjectName("btn_edit_aceptar")
        self.horizontalLayout_8.addWidget(self.btn_edit_aceptar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(UP_PROD)
        QtCore.QMetaObject.connectSlotsByName(UP_PROD)

    def retranslateUi(self, UP_PROD):
        _translate = QtCore.QCoreApplication.translate
        UP_PROD.setWindowTitle(_translate("UP_PROD", "ACTUALIZAR PRODUCTO"))
        self.label.setText(_translate("UP_PROD", "ACTUALIZAR PRODUCTO"))
        self.label_3.setText(_translate("UP_PROD", "NOMBRE DEL PRODUCTO"))
        self.btn_edit_buscar.setText(_translate("UP_PROD", "BUSCAR"))
        self.label_name_insert_2.setText(_translate("UP_PROD", "NOMBRE"))
        self.label_marca_insert_2.setText(_translate("UP_PROD", "MARCA"))
        self.label_modelo_insert_2.setText(_translate("UP_PROD", "MODELO"))
        self.label_cant_insert_2.setText(_translate("UP_PROD", "CANTIDAD"))
        self.label_precio_insert_2.setText(_translate("UP_PROD", "PRECIO"))
        self.btn_edit_back.setText(_translate("UP_PROD", "SALIR"))
        self.btn_edit_aceptar.setText(_translate("UP_PROD", "ACEPTAR"))
