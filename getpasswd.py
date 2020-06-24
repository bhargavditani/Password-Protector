from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_getpasswd_window(object):
    def setupUi(self, getpasswd_window):
        getpasswd_window.setObjectName("getpasswd_window")
        getpasswd_window.resize(393, 395)
        getpasswd_window.setMinimumSize(393, 395)
        getpasswd_window.setMaximumSize(393, 395)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        getpasswd_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        getpasswd_window.setWindowIcon(icon)
        self.listall_listwidget = QtWidgets.QListWidget(getpasswd_window)
        self.listall_listwidget.setGeometry(QtCore.QRect(0, 0, 391, 351))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.listall_listwidget.setFont(font)
        self.listall_listwidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listall_listwidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listall_listwidget.setTabKeyNavigation(False)
        self.listall_listwidget.setObjectName("listall_listwidget")

        self.close_button = QtWidgets.QPushButton(getpasswd_window)
        self.close_button.setGeometry(QtCore.QRect(160, 360, 85, 26))
        self.close_button.setAutoDefault(True)
        self.close_button.setDefault(True)
        self.close_button.setFlat(False)
        self.close_button.setFocus()
        self.close_button.setObjectName("close_button")

        self.retranslateUi(getpasswd_window)
        QtCore.QMetaObject.connectSlotsByName(getpasswd_window)

    def retranslateUi(self, getpasswd_window):
        _translate = QtCore.QCoreApplication.translate
        getpasswd_window.setWindowTitle(_translate("getpasswd_window", "Password Protector"))
        #self.listall_listwidget.setSortingEnabled(True)
        self.close_button.setText(_translate("getpasswd_window", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    getpasswd_window = QtWidgets.QWidget()
    ui = Ui_getpasswd_window()
    ui.setupUi(getpasswd_window)
    getpasswd_window.show()
    sys.exit(app.exec_())
