from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_userselect_window(object):
    def setupUi(self, userselect_window):
        userselect_window.setObjectName("userselect_window")
        userselect_window.resize(466, 315)
        userselect_window.setMinimumSize(466, 315)
        userselect_window.setMaximumSize(466, 315)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        userselect_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        userselect_window.setWindowIcon(icon)

        self.userselect_combobox = QtWidgets.QComboBox(userselect_window)
        self.userselect_combobox.setGeometry(QtCore.QRect(120, 100, 231, 22))
        self.userselect_combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #self.userselect_combobox.setCurrentText("")
        self.userselect_combobox.setObjectName("userselect_combobox")

        self.userpassword_lineedit = QtWidgets.QLineEdit(userselect_window)
        self.userpassword_lineedit.setGeometry(QtCore.QRect(120, 170, 231, 21))
        self.userpassword_lineedit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.userpassword_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userpassword_lineedit.setObjectName("userpassword_lineedit")

        self.password_button = QtWidgets.QPushButton(userselect_window)
        self.password_button.setGeometry(QtCore.QRect(360, 170, 31, 21))
        self.password_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password_button.setCheckable(True)
        self.password_button.setToolTip("Show/Hide Password")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.password_button.setIcon(icon1)
        self.password_button.setIconSize(QtCore.QSize(31, 21))
        self.password_button.setDefault(True)
        self.password_button.setFlat(True)
        self.password_button.setObjectName("password_button")

        self.ok_button = QtWidgets.QPushButton(userselect_window)
        self.ok_button.setGeometry(QtCore.QRect(270, 220, 85, 26))
        self.ok_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")

        self.deleteuser_button = QtWidgets.QPushButton(userselect_window)
        self.deleteuser_button.setGeometry(QtCore.QRect(130, 220, 85, 26))
        self.deleteuser_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteuser_button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.deleteuser_button.setAutoDefault(True)
        self.deleteuser_button.setDefault(True)
        self.deleteuser_button.setObjectName("ok_button")

        self.newuser_button = QtWidgets.QPushButton(userselect_window)
        self.newuser_button.setGeometry(QtCore.QRect(270, 270, 85, 26))
        self.newuser_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newuser_button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.newuser_button.setDefault(True)
        self.newuser_button.setObjectName("newuser_button")

        self.quit_button = QtWidgets.QPushButton(userselect_window)
        self.quit_button.setGeometry(QtCore.QRect(130, 270, 85, 26))
        self.quit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quit_button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.quit_button.setDefault(True)
        self.quit_button.setObjectName("quit_button")

        self.retranslateUi(userselect_window)
        QtCore.QMetaObject.connectSlotsByName(userselect_window)

    def retranslateUi(self, userselect_window):
        _translate = QtCore.QCoreApplication.translate
        userselect_window.setWindowTitle(_translate("userselect_window", "Password Protector"))
        self.userpassword_lineedit.setPlaceholderText(_translate("userselect_window", "Password"))
        self.ok_button.setText(_translate("userselect_window", "Ok"))
        self.newuser_button.setText(_translate("userselect_window", "New USER"))
        self.deleteuser_button.setText(_translate("userselect_window", "Delete USER"))
        self.quit_button.setText(_translate("userselect_window", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userselect_window = QtWidgets.QWidget()
    ui = Ui_userselect_window()
    ui.setupUi(userselect_window)
    userselect_window.show()
    sys.exit(app.exec_())
