class RecomendacionStub:
    """Stub que recomienda libros según historial"""

    def recomendar(self, usuario_id):
        # Simulación: usuarios pares reciben recomendación de ciencia ficción
        if usuario_id % 2 == 0:
            return ["Dune", "Fundación"]
        return ["Cien años de soledad", "El Quijote"]
