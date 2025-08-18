import os, sys, unittest, io
from contextlib import redirect_stdout
from unittest.mock import patch

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
if SRC not in sys.path: sys.path.insert(0, SRC)

# Importo el main de la CLI
from cli.main import main

class TestCLI(unittest.TestCase):
    def test_partida_gana_x(self):
        # Secuencia: X: (0,0), 0: (1,0), X: (0,1), 0: (1,1), X: (0,2) -> gana X
        entradas = ["0","0","1","0","0","1","1","1","0","2"]
        # Cada jugada pide dos inputs (fila y col)
        buf = io.StringIO()
        with patch("builtins.input", side_effect=entradas), redirect_stdout(buf):
            main()
        out = buf.getvalue()
        self.assertIn("¡Ganó X!", out)

if __name__ == "__main__":
    unittest.main()
