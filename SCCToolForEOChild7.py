# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SCCToolForEOChild7.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SCC_Dialog7(object):
    def setupUi(self, SCC_Dialog7):
        SCC_Dialog7.setObjectName("SCC_Dialog7")
        SCC_Dialog7.resize(779, 283)
        self.textBrowser = QtWidgets.QTextBrowser(SCC_Dialog7)
        self.textBrowser.setGeometry(QtCore.QRect(40, 130, 441, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget = QtWidgets.QWidget(SCC_Dialog7)
        self.layoutWidget.setGeometry(QtCore.QRect(510, 80, 183, 137))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Yes = QtWidgets.QCommandLinkButton(self.layoutWidget)
        self.Yes.setStyleSheet("")
        self.Yes.setObjectName("Yes")
        self.verticalLayout.addWidget(self.Yes)
        self.No = QtWidgets.QCommandLinkButton(self.layoutWidget)
        self.No.setObjectName("No")
        self.verticalLayout.addWidget(self.No)

        self.retranslateUi(SCC_Dialog7)
        QtCore.QMetaObject.connectSlotsByName(SCC_Dialog7)

    def retranslateUi(self, SCC_Dialog7):
        _translate = QtCore.QCoreApplication.translate
        SCC_Dialog7.setWindowTitle(_translate("SCC_Dialog7", "Dialog"))
        self.textBrowser.setHtml(_translate("SCC_Dialog7", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; font-size:16pt; font-weight:600; color:#008080;\">ECU</span><span style=\" font-family:\'宋体\',\'monospace\'; font-size:16pt; font-weight:600; color:#008080;\">配置字是否有变更？</span></p></body></html>"))
        self.Yes.setText(_translate("SCC_Dialog7", "Yes"))
        self.No.setText(_translate("SCC_Dialog7", "No"))
