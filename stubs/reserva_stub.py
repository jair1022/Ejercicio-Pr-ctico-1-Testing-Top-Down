class ReservaStub:
    """Stub que simula la reserva de libros"""

    def reservar_libro(self, usuario_id, libro_id):
        # Solo permite reservar libros con ID mayor a 100
        if libro_id > 100:
            print(f"[STUB] Reserva creada para User={usuario_id}, Book={libro_id}")
            return True
        return False
