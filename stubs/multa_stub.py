class MultaStub:
    """Stub que simula multas de usuario"""

    def tiene_multas(self, usuario_id):
        # Usuarios con ID múltiplo de 5 tienen multas
        return usuario_id % 5 == 0
