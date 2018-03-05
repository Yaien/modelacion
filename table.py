from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

class Condition:
    def __init__(self, rango: int, descuento: float):
        self.rango = rango
        self.descuento = descuento


sample_conditions = (
    Condition(100, 0.1),
    Condition(200, 0.2),
    Condition(300, 0.3),
    Condition(400, 0.4)
)


class ConditionTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(2)
        self.setRowCount(4)
        self.setHorizontalHeaderLabels(("Rango", "Descuento"))
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.fill(sample_conditions)
        

    def fill(self, condiciones):
        for row, condicion in enumerate(condiciones):
            self.setItem(row, 0, QTableWidgetItem(str(condicion.rango)))
            self.setItem(row, 1, QTableWidgetItem(str(condicion.descuento)))

    def collect(self):
        condiciones = []
        for row in range(self.rowCount()):
            rango = int(self.item(row, 0).text())
            descuento = float(self.item(row, 1).text())
            condicion = Condition(rango, descuento)
            condiciones.append(condicion)
        return condiciones