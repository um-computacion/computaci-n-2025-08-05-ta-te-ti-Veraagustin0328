import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from tateti.tateti import Tateti
from tateti.tablero import PosOcupadaException, PosFueraDeRangoException
def main():
    print("Bienvenidos al Tateti")
    print("Coordenadas válidas: filas y columnas 0, 1, 2")
    juego = Tateti()
    while True:
        print("\nTablero:")
        print(juego.tablero.como_texto())
        if juego.resultado is not None:
            if juego.resultado in ("X","0"):
                print(f"\n¡Ganó {juego.resultado}!")
            else:
                print("\nEmpate.")
            break
        print(f"\nTurno: {juego.turno}")
        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese col (0-2): "))
            juego.ocupar_una_de_las_casillas(fil, col)
        except ValueError:
            print("Entrada inválida: use números 0, 1 o 2.")
        except PosFueraDeRangoException as e:
            print(e)
        except PosOcupadaException as e:
            print(e)
        except Exception as e:
            print("Error inesperado:", e)
if __name__ == "__main__":
    main()
