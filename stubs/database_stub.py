class DatabaseStub:
    """Stub que simula base de datos"""

    def libro_disponible(self, libro_id):
        # Simulamos que solo los libros con ID par están disponibles
        return libro_id % 2 == 0

    def registrar_prestamo(self, usuario_id, libro_id):
        # Simulamos que se guarda el préstamo exitosamente
        print(f"[STUB] Préstamo registrado: User={usuario_id}, Book={libro_id}")
        return True
