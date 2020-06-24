from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newuser_window(object):
    def setupUi(self, newuser_window):
        newuser_window.setObjectName("newuser_window")
        newuser_window.resize(464, 361)
        newuser_window.setMinimumSize(464, 361)
        newuser_window.setMaximumSize(464, 361)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        newuser_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        newuser_window.setWindowIcon(icon)
        self.name_label = QtWidgets.QLabel(newuser_window)
        self.name_label.setGeometry(QtCore.QRect(30, 70, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setScaledContents(False)
        self.name_label.setObjectName("name_label")

        self.name_lineedit = QtWidgets.QLineEdit(newuser_window)
        self.name_lineedit.setGeometry(QtCore.QRect(190, 90, 221, 20))
        self.name_lineedit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.name_lineedit.setFocus()
        self.name_lineedit.setObjectName("name_lineedit")

        self.password_label = QtWidgets.QLabel(newuser_window)
        self.password_label.setGeometry(QtCore.QRect(30, 130, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")

        self.password_lineedit = QtWidgets.QLineEdit(newuser_window)
        self.password_lineedit.setGeometry(QtCore.QRect(190, 140, 221, 20))
        self.password_lineedit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineedit.setObjectName("password_lineedit")

        self.male_radiobutton = QtWidgets.QRadioButton(newuser_window)
        self.male_radiobutton.setGeometry(QtCore.QRect(40, 200, 61, 18))
        self.male_radiobutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.male_radiobutton.setObjectName("male_radiobutton")

        self.female_radiobutton = QtWidgets.QRadioButton(newuser_window)
        self.female_radiobutton.setGeometry(QtCore.QRect(110, 200, 71, 18))
        self.female_radiobutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.female_radiobutton.setObjectName("female_radiobutton")

        self.password_show_button = QtWidgets.QPushButton(newuser_window)
        self.password_show_button.setGeometry(QtCore.QRect(420, 140, 31, 20))
        self.password_show_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password_show_button.setCheckable(True)
        self.password_show_button.setDefault(True)
        self.password_show_button.setToolTip("Show/Hide Password")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.password_show_button.setIcon(icon1)
        self.password_show_button.setIconSize(QtCore.QSize(31, 20))
        self.password_show_button.setFlat(True)
        self.password_show_button.setObjectName("password_show_button")

        self.ok_button = QtWidgets.QPushButton(newuser_window)
        self.ok_button.setGeometry(QtCore.QRect(250, 280, 85, 26))
        self.ok_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")

        self.cancel_button = QtWidgets.QPushButton(newuser_window)
        self.cancel_button.setGeometry(QtCore.QRect(150, 280, 85, 26))
        self.cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_button.setDefault(True)
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(newuser_window)
        QtCore.QMetaObject.connectSlotsByName(newuser_window)

    def retranslateUi(self, newuser_window):
        _translate = QtCore.QCoreApplication.translate
        newuser_window.setWindowTitle(_translate("newuser_window", "Password Protector"))
        self.name_label.setText(_translate("newuser_window", "Name"))
        self.name_lineedit.setPlaceholderText(_translate("newuser_window", "New Username"))
        self.password_label.setText(_translate("newuser_window", "Password"))
        self.password_lineedit.setPlaceholderText(_translate("newuser_window", "New Password"))
        self.male_radiobutton.setText(_translate("newuser_window", "Male"))
        self.female_radiobutton.setText(_translate("newuser_window", "Female"))
        self.ok_button.setText(_translate("newuser_window", "Ok"))
        self.cancel_button.setText(_translate("newuser_window", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newuser_window = QtWidgets.QWidget()
    ui = Ui_newuser_window()
    ui.setupUi(newuser_window)
    newuser_window.show()
    sys.exit(app.exec_())
