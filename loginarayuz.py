from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import arayuz2
from hatapenceresi import *
from arayuz2 import *
import time


class Ui_LoginPage(object):

    def __init__(self):

        self.takipci = []
        self.takipedilen = []

    def signIn(self):
        try:

            # selenium ile bizi kendi profilimize götürür.
            self.options = webdriver.ChromeOptions()
            self.options.headless = False  # selenium browser kapatmak için bu özelliği True işaretlemek zorundayız.
            self.browser = webdriver.Chrome(options=self.options)
            self.browser.get("https://www.instagram.com/")


            self.username = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
            self.password = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

            self.username.clear()
            self.password.clear()

            self.username.send_keys(self.kllncadigir.text())
            self.password.send_keys(self.kllncadigir_2.text())

            self.btnSubmit = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

            self.btnSubmit.click()

            self.notnow = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
            self.notnow_2 = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]'))).click()

            self.password = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img"))).click()
            
            self.profilebtn = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div'))).click()
            self.takipcibtn = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div'))).click()

            # takipçileri al

            self.takipcibtn = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '.notranslate._0imsa')))
            # burada selenium'un sayfa açıldığında aşağı kaydırmasını sağlamaya yardımcı olmak için-
            # 4 satır uzunluğunda bir JavaScript kodu ekledim.
            # bu kod, kaydırma çubuğunu class ismiyle önceden belirttikleri için selenium bulur ve sayfanın sonuna kadar kaydırır.
            jsKomut = """
            sayfa = document.querySelector(".isgrP");
            sayfa.scrollTo(0,sayfa.scrollHeight);
            var sayfaSonu = sayfa.scrollHeight;
            return sayfaSonu;
            """
            # bu blok, sayfanın sonuna geldiğinde break döngüsüyle sonlandırır ve sonra kullanıcı isimlerini alır.
            sayfaSonu = self.browser.execute_script(jsKomut)
            while True:
                son = sayfaSonu
                time.sleep(1)
                sayfaSonu = self.browser.execute_script(jsKomut)
                if son == sayfaSonu:
                    break

            # takipçileri alan blok.
            self.takipcilerial = self.browser.find_elements_by_css_selector('.notranslate._0imsa')
            for self.i in self.takipcilerial:
                self.takipci.append(self.i.text)

            self.takipcibtncarpi = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button'))).click()
            self.takipedilenbtn = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/div'))).click()
            time.sleep(1)
            # takip edilenleri al

            jsKomut = """
            sayfa = document.querySelector(".isgrP");
            sayfa.scrollTo(0,sayfa.scrollHeight);
            var sayfaSonu = sayfa.scrollHeight;
            return sayfaSonu;
            """
            sayfaSonu = self.browser.execute_script(jsKomut)
            while True:
                son = sayfaSonu
                time.sleep(1)
                sayfaSonu = self.browser.execute_script(jsKomut)
                if son == sayfaSonu:
                    break
            self.takipedilenlerial = self.browser.find_elements_by_css_selector('.notranslate._0imsa')
            for self.j in self.takipedilenlerial:
                self.takipedilen.append(self.j.text)

            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_unFollowerBuster()
            self.ui.setupUi(self.window,self.takipci,self.takipedilen)
            self.window.show()


        except:
            self.hatamesaji()


    def uyarilabeli(self):  # connecting to instagram may take a while label'inin özellikleri.
        self.label_5.setStyleSheet("color:red;\n"
                                   "font-size:12px;\n")

    def closewindow(self):  # pencereyi kapama butonuna işlev veren fonksiyon.
        self.window.close()

    def hatamesaji(self):  # eğer kullanıcının girdiği şifre veya kullanıcı adı yanlışsa hata penceresi açılır.
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_hataPenceresi()
        self.ui.setupUi(self.window)
        self.window.show()
        time.sleep(2)

    # ARAYÜZ AŞAĞIDAKİ GİBİDİR.
    def setupUi(self, LoginPage):
        LoginPage.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        LoginPage.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(587, 868)
        LoginPage.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 110, 501, 651))
        self.frame.setStyleSheet("\n"
                                 "#frame{\n"
                                 "    border-image: url(:/newPrefix/instabackground.jpg);\n"
                                 "    border-radius:25px;\n"
                                 "    opacity: 0.9;\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 40, 501, 561))
        self.label.setStyleSheet("background-color:rgba(0,0,0,200);\n"
                                 "border-radius:25px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 50, 290, 131))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(39)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.kllncadigir = QtWidgets.QLineEdit(self.frame)
        self.kllncadigir.setGeometry(QtCore.QRect(120, 260, 251, 51))
        self.kllncadigir.setStyleSheet("border:4px solid darkgoldenrod;\n"
                                       "border-radius:20px;")
        self.kllncadigir.setObjectName("kllncadigir")
        self.kllncadigir_2 = QtWidgets.QLineEdit(self.frame)
        self.kllncadigir_2.setGeometry(QtCore.QRect(120, 350, 251, 51))
        self.kllncadigir_2.setStyleSheet("border:4px solid darkgoldenrod;\n"
                                         "border-radius:20px;")
        self.kllncadigir_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.kllncadigir_2.setObjectName("kllncadigir_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 620, 361, 21))
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(180, 170, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.loginbtn = QtWidgets.QPushButton(self.frame)
        self.loginbtn.setGeometry(QtCore.QRect(170, 450, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loginbtn.setFont(font)
        self.loginbtn.setStyleSheet("#loginbtn:hover{\n"
                                    "    background-color:white;\n"
                                    "}\n"
                                    "#loginbtn{\n"
                                    "    BACKGROUND-COLOR:#DCDCDC;\n"
                                    "    border-radius:20px;\n"
                                    "    color:BLACK;\n"
                                    "}\n"
                                    "#loginbtn:pressed{\n"
                                    "    padding-left:5px;\n"
                                    "    padding-top:5px;\n"
                                    "}")
        self.loginbtn.setObjectName("loginbtn")
        self.loginbtn.clicked.connect(self.signIn)

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(245, 10, 31, 28))
        self.pushButton.setStyleSheet("#pushButton{\n"
                                      "    BACKGROUND-COLOR:RED;\n"
                                      "}\n"
                                      "#pushButton:hover{\n"
                                      "    BACKGROUND-COLOR:#CC0000;\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.closewindow)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(60, 510, 391, 51))
        self.label_5.setStyleSheet("color:red;\n")
        self.label_5.setText("")
        self.label_5.setObjectName("label")
        LoginPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    # ARAYÜZDEKİ HER BİR HARF KARAKTERİNİ LATİN ALFABESİNE ÇEVİRİR.
    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Log In"))
        self.label_2.setText(_translate("LoginPage", "Log In"))
        self.kllncadigir.setPlaceholderText(_translate("LoginPage", "please enter your intagram username"))
        self.kllncadigir_2.setPlaceholderText(_translate("LoginPage", "please enter your intagram password"))
        self.label_3.setText(_translate("LoginPage", "                  Created and designed by Egemen Sevgi"))
        self.label_4.setText(_translate("LoginPage", "Instagram Analyzer™"))
        self.loginbtn.setText(_translate("LoginPage", "Log In"))
        self.pushButton.setText(_translate("LoginPage", "X"))
        self.label_5.setText(_translate("LoginPage", "                   Connecting to instagram may take while."))


import loginqrc  # giriş sayfasındaki resimleri import ettik.

# bu kısım, uygulamamızı çalıştırır.
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())
