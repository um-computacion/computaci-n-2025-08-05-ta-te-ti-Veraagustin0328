class Jugador:
    def __init__(self, ficha: str):
        if ficha not in {"X", "0"}:
            raise ValueError("La ficha debe ser 'X' u '0'")
        self.ficha = ficha
