from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UI import Ui_itcomputer


class itcom(QMainWindow, Ui_itcomputer.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_0.clicked.connect(
            lambda: self.push(self.pushButton_0.text()))
        self.pushButton_1.clicked.connect(
            lambda: self.push(self.pushButton_1.text()))
        self.pushButton_2.clicked.connect(
            lambda: self.push(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(
            lambda: self.push(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(
            lambda: self.push(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(
            lambda: self.push(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(
            lambda: self.push(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(
            lambda: self.push(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(
            lambda: self.push(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(
            lambda: self.push(self.pushButton_9.text()))
        self.pushButton_left.clicked.connect(
            lambda: self.push(self.pushButton_left.text()))
        self.pushButton_right.clicked.connect(
            lambda: self.push(self.pushButton_right.text()))
        
        self.Button_dengyu.clicked.connect(self.result)
        self.Button_clear.clicked.connect(self.clear)

    def push(self, s):
        str0 = self.textEdit.toPlainText()
        self.textEdit.setText(str0 + s)

    def result(self):
        
        try:
            
            b = self.textEdit.toPlainText()
            s = eval(b)
            a = self.comboBox.currentText()
            if a == '2':
                self.textEdit_2.setText(str(bin(s)))
                print(2)
            elif a == '8':
                self.textEdit_2.setText(str(oct(s)))
                print(8)
            elif a == '16':
                self.textEdit_2.setText(str(hex(s)))
                print(16)
            elif a == '10':
                self.textEdit_2.setText(str(s))
            self.clear()
        except Exception:
            if self.textEdit.toPlainText() == '':
                # QMessageBox.critical(self, '提示', '请先输入数字!')
                self.clear()
            else:            
                QMessageBox.critical(self, '错误', '输入有误!')
            self.clear()
    
    def clear(self):
        self.textEdit.setText('')
