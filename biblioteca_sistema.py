class BibliotecaSistema:
    def __init__(self, db, auth, notificacion=None, catalogo=None, multa=None,
                 reserva=None, historial=None, recomendacion=None, pago=None, reportes=None):
        self.db = db
        self.auth = auth
        self.notificacion = notificacion
        self.catalogo = catalogo
        self.multa = multa
        self.reserva = reserva
        self.historial = historial
        self.recomendacion = recomendacion
        self.pago = pago
        self.reportes = reportes

    def prestar_libro(self, usuario_id, libro_id):
        # 1. Verificar si el usuario está autorizado
        if not self.auth.verificar_usuario(usuario_id):
            return "Usuario no autorizado"

        # 2. Verificar si el usuario tiene multas pendientes
        if self.multa and self.multa.tiene_multas(usuario_id):
            return "Usuario con multas pendientes"

        # 3. Verificar si el libro está disponible
        if not self.db.libro_disponible(libro_id):
            return "Libro no disponible"

        # 4. Registrar préstamo
        self.db.registrar_prestamo(usuario_id, libro_id)

        # 5. Enviar notificación (si el módulo existe)
        if self.notificacion:
            self.notificacion.enviar_notificacion(usuario_id, "Préstamo realizado")

        return "Préstamo exitoso"

    def buscar_libro(self, titulo):
        # Buscar libro en el catálogo (si el stub existe)
        if self.catalogo:
            return self.catalogo.buscar_libro(titulo)
        return None
    
    def reservar_libro(self, usuario_id, libro_id):
        if self.reserva:
            return self.reserva.reservar_libro(usuario_id, libro_id)
        return "Módulo de reservas no disponible"

    def ver_historial(self, usuario_id):
        if self.historial:
            return self.historial.obtener_historial(usuario_id)
        return []

    def obtener_recomendaciones(self, usuario_id):
        if self.recomendacion:
            return self.recomendacion.recomendar(usuario_id)
        return []

    def pagar_multa(self, usuario_id, monto):
        if self.pago:
            return self.pago.procesar_pago(usuario_id, monto)
        return False

    def generar_reporte(self, tipo):
        if self.reportes:
            return self.reportes.generar_reporte(tipo)
        return {"mensaje": "Módulo de reportes no disponible"}
