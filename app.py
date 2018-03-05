import sys
from form import ValueLayout, RangoLayout
from table import ConditionTable
from plot import Canvas
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QHBoxLayout, 
    QVBoxLayout, QGroupBox, QMessageBox
)




class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modelacion")
        self.setMinimumSize(1000, 600)
        self.value_layout = ValueLayout()
        self.rango_layout = RangoLayout()
        self.table = ConditionTable()
        self.canvas = Canvas()
        self.btn = QPushButton("Graficar")
        self.btn.clicked.connect(self.plot)
        self.initUI()

    def plot(self):
        try: 
            self.collect()
            self.canvas.plot()
        except ValueError as e:
            QMessageBox.critical(self, 'Incorrecto', 'Campos de entrada no validos:\n{0}'.format(e))

    def collect(self):
        self.canvas.rango = int(self.rango_layout.rango_line.text())
        self.canvas.dw = int(self.value_layout.dw_line.text())
        self.canvas.d = int(self.value_layout.d_line.text())
        self.canvas.c = int(self.value_layout.c_line.text())
        self.canvas.s = int(self.value_layout.s_line.text())
        self.canvas.i = float(self.value_layout.i_line.text())
        self.canvas.condiciones = self.table.collect()

    def initUI(self):
        group_value = QGroupBox("Entrada")
        group_value.setLayout(self.value_layout)
        group_rango = QGroupBox("Rango")
        group_rango.setLayout(self.rango_layout)
        vbox = QVBoxLayout()
        vbox.addWidget(group_value) #Agrega el formulario
        vbox.addWidget(group_rango)
        vbox.addWidget(self.table)
        vbox.addWidget(self.btn)
        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addWidget(self.canvas, 1)
        self.setLayout(hbox)
    



    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    exc = App()
    exc.show()
    sys.exit(app.exec())
        