from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTableWidget
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets




from PyQt5 import QtCore

from loginarayuz import *

import iconlar2qrc
import iconlarqrc


class Ui_unFollowerBuster(object):

    def __init__(self):


        self.unfollowerspage = QtWidgets.QWidget()
        self.frame_2 = QtWidgets.QFrame(self.unfollowerspage)
        self.unfollowerstable = QtWidgets.QTableWidget(self.frame_2)
        self.unfollowerstable.setObjectName("unfollowerstable")
        self.unfollowerstable.setColumnCount(2)
        self.unfollowerstable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.unfollowerstable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.unfollowerstable.setHorizontalHeaderItem(1, item)
        self.unfollowerstable.setShowGrid(False)
        self.unfollowerstable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)



    def windowclosecmmnd(self):  # pencereyi kapamaya yarayan fonksiyon.
        self.window.close()

    # menü butonuna tıkladığımızda yana doğru açılabilmesini sağlar.
    def slideLeftMenu(self):
        width = self.leftmenucontainerframe.width()
        if width == 40:
            newWidth = 200
        else:
            newWidth = 40
        self.animation = QPropertyAnimation(self.leftmenucontainerframe, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def findname1(self):
        name = self.lineEdit_2.text().lower()
        for row in range(self.unfollowerstable.rowCount()):
            item = self.unfollowerstable.item(row, 1)
            self.unfollowerstable.setRowHidden(row, name not in item.text().lower())

    def findname2(self):
        name = self.lineEdit.text().lower()
        for row in range(self.followerstable.rowCount()):
            item = self.followerstable.item(row, 1)
            self.followerstable.setRowHidden(row, name not in item.text().lower())

    def findname3(self):
        name = self.lineEdit_7.text().lower()
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 1)
            self.tableWidget.setRowHidden(row, name not in item.text().lower())

    def findname4(self):
        name = self.lineEdit_8.text().lower()
        for row in range(self.tableWidget_2.rowCount()):
            item = self.tableWidget_2.item(row, 1)
            self.tableWidget_2.setRowHidden(row, name not in item.text().lower())

    def findname5(self):
        name = self.lineEdit_9.text().lower()
        for row in range(self.tableWidget_3.rowCount()):
            item = self.tableWidget_3.item(row, 1)
            self.tableWidget_3.setRowHidden(row, name not in item.text().lower())


    # ---------------------------------------------------------------------

    # ARAYÜZ AŞAĞIDAKİ GİBİDİR. CSS KULLANILDI VE QRC DOSYALARI İMPORT EDİLDİ.

    def setupUi(self, unFollowerBuster, takipci, takipedilen):

        """
        unFollowerBuster.setWindowFlags(
            QtCore.Qt.FramelessWindowHint)  # PENCERESİZ UYGULAMA İÇİN BU ÖZELLİĞİ KULLANDIK."""
        unFollowerBuster.setObjectName("unFollowerBuster")
        unFollowerBuster.resize(1098, 807)

        # TÜM CSS KODLARI AŞAĞIDADIR.
        unFollowerBuster.setStyleSheet("*{\n"
                                       "    border:none;\n"
                                       "}\n"
                                       "#minimizewindow:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "}\n"
                                       "#adjustwindow:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "}\n"
                                       "#closewindow:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "}\n"
                                       "#leftmenucontainerframe{\n"
                                       "    background-color:#1c1c1c;\n"
                                       "}\n"
                                       "#header_frame{\n"
                                       "    background-color:#1c1c1c;\n"
                                       "}\n"
                                       "#footer_frame{\n"
                                       "    background-color:#4f4f4f;\n"
                                       "}\n"
                                       "#mainbodycontents{\n"
                                       "    background-color:#c0c0c0;\n"
                                       "    border:5px solid darkgoldenrod;\n"
                                       "}\n"
                                       "#rightframe{\n"
                                       "    background-color:#104e8b;\n"
                                       "}\n"
                                       "#lineEdit{\n"
                                       "    border: 2px solid  #8b7d6b;\n"
                                       "    border-radius:20px;\n"
                                       "}\n"
                                       "#unfllwbtn2{\n"
                                       "    background-color:#cae1ff;\n"
                                       "    border-radius:20px;\n"
                                       "    border:3px solid #8b7d6b;\n"
                                       "}\n"
                                       "#unfllwbtn2:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "}\n"
                                       "#searchbtn2:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "}\n"
                                       "#lineEdit_2{\n"
                                       "    border:2px solid #8b7d6b;\n"
                                       "    border-radius: 20px;\n"
                                       "}\n"
                                       "#searchbtn:HOVER{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "}\n"
                                       "#unfllwslctd{\n"
                                       "    background-color:#cae1ff;\n"
                                       "    border:2px solid #8b7d6b;\n"
                                       "    border-radius:20px;\n"
                                       "}\n"
                                       "#unfllwslctd:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "}\n"
                                       "#unfllwrbtn:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "    border-radius:15px;\n"
                                       "}\n"
                                       "#mtlbtn:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "    border-radius:15px;\n"
                                       "}\n"
                                       "#fllwrbtn:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "    border-radius:15px;\n"
                                       "}\n"
                                       "#ifollowbtn:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "    border-radius:15px;\n"
                                       "}\n"
                                       "#idntfllwbtn:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "    border-radius:15px;\n"
                                       "}\n"
                                       "#label_2{\n"
                                       "    color:white;\n"
                                       "\n"
                                       "}\n"
                                       "#menu_btn{\n"
                                       "    color:white;\n"
                                       "}\n"
                                       "#menu_btn:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "}\n"
                                       "#label{\n"
                                       "    background-color:white;\n"
                                       "    border-radius:10px;\n"
                                       "}\n"
                                       "#lineEdit_7{\n"
                                       "    border:2px solid #8b7d6b;\n"
                                       "    border-radius:10px;\n"
                                       "}\n"
                                       "#pushButton_2:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "}\n"
                                       "#lineEdit_8{\n"
                                       "    border:2px solid #8b7d6b;\n"
                                       "    border-radius:10px;\n"
                                       "}\n"
                                       "#pushButton_3:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "}\n"
                                       "#label_4,#label_5,#label_6,#label_7,#label_8{\n"
                                       "     color:white;\n"
                                       "}\n"
                                       "#lineEdit_9{\n"
                                       "    border:2px solid #8b7d6b;\n"
                                       "    border-radius:10px;\n"
                                       "}\n"
                                       "#pushButton_4:hover{\n"
                                       "    background-color:#DCDCDC;\n"
                                       "}")

        self.centralwidget = QtWidgets.QWidget(unFollowerBuster)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_frame = QtWidgets.QWidget(self.centralwidget)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.headerleftframe = QtWidgets.QWidget(self.header_frame)
        self.headerleftframe.setObjectName("headerleftframe")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.headerleftframe)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.menu_btn = QtWidgets.QPushButton(self.headerleftframe)
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.menu_btn.setFont(font)
        self.menu_btn.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/yeniiconlar/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QtCore.QSize(32, 32))
        self.menu_btn.setObjectName("menu_btn")
        self.horizontalLayout_4.addWidget(self.menu_btn, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.headerleftframe, 0, QtCore.Qt.AlignTop)
        self.headermidframe = QtWidgets.QWidget(self.header_frame)
        self.headermidframe.setObjectName("headermidframe")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.headermidframe)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.headermidframe)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/iconlar/instagram.svg"))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(self.headermidframe)
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.headermidframe, 0, QtCore.Qt.AlignTop)
        self.headerrightframe_2 = QtWidgets.QWidget(self.header_frame)
        self.headerrightframe_2.setObjectName("headerrightframe_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerrightframe_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minimizewindow = QtWidgets.QPushButton(self.headerrightframe_2)
        self.minimizewindow.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/yeniiconlar/icons8-minimize-window-32.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.minimizewindow.setIcon(icon1)
        self.minimizewindow.setIconSize(QtCore.QSize(50, 40))
        self.minimizewindow.setObjectName("minimizewindow")
        self.horizontalLayout_2.addWidget(self.minimizewindow)
        self.adjustwindow = QtWidgets.QPushButton(self.headerrightframe_2)
        self.adjustwindow.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/yeniiconlar/icons8-restore-window-32.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.adjustwindow.setIcon(icon2)
        self.adjustwindow.setIconSize(QtCore.QSize(50, 30))
        self.adjustwindow.setObjectName("adjustwindow")
        self.horizontalLayout_2.addWidget(self.adjustwindow)
        self.closewindow = QtWidgets.QPushButton(self.headerrightframe_2)
        self.closewindow.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/yeniiconlar/icons8-close-window-32.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.closewindow.setIcon(icon3)
        self.closewindow.setIconSize(QtCore.QSize(50, 30))
        self.closewindow.setObjectName("closewindow")
        self.horizontalLayout_2.addWidget(self.closewindow)
        self.horizontalLayout.addWidget(self.headerrightframe_2, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.header_frame)
        self.chest_frame = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chest_frame.sizePolicy().hasHeightForWidth())
        self.chest_frame.setSizePolicy(sizePolicy)
        self.chest_frame.setObjectName("chest_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.chest_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.leftmenucontainerframe = QtWidgets.QFrame(self.chest_frame)
        self.leftmenucontainerframe.setMinimumSize(QtCore.QSize(40, 0))
        self.leftmenucontainerframe.setMaximumSize(QtCore.QSize(40, 16777215))
        self.leftmenucontainerframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftmenucontainerframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftmenucontainerframe.setObjectName("leftmenucontainerframe")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.leftmenucontainerframe)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.menuframe = QtWidgets.QFrame(self.leftmenucontainerframe)
        self.menuframe.setMinimumSize(QtCore.QSize(100, 400))
        self.menuframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuframe.setObjectName("menuframe")
        self.gridLayout = QtWidgets.QGridLayout(self.menuframe)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.mtlbtn = QtWidgets.QPushButton(self.menuframe)
        self.mtlbtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/yeniiconlar/user-check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mtlbtn.setIcon(icon4)
        self.mtlbtn.setIconSize(QtCore.QSize(35, 40))
        self.mtlbtn.setObjectName("mtlbtn")
        self.gridLayout.addWidget(self.mtlbtn, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_5 = QtWidgets.QLabel(self.menuframe)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_6 = QtWidgets.QLabel(self.menuframe)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_4 = QtWidgets.QLabel(self.menuframe)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.fllwrbtn = QtWidgets.QPushButton(self.menuframe)
        self.fllwrbtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/yeniiconlar/users.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fllwrbtn.setIcon(icon5)
        self.fllwrbtn.setIconSize(QtCore.QSize(35, 40))
        self.fllwrbtn.setObjectName("fllwrbtn")
        self.gridLayout.addWidget(self.fllwrbtn, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.idntfllwbtn = QtWidgets.QPushButton(self.menuframe)
        self.idntfllwbtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/yeniiconlar/user-x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.idntfllwbtn.setIcon(icon6)
        self.idntfllwbtn.setIconSize(QtCore.QSize(35, 40))
        self.idntfllwbtn.setObjectName("idntfllwbtn")
        self.gridLayout.addWidget(self.idntfllwbtn, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.unfllwrbtn = QtWidgets.QPushButton(self.menuframe)
        self.unfllwrbtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/yeniiconlar/user-minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unfllwrbtn.setIcon(icon7)
        self.unfllwrbtn.setIconSize(QtCore.QSize(35, 40))
        self.unfllwrbtn.setObjectName("unfllwrbtn")
        self.gridLayout.addWidget(self.unfllwrbtn, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_7 = QtWidgets.QLabel(self.menuframe)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.ifollowbtn = QtWidgets.QPushButton(self.menuframe)
        self.ifollowbtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/yeniiconlar/user-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ifollowbtn.setIcon(icon8)
        self.ifollowbtn.setIconSize(QtCore.QSize(35, 40))
        self.ifollowbtn.setObjectName("ifollowbtn")
        self.gridLayout.addWidget(self.ifollowbtn, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_8 = QtWidgets.QLabel(self.menuframe)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout_9.addWidget(self.menuframe, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.horizontalLayout_8.addWidget(self.leftmenucontainerframe)
        self.mainbodycontents = QtWidgets.QFrame(self.chest_frame)
        self.mainbodycontents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainbodycontents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainbodycontents.setObjectName("mainbodycontents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainbodycontents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainbodycontents)
        self.stackedWidget.setObjectName("stackedWidget")
        self.unfollowerspage.setObjectName("unfollowerspage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.unfollowerspage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.unfollowerspage)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(290, 45))
        self.lineEdit_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_10.addWidget(self.lineEdit_2, 0, QtCore.Qt.AlignLeft)
        self.searchbtn = QtWidgets.QPushButton(self.frame_4)
        self.searchbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.searchbtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/iconlar/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchbtn.setIcon(icon9)
        self.searchbtn.setObjectName("searchbtn")
        self.horizontalLayout_10.addWidget(self.searchbtn)
        self.horizontalLayout_11.addWidget(self.frame_4)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.unfollowerstable.setObjectName("unfollowerstable")
        self.unfollowerstable.setColumnCount(2)
        self.unfollowerstable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.unfollowerstable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.unfollowerstable.setHorizontalHeaderItem(1, item)
        self.verticalLayout_4.addWidget(self.unfollowerstable)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.unfllwslctd = QtWidgets.QFrame(self.unfollowerspage)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.unfllwslctd.setFont(font)
        self.unfllwslctd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.unfllwslctd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.unfllwslctd.setObjectName("unfllwslctd")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.unfllwslctd)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.unfollowbtn = QtWidgets.QPushButton(self.unfllwslctd)
        self.unfollowbtn.setObjectName("unfollowbtn")
        self.horizontalLayout_12.addWidget(self.unfollowbtn)
        self.verticalLayout_3.addWidget(self.unfllwslctd)
        self.stackedWidget.addWidget(self.unfollowerspage)
        self.myfollowerspage = QtWidgets.QWidget()
        self.myfollowerspage.setObjectName("myfollowerspage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.myfollowerspage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.myfollowerspage)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setMinimumSize(QtCore.QSize(50, 40))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_13.addWidget(self.lineEdit)
        self.searchbtn2 = QtWidgets.QPushButton(self.frame_5)
        self.searchbtn2.setText("")
        self.searchbtn2.setIcon(icon9)
        self.searchbtn2.setIconSize(QtCore.QSize(40, 30))
        self.searchbtn2.setObjectName("searchbtn2")
        self.horizontalLayout_13.addWidget(self.searchbtn2)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_13.addWidget(self.frame_8)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.myfollowerspage)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.followerstable = QtWidgets.QTableWidget(self.frame_6)
        self.followerstable.setObjectName("followerstable")
        self.followerstable.setColumnCount(2)
        self.followerstable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.followerstable.setHorizontalHeaderItem(0, item)
        # tüm tablolar için bu işlemi uygula.
        self.unfollowerstable.horizontalHeader().setDefaultSectionSize(325)
        item = QtWidgets.QTableWidgetItem()
        self.followerstable.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_16.addWidget(self.followerstable)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.myfollowerspage)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.unfllwbtn2 = QtWidgets.QPushButton(self.frame_7)
        self.unfllwbtn2.setMinimumSize(QtCore.QSize(0, 40))
        self.unfllwbtn2.setObjectName("unfllwbtn2")
        self.horizontalLayout_15.addWidget(self.unfllwbtn2)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.stackedWidget.addWidget(self.myfollowerspage)
        self.mutualpage = QtWidgets.QWidget()
        self.mutualpage.setObjectName("mutualpage")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.mutualpage)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_24 = QtWidgets.QFrame(self.mutualpage)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_15 = QtWidgets.QLabel(self.frame_24)
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_31.addWidget(self.label_15)
        self.frame_25 = QtWidgets.QFrame(self.frame_24)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_25)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_32.addWidget(self.lineEdit_7)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon9)
        self.pushButton_2.setIconSize(QtCore.QSize(70, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_32.addWidget(self.pushButton_2)
        self.horizontalLayout_31.addWidget(self.frame_25, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_12.addWidget(self.frame_24)
        self.frame_23 = QtWidgets.QFrame(self.mutualpage)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_23)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_33.addWidget(self.tableWidget)
        self.verticalLayout_12.addWidget(self.frame_23)
        self.stackedWidget.addWidget(self.mutualpage)
        self.ifollowpage = QtWidgets.QWidget()
        self.ifollowpage.setObjectName("ifollowpage")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.ifollowpage)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_22 = QtWidgets.QFrame(self.ifollowpage)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_16 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_34.addWidget(self.label_16)
        self.frame_28 = QtWidgets.QFrame(self.frame_22)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_28)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_35.addWidget(self.lineEdit_8)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon9)
        self.pushButton_3.setIconSize(QtCore.QSize(70, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_35.addWidget(self.pushButton_3)
        self.horizontalLayout_34.addWidget(self.frame_28, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_13.addWidget(self.frame_22)
        self.frame_26 = QtWidgets.QFrame(self.ifollowpage)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.frame_26)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_26)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_36.addWidget(self.tableWidget_2)
        self.verticalLayout_13.addWidget(self.frame_26)
        self.frame_27 = QtWidgets.QFrame(self.ifollowpage)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_13.addWidget(self.frame_27)
        self.stackedWidget.addWidget(self.ifollowpage)
        self.idontfollowpage = QtWidgets.QWidget()
        self.idontfollowpage.setObjectName("idontfollowpage")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.idontfollowpage)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_32 = QtWidgets.QFrame(self.idontfollowpage)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_14.addWidget(self.frame_32)
        self.frame_29 = QtWidgets.QFrame(self.idontfollowpage)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_17 = QtWidgets.QLabel(self.frame_29)
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_37.addWidget(self.label_17)
        self.frame_30 = QtWidgets.QFrame(self.frame_29)
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_30)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_38.addWidget(self.lineEdit_9)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_30)
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon9)
        self.pushButton_4.setIconSize(QtCore.QSize(70, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_38.addWidget(self.pushButton_4)
        self.horizontalLayout_37.addWidget(self.frame_30, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_14.addWidget(self.frame_29)
        self.frame_31 = QtWidgets.QFrame(self.idontfollowpage)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.frame_31)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_39.addWidget(self.tableWidget_3)
        self.verticalLayout_14.addWidget(self.frame_31)
        self.stackedWidget.addWidget(self.idontfollowpage)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_8.addWidget(self.mainbodycontents)
        self.rightframe = QtWidgets.QFrame(self.chest_frame)
        self.rightframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightframe.setObjectName("rightframe")
        self.horizontalLayout_8.addWidget(self.rightframe)
        self.verticalLayout.addWidget(self.chest_frame)
        self.footer_frame = QtWidgets.QWidget(self.centralwidget)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.footerleftframe = QtWidgets.QFrame(self.footer_frame)
        self.footerleftframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footerleftframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footerleftframe.setObjectName("footerleftframe")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.footerleftframe)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.footerleftframe)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.horizontalLayout_5.addWidget(self.footerleftframe, 0, QtCore.Qt.AlignLeft)
        self.footerrightframe = QtWidgets.QFrame(self.footer_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.footerrightframe.setFont(font)
        self.footerrightframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footerrightframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footerrightframe.setObjectName("footerrightframe")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.footerrightframe)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton = QtWidgets.QPushButton(self.footerrightframe)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_5.addWidget(self.footerrightframe)
        self.sizegrip = QtWidgets.QFrame(self.footer_frame)
        self.sizegrip.setMinimumSize(QtCore.QSize(10, 10))
        self.sizegrip.setMaximumSize(QtCore.QSize(10, 10))
        self.sizegrip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sizegrip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sizegrip.setObjectName("sizegrip")
        self.horizontalLayout_5.addWidget(self.sizegrip, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer_frame, 0, QtCore.Qt.AlignBottom)
        unFollowerBuster.setCentralWidget(self.centralwidget)
        self.retranslateUi(unFollowerBuster)
        self.stackedWidget.setCurrentIndex(0)

        self.followerstable.horizontalHeader().setDefaultSectionSize(325)
        self.followerstable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(325)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(325)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(325)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.searchbtn.clicked.connect(self.findname1)
        self.searchbtn2.clicked.connect(self.findname2)
        self.pushButton_2.clicked.connect(self.findname3)
        self.pushButton_3.clicked.connect(self.findname4)
        self.pushButton_4.clicked.connect(self.findname5)


        self.closewindow.clicked.connect(self.windowclosecmmnd)
        QtCore.QMetaObject.connectSlotsByName(unFollowerBuster)
        self.unfllwrbtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.unfollowerspage))
        self.fllwrbtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.myfollowerspage))
        self.mtlbtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.mutualpage))
        self.ifollowbtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ifollowpage))
        self.idntfllwbtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.idontfollowpage))



        QtWidgets.QSizeGrip(self.sizegrip)
        self.menu_btn.clicked.connect(lambda: self.slideLeftMenu())

        # bizi unfollow edenleri burada tablomuza ekledik!
        self.unfollowerlist = []
        for i in takipedilen:
            if i not in takipci:
                self.unfollowerlist.append(str(i))
        row1 = 0
        self.unfollowerstable.setRowCount(len(self.unfollowerlist))
        for j in self.unfollowerlist:
            self.unfollowerstable.setItem(row1, 1, QtWidgets.QTableWidgetItem(str(j)))
            row1 += 1

        # takipçilerimizi burada tablomuza ekledik.
        self.followerstable.setShowGrid(False)
        row2 = 0
        self.followerstable.setRowCount(len(takipci))
        for j in takipci:
            self.followerstable.setItem(row2, 1, QtWidgets.QTableWidgetItem(str(j)))
            row2 += 1

        # karşılıklı takip ettiklerimizi burada tablomuza ekledik.
        self.tableWidget.setShowGrid(False)
        self.mutuallist = []
        row3 = 0
        for j in takipci:
            if j in takipedilen:
                self.mutuallist.append(j)
        self.tableWidget.setRowCount(len(self.mutuallist))
        for i in self.mutuallist:
            self.tableWidget.setItem(row3, 1, QtWidgets.QTableWidgetItem(str(i)))
            row3 += 1

        # takip ettiklerimizi buradan görebiliriz.
        self.tableWidget_2.setShowGrid(False)
        row4 = 0
        self.tableWidget_2.setRowCount(len(takipedilen))
        for i in takipedilen:
            self.tableWidget_2.setItem(row4, 1, QtWidgets.QTableWidgetItem(str(i)))
            row4 += 1

        # bizim geri takip etmediklerimizi buradan görebiliriz.
        self.tableWidget_3.setShowGrid(False)
        self.geritakipetmedigim = []
        row5 = 0
        for i in takipci:
            if i not in takipedilen:
                self.geritakipetmedigim.append(i)
        self.tableWidget_3.setRowCount(len(self.geritakipetmedigim))
        for x in self.geritakipetmedigim:
            self.tableWidget_3.setItem(row5, 1, QtWidgets.QTableWidgetItem(str(x)))
            row5 += 1

        self.minimizewindow.clicked.connect(lambda: unFollowerBuster.showMinimized())
        def adjustwindow_cmmnd():
            if unFollowerBuster.isMaximized():
                unFollowerBuster.showNormal()
            else:
                unFollowerBuster.showMaximized()

        self.adjustwindow.clicked.connect(adjustwindow_cmmnd)

    # --------------------------------------------------------------------------------------------------------------------

    def retranslateUi(self, unFollowerBuster):
        _translate = QtCore.QCoreApplication.translate
        unFollowerBuster.setWindowTitle(_translate("unFollowerBuster", "unFollower Buster"))
        self.menu_btn.setText(_translate("unFollowerBuster", "Menu"))
        self.label_2.setText(_translate("unFollowerBuster", "Instagram Follower Analyzer"))
        self.label_5.setText(_translate("unFollowerBuster", "My Followers"))
        self.label_6.setText(_translate("unFollowerBuster", "Mutual"))
        self.label_4.setText(_translate("unFollowerBuster", "Unfollowers"))
        self.label_7.setText(_translate("unFollowerBuster", "I don\'t follow"))
        self.label_8.setText(_translate("unFollowerBuster", "I follow"))
        self.label_9.setText(_translate("unFollowerBuster", "My Latest Unfollowers"))
        self.lineEdit_2.setPlaceholderText(_translate("unFollowerBuster", "search by instagram username"))
        item = self.unfollowerstable.horizontalHeaderItem(1)
        item.setText(_translate("unFollowerBuster", "Instagram Id"))
        self.unfollowbtn.setText(_translate("unFollowerBuster", "Unfollow selected"))
        self.label_10.setText(
            _translate("unFollowerBuster", "My Followers                                             "))
        self.lineEdit.setPlaceholderText(_translate("unFollowerBuster", "search by instagram username"))
        item = self.followerstable.horizontalHeaderItem(1)
        item.setText(_translate("unFollowerBuster", "Followers"))
        self.unfllwbtn2.setText(_translate("unFollowerBuster", "Unfollow Selected"))
        self.label_15.setText(_translate("unFollowerBuster", "Mutual"))
        self.lineEdit_7.setPlaceholderText(_translate("unFollowerBuster", "search by instagram username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("unFollowerBuster", "Mutual"))
        self.label_16.setText(_translate("unFollowerBuster", "I Follow"))
        self.lineEdit_8.setPlaceholderText(_translate("unFollowerBuster", "search by instagram username"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("unFollowerBuster", "I Follow"))
        self.label_17.setText(_translate("unFollowerBuster", "I Don\'t Follow Back"))
        self.lineEdit_9.setPlaceholderText(_translate("unFollowerBuster", "search by instagram username"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("unFollowerBuster", "I Don\'t Follow"))
        self.label_3.setText(_translate("unFollowerBuster", "Created By Egemen Sevgi"))
        self.pushButton.setText(_translate("unFollowerBuster", "?"))


"""if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    unFollowerBuster = QtWidgets.QMainWindow()
    ui = Ui_unFollowerBuster()
    ui.setupUi(unFollowerBuster)
    unFollowerBuster.show()
    sys.exit(app.exec_())"""
