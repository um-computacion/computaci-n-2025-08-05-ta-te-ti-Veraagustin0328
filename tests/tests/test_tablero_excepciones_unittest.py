import os, sys, unittest
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path: sys.path.insert(0, SRC)

from tateti.tablero import Tablero, PosFueraDeRangoException, PosOcupadaException

class TestTableroExcepciones(unittest.TestCase):
    def test_fuera_de_rango(self):
        t = Tablero()
        for f,c in [(-1,0),(0,-1),(3,0),(0,3),(9,9)]:
            with self.subTest(par=(f,c)):
                with self.assertRaises(PosFueraDeRangoException):
                    t.poner_la_ficha(f,c,"X")

    def test_posicion_ocupada(self):
        t = Tablero()
        t.poner_la_ficha(1,1,"X")
        with self.assertRaises(PosOcupadaException):
            t.poner_la_ficha(1,1,"0")

    def test_coloca_actualiza_celda(self):
        t = Tablero()
        t.poner_la_ficha(2,2,"0")
        self.assertEqual(t.contenedor[2][2], "0")
