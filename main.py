#Importing Modules/Files
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QSplashScreen
from PyQt5.QtGui import QPixmap, QMovie, QPainter
from getpasswd import Ui_getpasswd_window as getpassword
from userselect import Ui_userselect_window as userselect
from newuser import Ui_newuser_window as newuser
from deleteuser import Ui_deleteuser_window as deluser
from deleteaccount import Ui_deleteaccount_window as delaccount
import string
import sqlite3
import sys, time


class Ui_main_window(object):

    #Constructor
    def __init__(self):

        self.getDialog = QtWidgets.QMainWindow()
        self.getpass_screen = getpassword()
        self.getpass_screen.setupUi(self.getDialog)

        self.delaccountDialog = QtWidgets.QMainWindow()
        self.delaccount_screen = delaccount()
        self.delaccount_screen.setupUi(self.delaccountDialog)


    def setupUi(self, main_window):

        global gender

        #Main Window
        main_window.setObjectName("main_window")
        main_window.resize(606, 510)
        main_window.setMinimumSize(QtCore.QSize(606, 510))
        main_window.setMaximumSize(606,510)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        main_window.setFont(font)
        main_window.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setWindowOpacity(1.0)
        main_window.setStyleSheet("background-color: #121212 ;")
        main_window.setAutoFillBackground(False)

        #Menubar
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.menubar.setStyleSheet("color: cyan ;")
        self.menuOptions.setStyleSheet("color: white ;")

        self.actionGetpassword = QtWidgets.QAction(main_window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGetpassword.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.actionGetpassword.setFont(font)
        self.actionGetpassword.setObjectName("actionSetting")
        self.menuOptions.addAction(self.actionGetpassword)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.actionGetpassword.triggered.connect(self.senddata)

        self.actionQuit = QtWidgets.QAction(main_window)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.actionGetpassword.setFont(font)
        self.actionQuit.setObjectName("actionQuit")
        self.menuOptions.addAction(self.actionGetpassword)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionQuit)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.actionQuit.triggered.connect(sys.exit)

        #accountname_label
        self.accountname_label = QtWidgets.QLabel(main_window)
        self.accountname_label.setGeometry(QtCore.QRect(20, 120, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.accountname_label.setFont(font)
        self.accountname_label.setMouseTracking(False)
        self.accountname_label.setStyleSheet("color: white")
        self.accountname_label.setTextFormat(QtCore.Qt.AutoText)
        self.accountname_label.setScaledContents(False)
        self.accountname_label.setWordWrap(False)
        self.accountname_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.accountname_label.setObjectName("accountname_label")

        #accountname_lineedit
        self.accountname_lineedit = QtWidgets.QLineEdit(main_window)
        self.accountname_lineedit.setGeometry(QtCore.QRect(190, 130, 371, 41))
        self.accountname_lineedit.setMouseTracking(True)
        self.accountname_lineedit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.accountname_lineedit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.accountname_lineedit.setFocus()
        self.accountname_lineedit.setStyleSheet("border :2px solid orange ;" "color:white ;")
        self.accountname_lineedit.setObjectName("accountname_lineedit")

        #username_label
        self.username_label = QtWidgets.QLabel(main_window)
        self.username_label.setGeometry(QtCore.QRect(30, 220, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.username_label.setWordWrap(True)
        self.username_label.setStyleSheet("color: white")
        self.username_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.username_label.setObjectName("username_label")

        #username_lineedit
        self.username_lineedit = QtWidgets.QLineEdit(main_window)
        self.username_lineedit.setGeometry(QtCore.QRect(190, 230, 371, 41))
        self.username_lineedit.setMouseTracking(True)
        self.username_lineedit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.username_lineedit.setStyleSheet("border :2px solid orange ;" "color:white ;")
        self.username_lineedit.setObjectName("username_lineedit")

        #password_label
        self.password_label = QtWidgets.QLabel(main_window)
        self.password_label.setGeometry(QtCore.QRect(30, 320, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setMouseTracking(False)
        self.password_label.setStyleSheet("color: white")
        self.password_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.password_label.setObjectName("password_label")

        #password_lineedit
        self.password_lineedit = QtWidgets.QLineEdit(main_window)
        self.password_lineedit.setGeometry(QtCore.QRect(190, 330, 371, 41))
        self.password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineedit.setMouseTracking(True)
        self.password_lineedit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.password_lineedit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhNoTextHandles|QtCore.Qt.ImhSensitiveData)
        self.password_lineedit.setStyleSheet("border :2px solid orange ;" "color:white ;")
        self.password_lineedit.setObjectName("password_lineedit")

        #showpassword_button
        self.showpassword_button = QtWidgets.QPushButton(main_window)
        self.showpassword_button.setGeometry(QtCore.QRect(570, 330, 31, 41))
        self.showpassword_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showpassword_button.setIcon(icon5)
        self.showpassword_button.setIconSize(QtCore.QSize(31, 41))
        self.showpassword_button.setCheckable(True)
        self.showpassword_button.setFlat(True)
        self.showpassword_button.setToolTip("Show/Hide Password")
        self.showpassword_button.setObjectName("showpassword_button")

        #encryptdata_button
        self.encryptdata_button = QtWidgets.QPushButton(main_window)
        self.encryptdata_button.setGeometry(QtCore.QRect(370, 450, 161, 55))
        self.encryptdata_button.setToolTip("Save Password")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.encryptdata_button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.encryptdata_button.setIcon(icon1)
        self.encryptdata_button.setAutoDefault(True)
        self.encryptdata_button.setDefault(True)
        self.encryptdata_button.setFlat(False)
        self.encryptdata_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.encryptdata_button.setStyleSheet("border :3px solid orange ;" "color:white ;")
        self.encryptdata_button.setObjectName("encryptdata_button")

        #deletedata_button
        self.deletedata_button = QtWidgets.QPushButton(main_window)
        self.deletedata_button.setGeometry(QtCore.QRect(10, 450, 181, 55))
        self.deletedata_button.setToolTip("Delete Password")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deletedata_button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deletedata_button.setIcon(icon1)
        self.deletedata_button.setAutoDefault(False)
        self.deletedata_button.setDefault(True)
        self.deletedata_button.setFlat(False)
        self.deletedata_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deletedata_button.setStyleSheet("border :3px solid orange ;" "color:white ;")
        self.deletedata_button.setObjectName("deletedata_button")

        #welcome_label
        self.welcome_label = QtWidgets.QLabel(main_window)
        self.welcome_label.setGeometry(QtCore.QRect(170, 40, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("selection-color: rgb(170, 0, 255);\n" "color: rgb(255, 85, 0);")
        self.welcome_label.setScaledContents(False)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setWordWrap(True)
        self.welcome_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.welcome_label.setObjectName("welcome_label")

        #getdata_button
        self.getdata_button = QtWidgets.QPushButton(main_window)
        self.getdata_button.setGeometry(QtCore.QRect(200, 450, 161, 55))
        self.getdata_button.setToolTip("Show Passwords")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.getdata_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/idea.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getdata_button.setIcon(icon2)
        self.getdata_button.setIconSize(QtCore.QSize(30, 30))
        self.getdata_button.setAutoDefault(True)
        self.getdata_button.setDefault(False)
        self.getdata_button.setFlat(False)
        self.getdata_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.getdata_button.setStyleSheet("border :3px solid orange ;" "color:white ;")
        self.getdata_button.setObjectName("getdata_button")

        #user_button
        self.user_button = QtWidgets.QPushButton(main_window)
        self.user_button.setGeometry(QtCore.QRect(10, 30, 131, 101))

        if gender == 'M':
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("resources/man.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.user_button.setIcon(icon4)
        else:
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("resources/girl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.user_button.setIcon(icon4)

        self.user_button.setToolTip("Switch User")
        self.user_button.setIconSize(QtCore.QSize(71, 81))
        self.user_button.setFlat(True)
        self.user_button.setStyleSheet("border : 2px solid #FFFFFF ;" "color: #FFFFFF ;")
        self.user_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_button.setObjectName("user_button")

        #retranslateUi Call
        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        #Button Connection
        self.encryptdata_button.clicked.connect(self.getdata)
        self.getdata_button.clicked.connect(self.senddata)
        self.getpass_screen.close_button.clicked.connect(self.getDialog.close)
        self.user_button.clicked.connect(self.changeuser)
        self.showpassword_button.clicked.connect(self.show_password)
        self.deletedata_button.clicked.connect(self.delaccountDialog.show)
        self.delaccount_screen.ok_button.clicked.connect(self.delaccount)
        self.delaccount_screen.cancel_button.clicked.connect(self.delaccountDialog.close)

    #Function
    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Password Protector"))
        self.accountname_label.setText(_translate("main_window", "Account Name *"))
        self.accountname_lineedit.setPlaceholderText(_translate("main_window", "e. g. Facebook"))
        self.username_label.setText(_translate("main_window", "User Name *"))
        self.username_lineedit.setPlaceholderText(_translate("main_window", "example@mail.com | example | 91****"))
        self.password_label.setText(_translate("main_window", "Password *"))
        self.password_lineedit.setPlaceholderText(_translate("main_window", "Password"))
        self.encryptdata_button.setText(_translate("main_window", "Encrypt"))
        self.deletedata_button.setText(_translate("main_window", "Remove Account"))
        self.welcome_label.setText(_translate("main_window", "Welcome to Password Protector!"))
        self.getdata_button.setText(_translate("main_window", "Get Password"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionGetpassword.setText(_translate("MainWindow", "Get Password"))
        self.actionGetpassword.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuit.setText(_translate("MainWindow","Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

    #Function
    def delaccount(self):
        accountname = self.delaccount_screen.accountname_lineedit.text()
        username = self.delaccount_screen.username_lineedit.text()

        if accountname != '' and username != '' :
            accountname = accountname[0].upper() + accountname[1:]
            dbroot = sqlite3.connect('file:C:/Users/Public/Passwordprotector/main.db?mode=rw', uri=True)
            dbcursor = dbroot.cursor()
            dbcursor.execute("SELECT username, acntname, usrname FROM saveddata WHERE username = '"+mainuser+"'and acntname = '"+accountname+"' and usrname = '"+username+"' ;")
            record = dbcursor.fetchone()

            if record != None:
                dbcursor.execute("DELETE FROM saveddata WHERE username = '"+mainuser+"'and acntname = '"+accountname+"' and usrname = '"+username+"' ;")
                dbroot.commit()
                dbroot.close()
                msg = QMessageBox()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.setIcon(QMessageBox.Information)
                msg.setText("Deleted Successfully!")
                msg.setWindowTitle("Done")
                msg.exec_()
                self.delaccount_screen.username_lineedit.clear()
                self.delaccount_screen.accountname_lineedit.clear()
                self.delaccountDialog.close()

            else:
                msg = QMessageBox()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Account Name or Username not Exists!")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            msg = QMessageBox()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("All Fields are Required!")
            msg.setWindowTitle("Error")
            msg.exec_()

    #Function
    def show_password(self):

        if self.showpassword_button.isChecked():
            self.password_lineedit.setEchoMode(QtWidgets.QLineEdit.Normal)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/blind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.showpassword_button.setIcon(icon)

        else:
            self.password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.showpassword_button.setIcon(icon)

    #Function
    def changeuser(self):
        userselectDialog.show()
        main_window.close()

    #Function
    def encrypt(self,passwd,actname):
        lwrcase = string.ascii_lowercase
        uprcase = string.ascii_uppercase
        lenact = len(actname)*len(passwd)
        encrypt_passwd = ''
        for i in passwd:
            lwr = lwrcase.find(i)
            upr = uprcase.find(i)
            if i.isdigit():
                encrypt_passwd += str((int(i)+lenact)%10)
            elif lwr != -1:
                encrypt_passwd += str(lwrcase[(lwr+lenact)%26])
            elif upr != -1:
                encrypt_passwd += str(uprcase[(upr+lenact)%26])
            else:
                encrypt_passwd += str(i)

        return encrypt_passwd

    #Function
    def decrypt(self,result):
        lwrcase = string.ascii_lowercase
        uprcase = string.ascii_uppercase
        decrypt_passwd = ''
        decrypt_password = []
        for i in result:
            lenact = len(i[0])*len(i[2])
            for j in range(len(i[2])):
                lwr = lwrcase.find(i[2][j])
                upr = uprcase.find(i[2][j])
                if i[2][j].isdigit():
                    decrypt_passwd += str((int(i[2][j])-lenact)%10)
                elif lwr != -1:
                    decrypt_passwd += str(lwrcase[(lwr-lenact)%26])
                elif upr != -1:
                    decrypt_passwd += str(uprcase[(upr-lenact)%26])
                else:
                    decrypt_passwd += str(i[2][j])
            decrypt_password.append(decrypt_passwd)
            decrypt_passwd = ''


        return decrypt_password

    #Function
    def getdata(self):

        global mainuser
        actname = self.accountname_lineedit.text()
        usrname = self.username_lineedit.text()
        passwd = self.password_lineedit.text()
        if actname!='' and usrname!='' and passwd!='':
            dbroot = sqlite3.connect('file:C:/Users/Public/Passwordprotector/main.db?mode=rw', uri=True)
            actname = actname[0].upper() + actname[1:len(actname)]
            dbcursor = dbroot.cursor()
            dbcursor.execute("SELECT usrname FROM saveddata WHERE usrname = '"+usrname+"' and acntname = '"+actname+"';")
            record = dbcursor.fetchone()
            if record==None:
                encrypt_passwd = self.encrypt(passwd,actname)
                actname = str(actname)
                usrname = str(usrname)
                encrypt_passwd = str(encrypt_passwd)
                dbcursor.execute("INSERT INTO saveddata ('username', 'acntname', 'usrname', 'passwd') VALUES (?,?, ?, ?) ;",(mainuser, actname, usrname, encrypt_passwd))
                dbroot.commit()
                dbroot.close()
                self.accountname_lineedit.clear()
                self.username_lineedit.clear()
                self.password_lineedit.clear()
                msg = QMessageBox()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.setIcon(QMessageBox.Information)
                msg.setText("Saved Successfully!")
                msg.setWindowTitle("Done!")
                msg.exec_()

            else:
                msg = QMessageBox()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("All Ready Exists this username with account name")
                msg.setWindowTitle("Error")
                msg.exec_()
                self.password_lineedit.clear()

        else:
            msg = QMessageBox()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Fill All Fields!")
            msg.setWindowTitle("Error")
            msg.exec_()

        self.accountname_lineedit.setFocus()

    #Function
    def senddata(self):
        global mainuser
        dbroot = sqlite3.connect('file:C:/Users/Public/Passwordprotector/main.db?mode=rw', uri=True)
        dbcursor = dbroot.cursor()
        dbcursor.execute("SELECT acntname, usrname, passwd FROM saveddata WHERE username = '"+mainuser+"' ;")
        result = dbcursor.fetchall()
        decrypt_passwd = self.decrypt(result)
        j = 0
        self.getpass_screen.listall_listwidget.clear()

        for i in result:
            self.getpass_screen.listall_listwidget.addItem(str("Account Name: {0}".format(i[0])))
            self.getpass_screen.listall_listwidget.addItem(str("User Name: {0}".format(i[1])))
            self.getpass_screen.listall_listwidget.addItem(str("Password: {0}".format(decrypt_passwd[j])))
            j += 1
            self.getpass_screen.listall_listwidget.addItem(str("-------------------------------------------------"))

        self.getDialog.show()


class MovieSplashScreen(QSplashScreen):

    def __init__(self, movie, parent = None):

        movie.jumpToFrame(0)
        pixmap = QPixmap(movie.frameRect().size())

        QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        self.movie.start()

    def hideEvent(self, event):
        self.movie.stop()

    def paintEvent(self, event):

        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)

    def sizeHint(self):
        return self.movie.scaledSize()


#Main Code
if __name__ == "__main__":

    #Importing Modules/Files
    import os, gc, subprocess

    mainuser = ''
    gender = ''

    try:
        dbroot = sqlite3.connect('file:C:/Users/Public/Passwordprotector/main.db?mode=rw', uri=True)
        dbroot.close()
    except:
        path = 'C:/Users/Public/Passwordprotector'
        try:
            os.mkdir(path)
            subprocess.check_call(["attrib","+H","C:/Users/Public/Passwordprotector"])
        except:
            pass
        dbroot = sqlite3.connect('C:/Users/Public/Passwordprotector/main.db')
        subprocess.check_call(["attrib","+H","C:/Users/Public/Passwordprotector/main.db"])
        dbcursor = dbroot.cursor()
        dbcursor.execute("CREATE TABLE saveddata (username CHAR NOT NULL,acntname CHAR NOT NULL,usrname CHAR NOT NULL,passwd CHAR NOT NULL);")
        dbcursor.execute("CREATE TABLE user (username CHAR NOT NULL PRIMARY KEY,passwd CHAR NOT NULL,gender CHAR NOT NULL);")
        dbroot.commit()
        dbroot.close()

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    movie = QMovie("resources/lock.gif")
    splash = MovieSplashScreen(movie)
    splash.show()
    start = time.time()
    while movie.state() == QMovie.Running and time.time() < start + 2:
        app.processEvents()

    #Function
    def setui():

        dbroot = sqlite3.connect('file:C:/Users/Public/Passwordprotector/main.db?mode=rw', uri=True)
        dbcursor = dbroot.cursor()
        dbcursor.execute("SELECT username FROM user ;")
        result = dbcursor.fetchall()
        userselect_screen.userpassword_lineedit.clear()
        userselect_screen.userselect_combobox.clear()
        userselect_screen.userselect_combobox.addItem("")
        userselect_screen.userselect_combobox.setItemText(0, "SELECT USER")

        for user in result:
            userselect_screen.userselect_combobox.addItem(user[0])
        dbroot.close()

    userselectDialog = QtWidgets.QMainWindow()
    userselect_screen = userselect()
    userselect_screen.setupUi(userselectDialog)
    setui()
    userselectDialog.show()
    splash.finish(userselectDialog)

    newuserDialog = QtWidgets.QMainWindow()
    newuser_screen = newuser()
    newuser_screen.setupUi(newuserDialog)

    deluserDialog = QtWidgets.QMainWindow()
    deluser_screen = deluser()
    deluser_screen.setupUi(deluserDialog)

    #Function
    def getuser():

        global mainuser, gender
        username = userselect_screen.userselect_combobox.currentText()
        decrypt_passwd = userselect_screen.userpassword_lineedit.text()

        if username!="SELECT USER" and decrypt_passwd != '':
            passwd = ui.encrypt(decrypt_passwd, username)
            dbroot = sqlite3.connect('file:C:/Users/Public/Passwordprotector/main.db?mode=rw', uri=True)
            dbcursor = dbroot.cursor()
            mainuser = username
            dbcursor.execute("SELECT * FROM user WHERE username = '"+username+"' and passwd = '"+passwd+"' ;")
            result = dbcursor.fetchone()

            if result == None:
                msg = QMessageBox()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Incorrect Password")
                msg.setWindowTitle("Error")
                msg.exec_()
                dbroot.close()

            else:
                gender = result[2]
                dbroot.close()
                gc.collect()
                ui.setupUi(main_window)
                userselect_screen.userpassword_lineedit.clear()
                main_window.show()
                userselectDialog.close()

        else:
            msg = QMessageBox()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("All Fields are Required!")
            msg.setWindowTitle("Error")
            msg.exec_()

    #Function
    def adduser():

        username = newuser_screen.name_lineedit.text()
        password = newuser_screen.password_lineedit.text()
        gender = ''

        if newuser_screen.male_radiobutton.isChecked():
            gender = 'M'

        elif newuser_screen.female_radiobutton.isChecked():
            gender = 'W'

        if username != '' and password != '' and gender != '':
            encrypt_password = ui.encrypt(password, username)
            dbroot = sqlite3.connect('file:C:/Users/Public/Passwordprotector/main.db?mode=rw', uri=True)
            dbcursor = dbroot.cursor()
            dbcursor.execute("SELECT username, gender FROM user WHERE username = '"+username+"' ; ")
            record = dbcursor.fetchone()

            if record == None:
                username = username[0].upper() +username[1:]
                dbcursor.execute("INSERT INTO user ('username', 'passwd', 'gender') VALUES (?, ?, ?) ;",(username, encrypt_password, gender))
                dbroot.commit()
                dbroot.close()
                msg = QMessageBox()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.setIcon(QMessageBox.Information)
                msg.setText("New Account Added!")
                msg.setWindowTitle("Done")
                msg.exec_()
                setui()
                newuser_screen.password_lineedit.clear()
                newuserDialog.close()

            else:
                msg = QMessageBox()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Username Already Exists!")
                msg.setWindowTitle("Error")
                msg.exec_()
                newuser_screen.password_lineedit.clear()
        else:
            msg = QMessageBox()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("All Fields are Required!")
            msg.setWindowTitle("Error")
            msg.exec_()
            newuser_screen.password_lineedit.clear()

    #Function
    def show():

        if newuser_screen.password_show_button.isChecked():
            newuser_screen.password_lineedit.setEchoMode(QtWidgets.QLineEdit.Normal)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/blind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            newuser_screen.password_show_button.setIcon(icon)

        else:
            newuser_screen.password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            newuser_screen.password_show_button.setIcon(icon)

    #Function
    def showpassword():

        if userselect_screen.password_button.isChecked():
            userselect_screen.userpassword_lineedit.setEchoMode(QtWidgets.QLineEdit.Normal)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/blind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            userselect_screen.password_button.setIcon(icon)

        else:
            userselect_screen.userpassword_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            userselect_screen.password_button.setIcon(icon)

    #Function
    def deleteuser():

        username = deluser_screen.username_lineedit.text()
        password = deluser_screen.password_lineedit.text()

        if username != '' and password != '' :
            username = username[0].upper() + username[1:]
            passwd = ui.encrypt(password, username)
            dbroot = sqlite3.connect('file:C:/Users/Public/Passwordprotector/main.db?mode=rw', uri=True)
            dbcursor = dbroot.cursor()
            dbcursor.execute("SELECT * FROM user WHERE username = '"+username+"' and passwd = '"+passwd+"' ;")
            record = dbcursor.fetchone()

            if record != None:
                dbcursor.execute("DELETE FROM user WHERE username = '"+username+"' and passwd = '"+passwd+"' ;")
                dbcursor.execute("DELETE FROM saveddata WHERE username = '"+username+"' ;")
                dbroot.commit()
                dbroot.close()
                setui()
                deluser_screen.username_lineedit.clear()
                deluser_screen.password_lineedit.clear()
                msg = QMessageBox()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.setIcon(QMessageBox.Information)
                msg.setText("User Deleted Successfully!")
                msg.setWindowTitle("Done")
                msg.exec_()
                deluserDialog.close()

            else:
                dbroot.close()
                deluser_screen.password_lineedit.clear()
                msg = QMessageBox()
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg.setWindowIcon(icon)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Incorrect Username or Password!")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            deluser_screen.password_lineedit.clear()
            msg = QMessageBox()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("All Fields are Required!")
            msg.setWindowTitle("Error")
            msg.exec_()


    gc.collect()

    #Dialogs
    userselect_screen.ok_button.clicked.connect(getuser)
    userselect_screen.newuser_button.clicked.connect(newuserDialog.show)
    userselect_screen.quit_button.clicked.connect(sys.exit)
    userselect_screen.password_button.clicked.connect(showpassword)
    userselect_screen.deleteuser_button.clicked.connect(deluserDialog.show)
    newuser_screen.ok_button.clicked.connect(adduser)
    newuser_screen.cancel_button.clicked.connect(newuserDialog.close)
    newuser_screen.password_show_button.clicked.connect(show)
    deluser_screen.delete_button.clicked.connect(deleteuser)
    deluser_screen.cancel_button.clicked.connect(deluserDialog.close)

    #Exit
    sys.exit(app.exec_())