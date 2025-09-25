class AuthStub:
    """Stub que simula autenticación"""

    def verificar_usuario(self, usuario_id):
        # Simulamos que usuarios con ID > 0 son válidos
        return usuario_id > 0
