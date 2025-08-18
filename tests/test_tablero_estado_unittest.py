import os, sys, unittest
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
if SRC not in sys.path: sys.path.insert(0, SRC)

from tateti.tablero import Tablero

class TestTableroEstado(unittest.TestCase):
    def test_estado_inicial(self):
        t = Tablero()
        self.assertIsNone(t.estado())

    def test_todas_las_filas_ganan_X(self):
        coords_por_fila = [
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
        ]
        for coords in coords_por_fila:
            with self.subTest(fila=coords):
                t = Tablero()
                for f,c in coords:
                    t.poner_la_ficha(f,c,"X")
                self.assertEqual(t.estado(), "X")

    def test_todas_las_columnas_ganan_0(self):
        coords_por_col = [
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
        ]
        for coords in coords_por_col:
            with self.subTest(col=coords):
                t = Tablero()
                for f,c in coords:
                    t.poner_la_ficha(f,c,"0")
                self.assertEqual(t.estado(), "0")

    def test_diagonal_principal(self):
        t = Tablero()
        for i in range(3):
            t.poner_la_ficha(i,i,"X")
        self.assertEqual(t.estado(), "X")

    def test_diagonal_secundaria(self):
        t = Tablero()
        jugadas = [(0,2),(1,1),(2,0)]
        for f,c in jugadas:
            t.poner_la_ficha(f,c,"0")
        self.assertEqual(t.estado(), "0")

    def test_empate(self):
        t = Tablero()
        sec = [
            (0,0,"X"),(0,1,"0"),(0,2,"X"),
            (1,0,"X"),(1,1,"0"),(1,2,"0"),
            (2,0,"0"),(2,1,"X"),(2,2,"X"),
        ]
        for f,c,fi in sec:
            t.poner_la_ficha(f,c,fi)
        self.assertEqual(t.estado(), "EMPATE")
