import sys
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import SCCToolForEO
import SCCToolForEOChild1
import SCCToolForEOChild2
import SCCToolForEOChild3
import SCCToolForEOChild4
import SCCToolForEOChild5
import SCCToolForEOChild6
import SCCToolForEOChild7



if __name__ == '__main__':
    ALT1 ="SW需要更换零件号 "
    ALT2 ="DU需要更换零件号 "
    ALT3 ="DU不需要更换零件号 "
    ALT4 ="800 POS需要新申请；生产车辆需要断点；售后车辆需要更改结构周 "
    ALT5 ="HWSD需要更换零件号 "
    ALT6 ="新软件需要立即导入售后 "
    ALT7 ="DU和HWSD都不需要更换零件号 "
    ALT8 ="ECU Node需要新申请 "
    ALT9 ="售后车辆需要更新配置字 "
    Result = []



    def GoClick(self):
        Result.clear()
        MainWindow.close()
        UI1.setupUi(Childwindow1)
        Childwindow1.show()
        UI1.SWUpdate.clicked.connect(UI1SWupdat)
        UI1.HWUpdate.clicked.connect(UI1HWupdat)
        UI1.SWAndHWUpdate.clicked.connect(UI1SWAndHWUpdate)




    def UI1SWupdat(self):
        Childwindow1.close()
        UI2.setupUi(Childwindow2)
        Childwindow2.show()
        UI2.preload.clicked.connect(UI2Preload)
        UI2.EOL.clicked.connect(UI2EOL)
        UI2.PreloadAndEol.clicked.connect(UI2PreloadAndEOL)


    def UI1HWupdat(self):
        Childwindow1.close()
        UI4.setupUi(Childwindow4)
        Childwindow4.show()
        Result.append(ALT5 + ALT2)
        UI4.Yes.clicked.connect(UI4Yes)
        UI4.No.clicked.connect(UI4No)




    def UI1SWAndHWUpdate(self):
        Childwindow1.close()
        UI5.setupUi(Childwindow5)
        Childwindow5.show()
        Result.append(ALT5+ALT2+ALT1)
        UI5.Yes.clicked.connect(UI5Yes)
        UI5.No.clicked.connect(UI5No)


    def UI2Preload(self):
        Childwindow2.close()
        UI3.setupUi(Childwindow3)
        Childwindow3.show()
        Result.append(ALT2+ALT1)
        UI3.No.clicked.connect(UI3No)
        UI3.Yes.clicked.connect(UI3Yes)


    def UI2EOL(self):
        Childwindow2.close()
        UI3.setupUi(Childwindow3)
        Childwindow3.show()
        Result.append(ALT1)
        UI3.No.clicked.connect(UI3No)
        UI3.Yes.clicked.connect(UI3Yes)


    def UI2PreloadAndEOL(self):
        Childwindow2.close()
        UI3.setupUi(Childwindow3)
        Childwindow3.show()
        Result.append(ALT2+ALT1)
        UI3.No.clicked.connect(UI3No)
        UI3.Yes.clicked.connect(UI3Yes)


    def UI3Yes(self):
        Childwindow3.close()
        UI6.setupUi(Childwindow6)
        Childwindow6.show()
        UI6.No.clicked.connect(UI6No)
        UI6.Yes.clicked.connect(UI6Yes)


    def UI3No(self):
        Childwindow3.close()
        UI6.setupUi(Childwindow6)
        Childwindow6.show()
        Result.append(ALT4)
        UI6.No.clicked.connect(UI6No)
        UI6.Yes.clicked.connect(UI6Yes)

    def UI4Yes(self):
        Childwindow4.close()
        UI6.setupUi(Childwindow6)
        Childwindow6.show()
        UI6.No.clicked.connect(UI6No)
        UI6.Yes.clicked.connect(UI6Yes)


    def UI4No(self):
        Childwindow4.close()
        UI6.setupUi(Childwindow6)
        Childwindow6.show()
        Result.append(ALT6)

        UI6.No.clicked.connect(UI6No)
        UI6.Yes.clicked.connect(UI6Yes)


    def UI5Yes(self):
        Childwindow5.close()
        UI6.setupUi(Childwindow6)
        Childwindow6.show()
        UI6.No.clicked.connect(UI6No)
        UI6.Yes.clicked.connect(UI6Yes)



    def UI5No(self):
        Childwindow5.close()
        UI6.setupUi(Childwindow6)
        Childwindow6.show()
        Result.append(ALT6)

        UI6.No.clicked.connect(UI6No)
        UI6.Yes.clicked.connect(UI6Yes)


    def UI6Yes(self):
        Result.append(ALT8)
        Childwindow6.close()
        UI7.setupUi(Childwindow7)
        Childwindow7.show()
        UI7.No.clicked.connect(UI7No)
        UI7.Yes.clicked.connect(UI7Yes)


    def UI6No(self):
        Childwindow6.close()
        UI7.setupUi(Childwindow7)
        Childwindow7.show()
        UI7.No.clicked.connect(UI7No)
        UI7.Yes.clicked.connect(UI7Yes)


    def UI7Yes(self):
        Childwindow7.close()
        UI.setupUi(MainWindow)
        Result.append(ALT9)
        UI.textBrowser.setText(str(Result))
        print(Result)
        MainWindow.show()
        UI.GO.clicked.connect(GoClick)
        UI.exit.clicked.connect(sys.exit)

    def UI7No(self):
        Childwindow7.close()
        UI.setupUi(MainWindow)
        UI.textBrowser.setText(str(Result))
        print( Result )
        MainWindow.show()
        UI.GO.clicked.connect(GoClick)
        UI.exit.clicked.connect(sys.exit)


    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    Childwindow1 = QMainWindow()
    Childwindow2 = QMainWindow()
    Childwindow3 = QMainWindow()
    Childwindow4 = QMainWindow()
    Childwindow5 = QMainWindow()
    Childwindow6 = QMainWindow()
    Childwindow7 = QMainWindow()

    UI= SCCToolForEO.Ui_SCC_MainWindow()
    UI1 = SCCToolForEOChild1.Ui_SCC_Dialog1()
    UI2 = SCCToolForEOChild2.Ui_SCC_Dialog2()
    UI3 = SCCToolForEOChild3.Ui_SCC_Dialog3()
    UI4 = SCCToolForEOChild4.Ui_SCC_Dialog4()
    UI5 = SCCToolForEOChild5.Ui_SCC_Dialog5()
    UI6 = SCCToolForEOChild6.Ui_SCC_Dialog6()
    UI7 = SCCToolForEOChild7.Ui_SCC_Dialog7()



    UI.setupUi(MainWindow)
    MainWindow.show()
    UI.GO.clicked.connect(GoClick)
    UI.exit.clicked.connect(sys.exit)


    sys.exit(app.exec_())
