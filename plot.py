from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np


class Canvas(FigureCanvasQTAgg):
    def __init__(self, figure=Figure(figsize=(5, 4), dpi=100)):
        super().__init__(figure)
        self.axes = figure.add_subplot(111)
        self.rango = 100
        self.dw = 0 # Dias trabajados
        self.d = 0 #Demanda Diaria
        self.c = 0 #Costo Producto
        self.s = 0 #Costo Pedido
        self.i = 0 #%Costo
        self.condiciones = []
        self.config()

    def costo_mantenimiento(self, q):
        return (q / 2) * self.i * self.c

    def costo_pedido(self, q):
        D = self.dw * self.d
        return (D/q) * self.s

    def costo_producto(self, q):
        D = self.dw * self.d
        costo = self.c * D
        condiciones = iter(self.condiciones)
        actual, sig = next(condiciones), next(condiciones, None)
        for qi in q:
            if sig and qi >= sig.rango:
                actual, sig = sig, next(condiciones, None)
            if qi >= actual.rango:
                yield costo - costo * actual.descuento
            else:
                yield costo
    

    def plot(self):
        self.axes.clear()
        q = np.arange(1, self.rango * 10, 0.1)
        costo_producto = list(self.costo_producto(q))
        costo_pedido = self.costo_pedido(q)
        costo_mantenimiento = self.costo_mantenimiento(q)
        costo_total = costo_producto + costo_pedido + costo_mantenimiento
        self.axes.plot(q, costo_producto, label="Costo Producto")
        self.axes.plot(q, costo_pedido, label='Costo pedido')
        self.axes.plot(q, costo_mantenimiento, label='Costo Mantenimiento')
        self.axes.plot(q, costo_total, label="Costo Total")
        self.config()
        self.draw()
    
    def config(self):
        self.axes.set_xlabel('Q')
        self.axes.set_ylabel('Costos')
        self.axes.legend()

    @property
    def utilidad_maxima(self):
        b = self.min_prod_b
        a = self.lim_prod - b
        utilidad = self.valor_a * a + self.valor_b * b
        return {'a': a, 'b': b, 'utilidad': utilidad}