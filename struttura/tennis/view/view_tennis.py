
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gestionecampodatennis(object):
    def setupUi(self, gestionecampodatennis):
        gestionecampodatennis.setObjectName("gestionecampodatennis")
        gestionecampodatennis.resize(781, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(gestionecampodatennis.sizePolicy().hasHeightForWidth())
        gestionecampodatennis.setSizePolicy(sizePolicy)
        gestionecampodatennis.setMinimumSize(QtCore.QSize(781, 500))
        gestionecampodatennis.setMaximumSize(QtCore.QSize(781, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/immaginelogo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        gestionecampodatennis.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(gestionecampodatennis)
        self.centralwidget.setObjectName("centralwidget")
        self.immaginepesi = QtWidgets.QLabel(self.centralwidget)
        self.immaginepesi.setGeometry(QtCore.QRect(-10, 0, 791, 501))
        self.immaginepesi.setText("")
        self.immaginepesi.setPixmap(QtGui.QPixmap("images/immaginepesisfocata.jpeg"))
        self.immaginepesi.setScaledContents(True)
        self.immaginepesi.setAlignment(QtCore.Qt.AlignCenter)
        self.immaginepesi.setObjectName("immaginepesi")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(40, 50, 581, 381))
        self.listView.setObjectName("listView")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(600, 50, 22, 381))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setInvertedAppearance(True)
        self.aggiungiutente = QtWidgets.QPushButton(self.centralwidget)
        self.aggiungiutente.setGeometry(QtCore.QRect(630, 130, 140, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.aggiungiutente.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.aggiungiutente.setFont(font)
        self.aggiungiutente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aggiungiutente.setObjectName("aggiungiutente")
        self.eliminautente = QtWidgets.QPushButton(self.centralwidget)
        self.eliminautente.setGeometry(QtCore.QRect(630, 210, 140, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.eliminautente.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.eliminautente.setFont(font)
        self.eliminautente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminautente.setObjectName("eliminautente")
        self.visualizzautente = QtWidgets.QPushButton(self.centralwidget)
        self.visualizzautente.setGeometry(QtCore.QRect(630, 170, 140, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.visualizzautente.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.visualizzautente.setFont(font)
        self.visualizzautente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualizzautente.setObjectName("visualizzautente")
        self.calendario = QtWidgets.QPushButton(self.centralwidget)
        self.calendario.setGeometry(QtCore.QRect(630, 50, 140, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.calendario.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.calendario.setFont(font)
        self.calendario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calendario.setObjectName("calendario")
        self.freccia = QtWidgets.QPushButton(self.centralwidget)
        self.freccia.setGeometry(QtCore.QRect(20, 15, 51, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 1, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.freccia.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.freccia.setFont(font)
        self.freccia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.freccia.setIconSize(QtCore.QSize(40, 40))
        self.freccia.setDefault(False)
        self.freccia.setObjectName("freccia")
        gestionecampodatennis.setCentralWidget(self.centralwidget)

        self.retranslateUi(gestionecampodatennis)
        QtCore.QMetaObject.connectSlotsByName(gestionecampodatennis)

    def retranslateUi(self, gestionecampodatennis):
        _translate = QtCore.QCoreApplication.translate
        gestionecampodatennis.setWindowTitle(_translate("gestionecampodatennis", "Gestione campo da tennis"))
        self.aggiungiutente.setText(_translate("gestionecampodatennis", "Aggiungi utente"))
        self.eliminautente.setText(_translate("gestionecampodatennis", "Elimina utente"))
        self.visualizzautente.setText(_translate("gestionecampodatennis", "Visualizza utente"))
        self.calendario.setText(_translate("gestionecampodatennis", "Calendario"))
        self.freccia.setText(_translate("gestionecampodatennis", "⬅️"))
        self.freccia.setShortcut(_translate("gestionecampodatennis", "Alt+Left"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     gestionecampodatennis = QtWidgets.QMainWindow()
#     ui = Ui_gestionecampodatennis()
#     ui.setupUi(gestionecampodatennis)
#     gestionecampodatennis.show()
#     sys.exit(app.exec_())
