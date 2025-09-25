class BibliotecaSistema:
    def __init__(self, db, auth, notificacion=None, catalogo=None, multa=None,
                 reserva=None, historial=None, recomendacion=None, pago=None, reportes=None):
        """
        Sistema de Gestión de Biblioteca con soporte para pruebas Top Down.
        Los módulos db y auth son obligatorios, los demás stubs son opcionales.

        Parámetros:
            db (obj): Stub de base de datos.
            auth (obj): Stub de autenticación.
            notificacion (obj, opcional): Stub de notificaciones.
            catalogo (obj, opcional): Stub de catálogo de libros.
            multa (obj, opcional): Stub de gestión de multas.
            reserva (obj, opcional): Stub de reservas.
            historial (obj, opcional): Stub de historial de préstamos.
            recomendacion (obj, opcional): Stub de recomendaciones.
            pago (obj, opcional): Stub de pagos.
            reportes (obj, opcional): Stub de reportes estadísticos.
        """
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

    # ================== MÓDULO DE PRÉSTAMOS ==================
    def prestar_libro(self, usuario_id, libro_id):
        """
        Permite prestar un libro validando usuario, multas y disponibilidad.
        """
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

        # 5. Enviar notificación (si existe módulo)
        if self.notificacion:
            self.notificacion.enviar_notificacion(usuario_id, "Préstamo realizado")

        return "Préstamo exitoso"

    # ================== MÓDULO DE CATÁLOGO ==================
    def buscar_libro(self, titulo):
        """
        Busca un libro en el catálogo.
        """
        if self.catalogo:
            return self.catalogo.buscar_libro(titulo)
        return {"mensaje": "Módulo de catálogo no disponible"}

    # ================== MÓDULO DE RESERVAS ==================
    def reservar_libro(self, usuario_id, libro_id):
        """
        Reserva un libro para un usuario.
        """
        if self.reserva:
            return self.reserva.reservar_libro(usuario_id, libro_id)
        return "Módulo de reservas no disponible"

    # ================== MÓDULO DE HISTORIAL ==================
    def ver_historial(self, usuario_id):
        """
        Devuelve el historial de préstamos de un usuario.
        """
        if self.historial:
            return self.historial.obtener_historial(usuario_id)
        return []

    # ================== MÓDULO DE RECOMENDACIONES ==================
    def obtener_recomendaciones(self, usuario_id):
        """
        Devuelve recomendaciones de libros basadas en el historial del usuario.
        """
        if self.recomendacion:
            return self.recomendacion.recomendar(usuario_id)
        return []

    # ================== MÓDULO DE PAGOS ==================
    def pagar_multa(self, usuario_id, monto):
        """
        Procesa el pago de una multa.
        """
        if self.pago:
            return self.pago.procesar_pago(usuario_id, monto)
        return False

    # ================== MÓDULO DE REPORTES ==================
    def generar_reporte(self, tipo):
        """
        Genera un reporte estadístico de la biblioteca.
        """
        if self.reportes:
            return self.reportes.generar_reporte(tipo)
        return {"mensaje": "Módulo de reportes no disponible"}
