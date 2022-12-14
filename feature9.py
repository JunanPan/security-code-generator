# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feature9.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import random


class Ui_window_feature9(object):
    def setupUi(self, window_feature9):
        window_feature9.setObjectName("window_feature9")
        window_feature9.resize(510, 600)
        self.label_title = QtWidgets.QLabel(window_feature9)
        self.label_title.setGeometry(QtCore.QRect(130, 130, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_tip = QtWidgets.QLabel(window_feature9)
        self.label_tip.setGeometry(QtCore.QRect(80, 330, 221, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_tip.setFont(font)
        self.label_tip.setObjectName("label_tip")
        self.lineEdit_codenum = QtWidgets.QLineEdit(window_feature9)
        self.lineEdit_codenum.setGeometry(QtCore.QRect(310, 330, 120, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_codenum.setFont(font)
        self.lineEdit_codenum.setObjectName("lineEdit_codenum")
        self.pushButton_create = QtWidgets.QPushButton(window_feature9)
        self.pushButton_create.setGeometry(QtCore.QRect(205, 390, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_select = QtWidgets.QPushButton(window_feature9)
        self.pushButton_select.setGeometry(QtCore.QRect(195, 270, 120, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_select.setFont(font)
        self.pushButton_select.setObjectName("pushButton_select")
        self.label_tip_2 = QtWidgets.QLabel(window_feature9)
        self.label_tip_2.setGeometry(QtCore.QRect(330, 280, 170, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label_tip_2.setFont(font)
        self.label_tip_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_tip_2.setText("")
        self.label_tip_2.setObjectName("label_tip_2")
        self.label_tip_3 = QtWidgets.QLabel(window_feature9)
        self.label_tip_3.setGeometry(QtCore.QRect(120, 210, 260, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_tip_3.setFont(font)
        self.label_tip_3.setObjectName("label_tip_3")
        self.label_tip_4 = QtWidgets.QLabel(window_feature9)
        self.label_tip_4.setGeometry(QtCore.QRect(60, 180, 390, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_tip_4.setFont(font)
        self.label_tip_4.setObjectName("label_tip_4")

        # 选择文件
        self.filename = ""
        self.pushButton_select.clicked.connect(lambda: self.select_file(window_feature9))
        # 生成
        self.pushButton_create.clicked.connect(lambda: self.create())

        self.retranslateUi(window_feature9)
        QtCore.QMetaObject.connectSlotsByName(window_feature9)

    def retranslateUi(self, window_feature9):
        _translate = QtCore.QCoreApplication.translate
        window_feature9.setWindowTitle(_translate("window_feature9", "Form"))
        self.label_title.setText(_translate("window_feature9", "企业粉丝防伪码抽奖"))
        self.label_tip.setText(_translate("window_feature9", "请输入中奖用户数量:"))
        self.pushButton_create.setText(_translate("window_feature9", "抽奖"))
        self.pushButton_select.setText(_translate("window_feature9", "choose file"))
        self.label_tip_3.setText(_translate("window_feature9", "个ini文件中，并选择"))
        self.label_tip_4.setText(_translate("window_feature9", "提示：请将所有参与抽奖的防伪码汇总至一"))

    def select_file(self, window_feature5):
        directory = QtWidgets.QFileDialog.getOpenFileName(window_feature5, "选取文件", "./", "文本文件 (*.txt)、*.txt")  # 起始路径
        self.filename = directory[0]
        self.label_tip_2.setText("已选择" + self.filename.split('/')[-1])

    def create(self):
        # 打开用户防伪码存储文件，并存储防伪码
        user_scode = []
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                user_scode.append(line.strip('\n'))

        user_count_num = self.lineEdit_codenum.text()
        if int(user_count_num) == 0 or int(user_count_num) >= len(user_scode):
            QtWidgets.QMessageBox.warning(QtWidgets.QWidget(), "warning", "Quantity error！", QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)
        else:
            lucky_fans = random.sample(user_scode, int(user_count_num))
            tip_sentence = "Lucky code：\n"
            for i in range(len(lucky_fans) - 1):
                tip_sentence = tip_sentence + lucky_fans[i] + '\n'
            tip_sentence = tip_sentence + lucky_fans[-1]
            QtWidgets.QMessageBox.information(QtWidgets.QWidget(), "提示", tip_sentence, QtWidgets.QMessageBox.Yes,
                                              QtWidgets.QMessageBox.Yes)