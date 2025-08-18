import os, sys, unittest
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path: sys.path.insert(0, SRC)

from tateti.tablero import Tablero

class TestRenderizado(unittest.TestCase):
    def test_como_texto_inicial(self):
        t = Tablero()
        s = t.como_texto()
        self.assertIn("   0   1   2", s)
        self.assertIn(". | . | .", s)

    def test_como_texto_con_fichas(self):
        t = Tablero()
        t.poner_la_ficha(0,0,"X")
        t.poner_la_ficha(1,1,"0")
        s = t.como_texto()
        self.assertIn("X", s)
        self.assertIn("0", s)
