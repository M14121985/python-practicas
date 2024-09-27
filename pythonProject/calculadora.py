import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QPushButton, QLineEdit,
)
from PyQt6.QtCore import Qt
from math import sin, cos, tan, log, exp, sqrt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora Avanzada')
        self.setGeometry(100, 100, 300, 400)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setMaxLength(15)

        grid = QGridLayout()
        grid.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'sqrt',
            'log', 'exp', '(', ')',
            'C', 'CE'
        ]

        row = 1
        col = 0
        for button_text in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.button_clicked)
            grid.addWidget(button, row, col, 1, 1)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.setLayout(grid)

    def button_clicked(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText('Error')
        elif button_text == 'C':
            self.display.clear()
        elif button_text == 'CE':
            self.display.setText(self.display.text()[:-1])
        elif button_text in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp']:
            self.display.setText(self.display.text() + button_text + '(')
        else:
            self.display.setText(self.display.text() + button_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())