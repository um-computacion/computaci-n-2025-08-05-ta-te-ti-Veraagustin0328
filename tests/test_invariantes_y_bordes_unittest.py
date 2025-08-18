import os, sys, unittest
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from tateti.tablero import Tablero, PosFueraDeRangoException
from tateti.tateti import Tateti

class TestInvariantesYBordes(unittest.TestCase):
    def test_tablero_inicia_vacio_solo_puntos_en_render(self):
        t = Tablero()
        s = t.como_texto()
        # Deben aparecer 3 filas vacías
        self.assertEqual(s.count(". | . | ."), 3)
        # No debe haber ninguna X al inicio
        self.assertNotIn("X", s)

    def test_tablero_estado_no_cambia_sin_movimientos(self):
        t = Tablero()
        self.assertIsNone(t.estado())
        # Llamar al render no debería cambiar nada
        _ = t.como_texto()
        self.assertIsNone(t.estado())

    def test_tateti_no_alterna_en_excepcion_ocupada(self):
        j = Tateti()
        j.ocupar_una_de_las_casillas(1,1)  # X
        turno_antes = j.turno  # debería ser "0"
        with self.assertRaises(Exception):
            j.ocupar_una_de_las_casillas(1,1)  # ocupada
        self.assertEqual(j.turno, turno_antes)

    def test_tateti_no_alterna_en_excepcion_rango(self):
        j = Tateti()
        turno_antes = j.turno
        with self.assertRaises(PosFueraDeRangoException):
            j.ocupar_una_de_las_casillas(-1, 5)
        self.assertEqual(j.turno, turno_antes)

    def test_multiple_partidas_independientes(self):
        a = Tateti()
        b = Tateti()
        a.ocupar_una_de_las_casillas(0,0)  # X en 'a'
        self.assertEqual(a.tablero.contenedor[0][0], "X")
        # 'b' debe seguir vacío
        self.assertEqual(b.tablero.contenedor[0][0], "")

    def test_mezcla_fichas_sin_linea_no_gana(self):
        t = Tablero()
        jugadas = [(0,0,"X"), (0,1,"0"), (1,1,"X")]
        for f,c,fi in jugadas:
            t.poner_la_ficha(f,c,fi)
        self.assertIsNone(t.estado())

if __name__ == "__main__":
    unittest.main()
