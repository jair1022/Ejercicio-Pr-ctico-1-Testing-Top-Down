class CatalogoStub:
    """Stub que simula catálogo de libros"""

    def buscar_libro(self, titulo):
        # Simulación: si el título contiene "Python", existe
        if "Python" in titulo:
            return {"id": 10, "titulo": titulo, "autor": "Autor Ejemplo"}
        return None
