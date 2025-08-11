from .tablero import Tablero
class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.resultado = None  # None | "X" | "0" | "EMPATE"
    def ocupar_una_de_las_casillas(self, fil, col):
        if self.resultado is not None:
            return
        self.tablero.poner_la_ficha(fil, col, self.turno)
        estado = self.tablero.estado()
        if estado is not None:
            self.resultado = estado
            return
        self.turno = "0" if self.turno == "X" else "X"
