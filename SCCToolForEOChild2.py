# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SCCToolForEOChild2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SCC_Dialog2(object):
    def setupUi(self, SCC_Dialog2):
        SCC_Dialog2.setObjectName("SCC_Dialog2")
        SCC_Dialog2.resize(779, 283)
        self.textBrowser = QtWidgets.QTextBrowser(SCC_Dialog2)
        self.textBrowser.setGeometry(QtCore.QRect(40, 130, 441, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget = QtWidgets.QWidget(SCC_Dialog2)
        self.layoutWidget.setGeometry(QtCore.QRect(510, 80, 183, 137))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.preload = QtWidgets.QCommandLinkButton(self.layoutWidget)
        self.preload.setStyleSheet("")
        self.preload.setObjectName("preload")
        self.verticalLayout.addWidget(self.preload)
        self.EOL = QtWidgets.QCommandLinkButton(self.layoutWidget)
        self.EOL.setObjectName("EOL")
        self.verticalLayout.addWidget(self.EOL)
        self.PreloadAndEol = QtWidgets.QCommandLinkButton(self.layoutWidget)
        self.PreloadAndEol.setObjectName("PreloadAndEol")
        self.verticalLayout.addWidget(self.PreloadAndEol)

        self.retranslateUi(SCC_Dialog2)
        QtCore.QMetaObject.connectSlotsByName(SCC_Dialog2)

    def retranslateUi(self, SCC_Dialog2):
        _translate = QtCore.QCoreApplication.translate
        SCC_Dialog2.setWindowTitle(_translate("SCC_Dialog2", "Dialog"))
        self.textBrowser.setHtml(_translate("SCC_Dialog2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'??????\',\'monospace\'; font-size:16pt; font-weight:600; color:#008080;\">???????????????????????????????????????</span></p></body></html>"))
        self.preload.setText(_translate("SCC_Dialog2", "Preload SW"))
        self.EOL.setText(_translate("SCC_Dialog2", "EOL"))
        self.PreloadAndEol.setText(_translate("SCC_Dialog2", "Preload and EOL"))
