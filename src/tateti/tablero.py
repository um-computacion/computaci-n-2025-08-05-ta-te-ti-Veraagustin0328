class PosOcupadaException(Exception):
    ...
class PosFueraDeRangoException(Exception):
    ...
class Tablero:
    def __init__(self):
        self.contenedor = [["","",""],["","",""],["","",""]]
    def _validar_rango(self, fil:int, col:int):
        if not (0 <= fil < 3 and 0 <= col < 3):
            raise PosFueraDeRangoException("fila/col fuera de rango (0..2)")
    def poner_la_ficha(self, fil, col, ficha):
        self._validar_rango(fil, col)
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("pos ocupada!")
    def _lineas(self):
        f = self.contenedor
        cols = [[f[r][c] for r in range(3)] for c in range(3)]
        d1 = [f[i][i] for i in range(3)]
        d2 = [f[i][2-i] for i in range(3)]
        return f + cols + [d1, d2]
    def hay_linea(self, ficha:str)->bool:
        return any(all(c==ficha for c in linea) for linea in self._lineas())
    def hay_libres(self)->bool:
        return any(c=="" for fila in self.contenedor for c in fila)
    def estado(self):
        if self.hay_linea("X"): return "X"
        if self.hay_linea("0"): return "0"
        if not self.hay_libres(): return "EMPATE"
        return None
    def como_texto(self)->str:
        filas_fmt=[]
        for i,fila in enumerate(self.contenedor):
            c=[x if x!="" else "." for x in fila]
            filas_fmt.append(f"{i}  {' | '.join(c)}")
        guia="   0   1   2"; sep="  " + "-"*9
        return "\n".join([guia, filas_fmt[0], sep, filas_fmt[1], sep, filas_fmt[2]])
