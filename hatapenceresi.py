

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hataPenceresi(object):
    def closewindoww(self):
        self.window.close
    def setupUi(self, hataPenceresi):
        hataPenceresi.setObjectName("hataPenceresi")
        hataPenceresi.resize(618, 173)
        hataPenceresi.setStyleSheet("background-color:#DCDCDC;")
        self.centralwidget = QtWidgets.QWidget(hataPenceresi)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("COLOR:RED;")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton.setStyleSheet("border-radius:20px;\n"
"border:2px solid teal;\n"
"background-color:#b5b5b5;\n"
"color:white;\n"
"")
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.closewindoww)
        self.verticalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame)
        hataPenceresi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(hataPenceresi)
        self.statusbar.setObjectName("statusbar")
        hataPenceresi.setStatusBar(self.statusbar)

        self.retranslateUi(hataPenceresi)
        QtCore.QMetaObject.connectSlotsByName(hataPenceresi)

    def retranslateUi(self, hataPenceresi):
        _translate = QtCore.QCoreApplication.translate
        hataPenceresi.setWindowTitle(_translate("hataPenceresi", "Error"))
        self.label.setText(_translate("hataPenceresi", "Error, your username or password is invalid."))
        self.pushButton.setText(_translate("hataPenceresi", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hataPenceresi = QtWidgets.QMainWindow()
    ui = Ui_hataPenceresi()
    ui.setupUi(hataPenceresi)
    hataPenceresi.show()
    sys.exit(app.exec_())
