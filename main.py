import sys
from PyQt5 import QtWidgets

from window_main import Ui_window_main

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main_window = Ui_window_main()
    # admin_window = Ui_Window_admin()

    MainWindow_main_window = QtWidgets.QMainWindow()
    # MainWindow_admin_window = QtWidgets.QMainWindow()

    main_window.setupUi(MainWindow_main_window)
    # admin_window.setupUi(MainWindow_admin_window)

    MainWindow_main_window.show()
    # login_window.pushButton_login.clicked.connect(MainWindow_admin_window.show)

    app.exec_()
