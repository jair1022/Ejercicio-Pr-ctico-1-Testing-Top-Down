class HistorialStub:
    """Stub que simula historial de préstamos"""

    def obtener_historial(self, usuario_id):
        # Devuelve un historial simulado
        return [
            {"libro_id": 1, "titulo": "Introducción a Python"},
            {"libro_id": 2, "titulo": "Machine Learning Básico"},
        ] if usuario_id > 0 else []
