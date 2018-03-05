from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit

class ValueLayout(QFormLayout):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.dw_line = QLineEdit()
        self.d_line = QLineEdit()
        self.c_line = QLineEdit()
        self.s_line = QLineEdit()
        self.i_line = QLineEdit() 
        self.addRow(QLabel("Dias Trabajados:"), self.dw_line)
        self.addRow(QLabel("Demanda Diara:"), self.d_line)
        self.addRow(QLabel("Costo Producto:"), self.c_line)
        self.addRow(QLabel("Costo Pedido:"), self.s_line)
        self.addRow(QLabel("% Costo:"), self.i_line)

class RangoLayout(QFormLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rango_line = QLineEdit()
        self.addRow(QLabel("Rango:"), self.rango_line)
        self.rango_line.setText("100")