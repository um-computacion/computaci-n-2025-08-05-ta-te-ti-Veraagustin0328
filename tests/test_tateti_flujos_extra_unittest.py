import os, sys, unittest
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from tateti.tateti import Tateti
from tateti.tablero import PosFueraDeRangoException, PosOcupadaException

class TestTatetiFlujosExtra(unittest.TestCase):
    def test_gana_0_por_diagonal(self):
        j = Tateti()
        # 0 gana con diagonal secundaria (0,2)-(1,1)-(2,0)
        j.ocupar_una_de_las_casillas(0,0)  # X
        j.ocupar_una_de_las_casillas(0,2)  # 0
        j.ocupar_una_de_las_casillas(2,2)  # X
        j.ocupar_una_de_las_casillas(1,1)  # 0
        j.ocupar_una_de_las_casillas(1,0)  # X
        self.assertIsNone(j.resultado)      # todavía nadie gana
        j.ocupar_una_de_las_casillas(2,0)  # 0 cierra diagonal
        self.assertEqual(j.resultado, "0")

    def test_gana_x_por_columna(self):
        j = Tateti()
        # X gana en columna 0
        j.ocupar_una_de_las_casillas(0,0)  # X
        j.ocupar_una_de_las_casillas(0,1)  # 0
        j.ocupar_una_de_las_casillas(1,0)  # X
        j.ocupar_una_de_las_casillas(1,1)  # 0
        j.ocupar_una_de_las_casillas(2,0)  # X
        self.assertEqual(j.resultado, "X")

    def test_empate_secuencia_alternada_distinta(self):
        j = Tateti()
        # Tablero final (empate):
        # X X O
        # O O X
        # X O X
        sec = [
            (0,0),(0,2),(0,1),
            (1,0),(2,0),(2,1),
            (2,2),(1,1),(1,2),
        ]
        for f,c in sec:
            if j.resultado is None:
                j.ocupar_una_de_las_casillas(f,c)
        self.assertEqual(j.resultado, "EMPATE")

    def test_intento_jugar_pos_ocupada_mantiene_turno(self):
        j = Tateti()
        j.ocupar_una_de_las_casillas(0,0)  # X
        turno_antes = j.turno
        with self.assertRaises(PosOcupadaException):
            j.ocupar_una_de_las_casillas(0,0)
        self.assertEqual(j.turno, turno_antes)

    def test_jugada_fuera_de_rango_no_cambia_turno(self):
        j = Tateti()
        turno_antes = j.turno
        with self.assertRaises(PosFueraDeRangoException):
            j.ocupar_una_de_las_casillas(3,3)
        self.assertEqual(j.turno, turno_antes)

    def test_no_permite_jugar_despues_de_empate(self):
        j = Tateti()
        # forzar empate
        sec = [
            (0,0),(0,1),(0,2),
            (1,1),(1,0),(1,2),
            (2,1),(2,0),(2,2),
        ]
        for f,c in sec:
            if j.resultado is None:
                j.ocupar_una_de_las_casillas(f,c)
        self.assertEqual(j.resultado, "EMPATE")
        turno_antes = j.turno
        j.ocupar_una_de_las_casillas(2,2)  # ignorado
        self.assertEqual(j.turno, turno_antes)
        self.assertEqual(j.resultado, "EMPATE")

    def test_ignora_jugadas_despues_de_ganar_multiples(self):
        j = Tateti()
        # X gana por fila 0
        j.ocupar_una_de_las_casillas(0,0)
        j.ocupar_una_de_las_casillas(1,0)
        j.ocupar_una_de_las_casillas(0,1)
        j.ocupar_una_de_las_casillas(1,1)
        j.ocupar_una_de_las_casillas(0,2)  # gana X
        self.assertEqual(j.resultado,"X")
        turno_antes = j.turno
        # más jugadas deberían ignorarse
        for _ in range(3):
            j.ocupar_una_de_las_casillas(2,2)
        self.assertEqual(j.turno, turno_antes)
        self.assertEqual(j.resultado,"X")

if __name__ == "__main__":
    unittest.main()
