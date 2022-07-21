import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow
from operator import add, sub, mul, truediv
from decimal import *

operations = {
    '+': add,
    '-': sub,
    "*": mul,
    "/": truediv
}

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lbl_temp.clear()

        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))

        self.ui.btn_clr.clicked.connect(self.clr_all)
        self.ui.btn_point.clicked.connect(self.add_point)
        self.ui.btn_back.clicked.connect(self.backspace)
        self.ui.btn_abs.clicked.connect(self.ent_abs)
        
        self.ui.btn_is.clicked.connect(lambda: self.calculate())   
        self.ui.btn_add.clicked.connect(lambda: self.math_operation('+'))
        self.ui.btn_sub.clicked.connect(lambda: self.math_operation('-'))
        self.ui.btn_div.clicked.connect(lambda: self.math_operation('/'))
        self.ui.btn_mul.clicked.connect(lambda: self.math_operation('*'))

    def clr_error(self):
        entry = self.ui.lbl_ent.text()
        if entry == "На ноль делить нельзя!":
            self.ui.lbl_ent.setText('0')


    def del_temp_if_next_btn(self):
        if self.get_math_sign() == '=':
            self.ui.lbl_temp.clear()

    def add_digit(self, btn_text: str):
        self.clr_error()
        self.del_temp_if_next_btn()
        if self.ui.lbl_ent.text() == '0':
            self.ui.lbl_ent.setText(btn_text)
        else:
            self.ui.lbl_ent.setText(self.ui.lbl_ent.text() + btn_text)
    
    def clr_all(self):
        self.clr_error()
        self.ui.lbl_ent.setText('0')
        self.ui.lbl_temp.clear()

    def add_point(self):
        self.del_temp_if_next_btn()
        if '.' not in self.ui.lbl_ent.text():
            self.ui.lbl_ent.setText(self.ui.lbl_ent.text() + '.')
    
    def add_temp(self, math_sign: str):
        self.del_temp_if_next_btn()
        if not self.ui.lbl_temp.text():
            self.ui.lbl_temp.setText(self.remove_trailing_zeros(self.ui.lbl_ent.text()) + f' {math_sign} ')
            self.ui.lbl_ent.setText('0')

    @staticmethod
    def remove_trailing_zeros(num: str):
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n
    
    def get_entry_num(self):
        entry = self.ui.lbl_ent.text().strip('.')
        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self):
        if self.ui.lbl_temp.text():
            temp = self.ui.lbl_temp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)
    
    def get_math_sign(self):
        if self.ui.lbl_temp.text():
            return self.ui.lbl_temp.text().strip('.').split()[-1]
    
    def calculate(self):
        entry = self.ui.lbl_ent.text()
        temp = self.ui.lbl_temp.text()
        try:
            if temp:
                result = self.remove_trailing_zeros(str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num())))
                self.ui.lbl_temp.setText(temp + self.remove_trailing_zeros(entry) + ' =')
                self.ui.lbl_ent.setText(result)
                return result
        except KeyError:
            pass
        except ZeroDivisionError:
            self.ui.lbl_ent.setText("На ноль делить нельзя!")
            
    def math_operation(self, math_sign: str):
        temp = self.ui.lbl_temp.text()
        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sign() != math_sign:
                if self.get_math_sign() == '=':
                    self.add_temp(math_sign)
                else:
                    self.ui.lbl_temp.setText(temp[:-2] + f'{math_sign}')
            else:
                self.ui.lbl_temp.setText(self.calculate() + f'{math_sign}')
    
    def backspace(self):
        self.clr_error()
        self.del_temp_if_next_btn()
        entry = self.ui.lbl_ent.text()
        if len(entry) < 2 or (len(entry) == 1 and '-' in entry) or (entry == "На ноль делить нельзя!"):
            self.ui.lbl_ent.setText('0')
        else:
            self.ui.lbl_ent.setText(entry[:-1])
    
    def ent_abs(self):
        self.del_temp_if_next_btn()
        entry = self.ui.lbl_ent.text()
        if '-' in entry:
            entry = entry[1:]
        else:
            if entry != '0':
                entry = '-' + entry
        self.ui.lbl_ent.setText(entry)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())