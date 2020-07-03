# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proyecto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_ClienteGustavo(object):
    def setupUi(self, ClienteGustavo):
        if not ClienteGustavo.objectName():
            ClienteGustavo.setObjectName(u"ClienteGustavo")
        ClienteGustavo.resize(613, 424)
        self.centralwidget = QWidget(ClienteGustavo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Servidor_2 = QGroupBox(self.centralwidget)
        self.Servidor_2.setObjectName(u"Servidor_2")
        self.Servidor_2.setGeometry(QRect(9, 9, 611, 91))
        self.widget = QWidget(self.Servidor_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 581, 41))
        self.Servidor = QHBoxLayout(self.widget)
        self.Servidor.setObjectName(u"Servidor")
        self.Servidor.setContentsMargins(0, 0, 0, 0)
        self.ip_2 = QLabel(self.widget)
        self.ip_2.setObjectName(u"ip_2")

        self.Servidor.addWidget(self.ip_2)

        self.ip = QLineEdit(self.widget)
        self.ip.setObjectName(u"ip")

        self.Servidor.addWidget(self.ip)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.Servidor.addWidget(self.label_4)

        self.puerto = QLineEdit(self.widget)
        self.puerto.setObjectName(u"puerto")

        self.Servidor.addWidget(self.puerto)

        self.conectar = QPushButton(self.Servidor_2)
        self.conectar.setObjectName(u"conectar")
        self.conectar.setGeometry(QRect(10, 60, 581, 23))
        self.Estudiante = QGroupBox(self.centralwidget)
        self.Estudiante.setObjectName(u"Estudiante")
        self.Estudiante.setGeometry(QRect(6, 110, 611, 141))
        self.widget1 = QWidget(self.Estudiante)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 20, 581, 122))
        self.formLayout = QFormLayout(self.widget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nombre = QLineEdit(self.widget1)
        self.nombre.setObjectName(u"nombre")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nombre)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.email = QLineEdit(self.widget1)
        self.email.setObjectName(u"email")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.email)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.contrasenia = QLineEdit(self.widget1)
        self.contrasenia.setObjectName(u"contrasenia")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.contrasenia)

        self.enviarB = QPushButton(self.widget1)
        self.enviarB.setObjectName(u"enviar_archivo")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.enviarB)

        self.Archivo = QGroupBox(self.centralwidget)
        self.Archivo.setObjectName(u"Archivo")
        self.Archivo.setGeometry(QRect(6, 260, 611, 71))
        self.widget2 = QWidget(self.Archivo)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(0, 20, 595, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.abrirB = QPushButton(self.widget2)
        self.abrirB.setObjectName(u"abrir_archivo")

        self.horizontalLayout_3.addWidget(self.abrirB)

        self.abrir = QLineEdit(self.widget2)
        self.abrir.setObjectName(u"abrir")

        self.horizontalLayout_3.addWidget(self.abrir)

        self.estado = QLabel(self.centralwidget)
        self.estado.setObjectName(u"estado")
        self.estado.setGeometry(QRect(460, 360, 40, 16))
        self.conexion = QLabel(self.centralwidget)
        self.conexion.setObjectName(u"conexion")
        self.conexion.setGeometry(QRect(510, 360, 81, 16))
        ClienteGustavo.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ClienteGustavo)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 613, 21))
        ClienteGustavo.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ClienteGustavo)
        self.statusbar.setObjectName(u"statusbar")
        ClienteGustavo.setStatusBar(self.statusbar)

        self.retranslateUi(ClienteGustavo)

        QMetaObject.connectSlotsByName(ClienteGustavo)
    # setupUi

    def retranslateUi(self, ClienteGustavo):
        ClienteGustavo.setWindowTitle(QCoreApplication.translate("ClienteGustavo", u"MainWindow", None))
        self.Servidor_2.setTitle(QCoreApplication.translate("ClienteGustavo", u"Servidor", None))
        self.ip_2.setText(QCoreApplication.translate("ClienteGustavo", u"IP", None))
        self.label_4.setText(QCoreApplication.translate("ClienteGustavo", u"Puerto", None))
        self.conectar.setText(QCoreApplication.translate("ClienteGustavo", u"Conectar", None))
        self.Estudiante.setTitle(QCoreApplication.translate("ClienteGustavo", u"Estudiante", None))
        self.label.setText(QCoreApplication.translate("ClienteGustavo", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("ClienteGustavo", u"Email", None))
        self.label_3.setText(QCoreApplication.translate("ClienteGustavo", u"Contrase\u00f1a", None))
        self.enviarB.setText(QCoreApplication.translate("ClienteGustavo", u"Enviar", None))
        self.Archivo.setTitle(QCoreApplication.translate("ClienteGustavo", u"Archivo", None))
        self.abrirB.setText(QCoreApplication.translate("ClienteGustavo", u"Abrir", None))
        self.estado.setText(QCoreApplication.translate("ClienteGustavo", u"Estado: ", None))
        self.conexion.setText(QCoreApplication.translate("ClienteGustavo", u"Desconectado", None))
    # retranslateUi

