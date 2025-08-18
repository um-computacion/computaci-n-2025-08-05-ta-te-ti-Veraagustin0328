import os, sys, unittest
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
if SRC not in sys.path: sys.path.insert(0, SRC)

from tateti.tablero import Tablero

class TestTableroCasosExtra(unittest.TestCase):
    def test_no_hay_ganador_con_dos_en_linea(self):
        t = Tablero()
        t.poner_la_ficha(0,0,"X"); t.poner_la_ficha(0,1,"X")
        self.assertIsNone(t.estado())

    def test_estado_sigue_none_hasta_jugada_ganadora_fila(self):
        t = Tablero()
        t.poner_la_ficha(1,0,"X"); t.poner_la_ficha(1,1,"X")
        self.assertIsNone(t.estado())
        t.poner_la_ficha(1,2,"X")
        self.assertEqual(t.estado(),"X")

    def test_estado_sigue_none_hasta_jugada_ganadora_columna(self):
        t = Tablero()
        t.poner_la_ficha(0,2,"0"); t.poner_la_ficha(1,2,"0")
        self.assertIsNone(t.estado())
        t.poner_la_ficha(2,2,"0")
        self.assertEqual(t.estado(),"0")

    def test_estado_sigue_none_hasta_jugada_ganadora_diagonal(self):
        t = Tablero()
        t.poner_la_ficha(0,0,"X"); t.poner_la_ficha(1,1,"X")
        self.assertIsNone(t.estado())
        t.poner_la_ficha(2,2,"X")
        self.assertEqual(t.estado(),"X")

    def test_hay_libres_false_solo_tablero_lleno(self):
        t = Tablero()
        self.assertTrue(t.hay_libres())
        # Llenar sin ganador (empate)
        sec = [
            (0,0,"X"),(0,1,"0"),(0,2,"X"),
            (1,0,"X"),(1,1,"0"),(1,2,"0"),
            (2,0,"0"),(2,1,"X"),(2,2,"X"),
        ]
        for f,c,fi in sec: t.poner_la_ficha(f,c,fi)
        self.assertFalse(t.hay_libres())
        self.assertEqual(t.estado(),"EMPATE")

    def test_como_texto_formato_separadores(self):
        t = Tablero()
        out = t.como_texto()
        self.assertIn("   0   1   2", out)
        self.assertIn("  ---------", out)

    def test_no_modifica_otros_casilleros_al_colocar(self):
        t = Tablero()
        t.poner_la_ficha(2,1,"0")
        self.assertEqual(t.contenedor[2][1],"0")
        # El resto de la fila debe seguir vacío
        self.assertEqual(t.contenedor[2][0],"")
        self.assertEqual(t.contenedor[2][2],"")
