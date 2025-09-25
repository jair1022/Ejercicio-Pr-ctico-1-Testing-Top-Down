class ReportesStub:
    """Stub que simula reportes estadísticos"""

    def generar_reporte(self, tipo):
        if tipo == "prestamos":
            return {"total": 120, "activos": 45}
        elif tipo == "usuarios":
            return {"registrados": 300, "activos": 250}
        else:
            return {"mensaje": "Tipo de reporte no soportado"}
