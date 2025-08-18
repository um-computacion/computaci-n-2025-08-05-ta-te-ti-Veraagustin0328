import os, sys, unittest
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path: sys.path.insert(0, SRC)

from tateti.tateti import Tateti

class TestTateti(unittest.TestCase):
    def test_turno_inicial(self):
        j = Tateti()
        self.assertEqual(j.turno, "X")
        self.assertIsNone(j.resultado)

    def test_alternancia_de_turnos(self):
        j = Tateti()
        j.ocupar_una_de_las_casillas(0,0)  # X
        self.assertEqual(j.turno, "0")
        j.ocupar_una_de_las_casillas(1,1)  # 0
        self.assertEqual(j.turno, "X")

    def test_gana_x_por_fila(self):
        j = Tateti()
        j.ocupar_una_de_las_casillas(0,0)  # X
        j.ocupar_una_de_las_casillas(1,0)  # 0
        j.ocupar_una_de_las_casillas(0,1)  # X
        j.ocupar_una_de_las_casillas(1,1)  # 0
        j.ocupar_una_de_las_casillas(0,2)  # X
        self.assertEqual(j.resultado, "X")

    def test_gana_0_por_columna(self):
        j = Tateti()
        # 0 gana en la columna 1
        j.ocupar_una_de_las_casillas(0,0)  # X
        j.ocupar_una_de_las_casillas(0,1)  # 0
        j.ocupar_una_de_las_casillas(2,2)  # X
        j.ocupar_una_de_las_casillas(1,1)  # 0
        j.ocupar_una_de_las_casillas(2,0)  # X
        j.ocupar_una_de_las_casillas(2,1)  # 0
        self.assertEqual(j.resultado, "0")

    def test_empate_via_api(self):
        j = Tateti()
        sec = [
            (0,0),(0,1),(0,2),
            (1,1),(1,0),(1,2),
            (2,1),(2,0),(2,2),
        ]
        for f,c in sec:
            if j.resultado is None:
                j.ocupar_una_de_las_casillas(f,c)
        self.assertEqual(j.resultado, "EMPATE")

    def test_no_permite_jugar_tras_final(self):
        j = Tateti()
        # X gana
        j.ocupar_una_de_las_casillas(0,0)
        j.ocupar_una_de_las_casillas(1,0)
        j.ocupar_una_de_las_casillas(0,1)
        j.ocupar_una_de_las_casillas(1,1)
        j.ocupar_una_de_las_casillas(0,2)
        self.assertEqual(j.resultado, "X")
        turno_antes = j.turno
        j.ocupar_una_de_las_casillas(2,2)  # debería ignorar
        self.assertEqual(j.resultado, "X")
        self.assertEqual(j.turno, turno_antes)
