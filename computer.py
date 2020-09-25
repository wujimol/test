from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UI import Ui_computer


class com(QMainWindow, Ui_computer.Ui_MainWindow):
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
        self.pushButton_sub.clicked.connect(
            lambda: self.push(self.pushButton_sub.text()))
        self.pushButton_minus.clicked.connect(
            lambda: self.push(self.pushButton_minus.text()))
        self.pushButton_mul.clicked.connect(
            lambda: self.push(self.pushButton_mul.text()))
        self.pushButton_div.clicked.connect(
            lambda: self.push(self.pushButton_div.text()))
        self.pushButton_dian.clicked.connect(
            lambda: self.push(self.pushButton_dian.text()))
        self.Button_dengyu.clicked.connect(self.result)
        self.Button_clear.clicked.connect(self.clear)
        self.pushButton_delete.clicked.connect(self.delete)

    def push(self, s):
        str0 = self.textEdit.toPlainText()
        self.textEdit.setText(str0 + s)

    def clear(self):
        self.textEdit.setText('')

    def result(self):

        try:
            a = self.textEdit.toPlainText()
            s = float(eval(a))
            self.textEdit_2.setText(str(s))
            self.clear()
        except Exception:
            if a == '':
                self.clear()
            else:
                QMessageBox.critical(self, '错误', '输入有误!')
                self.clear()

    def delete(self):
        a = self.textEdit.toPlainText()
        self.textEdit.setText(a[:-1])