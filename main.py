from PyQt5.QtWidgets import QApplication
import sys
import diaoyong
import computer
import sencomputer
import itcomputer
# 测试git
if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = computer.com()
    senwin = sencomputer.sencom()
    itwin = itcomputer.itcom()
    win.show()
    a = diaoyong.diaowin()

    win.pushButton_sen.clicked.connect(lambda: a.senshow(senwin, win))
    senwin.pushButton_back.clicked.connect(lambda: a.show(win, senwin))
    win.pushButton_it.clicked.connect(lambda: a.itshow(win, itwin))
    itwin.pushButton_back.clicked.connect(lambda: a.show2(win, itwin))
    app.exec_()
