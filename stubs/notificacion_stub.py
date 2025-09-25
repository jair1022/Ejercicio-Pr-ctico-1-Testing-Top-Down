class NotificacionStub:
    """Stub que simula notificación al usuario"""

    def enviar_notificacion(self, usuario_id, mensaje):
        # Simulación: siempre envía con éxito
        print(f"[STUB] Notificación enviada a usuario {usuario_id}: {mensaje}")
        return True
