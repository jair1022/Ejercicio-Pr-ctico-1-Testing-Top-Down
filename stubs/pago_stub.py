class PagoStub:
    """Stub que simula pagos"""

    def procesar_pago(self, usuario_id, monto):
        # Simulación: todo pago mayor a 0 se procesa
        if monto > 0:
            print(f"[STUB] Pago procesado: Usuario={usuario_id}, Monto={monto}")
            return True
        return False
