# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from home.views.menu import Ui_menu


class Ui_Schermataprincipale(object):
    def setupUi(self, Schermataprincipale):
        Schermataprincipale.setObjectName("Schermataprincipale")
        Schermataprincipale.resize(781, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Schermataprincipale.sizePolicy().hasHeightForWidth())
        Schermataprincipale.setSizePolicy(sizePolicy)
        Schermataprincipale.setMinimumSize(QtCore.QSize(781, 500))
        Schermataprincipale.setMaximumSize(QtCore.QSize(781, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/immaginelogo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Schermataprincipale.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Schermataprincipale)
        self.centralwidget.setObjectName("centralwidget")
        self.benvenuto = QtWidgets.QLabel(self.centralwidget)
        self.benvenuto.setGeometry(QtCore.QRect(240, 160, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.benvenuto.setFont(font)
        self.benvenuto.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.benvenuto.setTextFormat(QtCore.Qt.PlainText)
        self.benvenuto.setAlignment(QtCore.Qt.AlignCenter)
        self.benvenuto.setObjectName("benvenuto")
        self.immaginepesi = QtWidgets.QLabel(self.centralwidget)
        self.immaginepesi.setGeometry(QtCore.QRect(0, -9, 791, 511))
        self.immaginepesi.setText("")
        self.immaginepesi.setPixmap(QtGui.QPixmap("images/immaginepesi.PNG"))
        self.immaginepesi.setScaledContents(True)
        self.immaginepesi.setAlignment(QtCore.Qt.AlignCenter)
        self.immaginepesi.setObjectName("immaginepesi")
        self.entra = QtWidgets.QPushButton(self.centralwidget)
        self.entra.setGeometry(QtCore.QRect(330, 240, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        self.entra.setFont(font)
        self.entra.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.entra.setObjectName("entra")
        self.immaginepesi.raise_()
        self.benvenuto.raise_()
        self.entra.raise_()
        Schermataprincipale.setCentralWidget(self.centralwidget)

        self.retranslateUi(Schermataprincipale)
        QtCore.QMetaObject.connectSlotsByName(Schermataprincipale)
        self.entra.clicked.connect(self.mostramenu)

    def mostramenu(self):
        self.menu = QtWidgets.QMainWindow()
        self.ui = Ui_menu()
        self.ui.setupUi(self.menu)
        self.menu.show()

    def retranslateUi(self, Schermataprincipale):
        _translate = QtCore.QCoreApplication.translate
        Schermataprincipale.setWindowTitle(_translate("Schermataprincipale", "Schermata principale"))
        self.benvenuto.setText(_translate("Schermataprincipale", "BENVENUTO"))
        self.entra.setText(_translate("Schermataprincipale", "ENTRA"))
        self.entra.setShortcut(_translate("Schermataprincipale", "Enter"))

