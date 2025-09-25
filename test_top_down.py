import pytest
from biblioteca_sistema import BibliotecaSistema
from stubs.database_stub import DatabaseStub
from stubs.auth_stub import AuthStub
from stubs.notificacion_stub import NotificacionStub
from stubs.catalogo_stub import CatalogoStub
from stubs.multa_stub import MultaStub
from stubs.reserva_stub import ReservaStub
from stubs.historial_stub import HistorialStub
from stubs.recomendacion_stub import RecomendacionStub
from stubs.pago_stub import PagoStub
from stubs.reportes_stub import ReportesStub

# ===================== PRUEBAS DE PRÉSTAMOS =====================

def test_prestamo_exitoso():
    db = DatabaseStub()
    auth = AuthStub()
    sistema = BibliotecaSistema(db, auth)
    assert sistema.prestar_libro(1, 2) == "Préstamo exitoso"

def test_usuario_no_autorizado():
    db = DatabaseStub()
    auth = AuthStub()
    sistema = BibliotecaSistema(db, auth)
    assert sistema.prestar_libro(0, 2) == "Usuario no autorizado"

def test_libro_no_disponible():
    db = DatabaseStub()
    auth = AuthStub()
    sistema = BibliotecaSistema(db, auth)
    assert sistema.prestar_libro(1, 3) == "Libro no disponible"

def test_usuario_con_multas():
    db = DatabaseStub()
    auth = AuthStub()
    multa = MultaStub()
    sistema = BibliotecaSistema(db, auth, multa=multa)
    assert sistema.prestar_libro(5, 2) == "Usuario con multas pendientes"

def test_prestamo_con_notificacion():
    db = DatabaseStub()
    auth = AuthStub()
    notif = NotificacionStub()
    sistema = BibliotecaSistema(db, auth, notificacion=notif)
    assert sistema.prestar_libro(1, 2) == "Préstamo exitoso"

# ===================== PRUEBAS DE CATÁLOGO =====================

def test_buscar_libro_existente():
    db = DatabaseStub()
    auth = AuthStub()
    catalogo = CatalogoStub()
    sistema = BibliotecaSistema(db, auth, catalogo=catalogo)
    libro = sistema.buscar_libro("Python Básico")
    assert libro is not None
    assert libro["titulo"] == "Python Básico"

def test_buscar_libro_inexistente():
    db = DatabaseStub()
    auth = AuthStub()
    catalogo = CatalogoStub()
    sistema = BibliotecaSistema(db, auth, catalogo=catalogo)
    assert sistema.buscar_libro("Historia Antigua") is None

# ===================== PRUEBAS DE RESERVAS =====================

def test_reserva_exitosa():
    db = DatabaseStub()
    auth = AuthStub()
    reserva = ReservaStub()
    sistema = BibliotecaSistema(db, auth, reserva=reserva)
    assert sistema.reservar_libro(1, 150) is True

def test_reserva_fallida():
    db = DatabaseStub()
    auth = AuthStub()
    reserva = ReservaStub()
    sistema = BibliotecaSistema(db, auth, reserva=reserva)
    assert sistema.reservar_libro(1, 50) is False

# ===================== PRUEBAS DE HISTORIAL =====================

def test_historial_usuario_valido():
    db = DatabaseStub()
    auth = AuthStub()
    historial = HistorialStub()
    sistema = BibliotecaSistema(db, auth, historial=historial)
    data = sistema.ver_historial(1)
    assert len(data) > 0

def test_historial_usuario_invalido():
    db = DatabaseStub()
    auth = AuthStub()
    historial = HistorialStub()
    sistema = BibliotecaSistema(db, auth, historial=historial)
    assert sistema.ver_historial(0) == []

# ===================== PRUEBAS DE RECOMENDACIÓN =====================

def test_recomendacion_usuario_par():
    db = DatabaseStub()
    auth = AuthStub()
    reco = RecomendacionStub()
    sistema = BibliotecaSistema(db, auth, recomendacion=reco)
    recos = sistema.obtener_recomendaciones(2)
    assert "Dune" in recos

def test_recomendacion_usuario_impar():
    db = DatabaseStub()
    auth = AuthStub()
    reco = RecomendacionStub()
    sistema = BibliotecaSistema(db, auth, recomendacion=reco)
    recos = sistema.obtener_recomendaciones(3)
    assert "Cien años de soledad" in recos

# ===================== PRUEBAS DE PAGOS =====================

def test_pago_exitoso():
    db = DatabaseStub()
    auth = AuthStub()
    pago = PagoStub()
    sistema = BibliotecaSistema(db, auth, pago=pago)
    assert sistema.pagar_multa(1, 100) is True

def test_pago_fallido():
    db = DatabaseStub()
    auth = AuthStub()
    pago = PagoStub()
    sistema = BibliotecaSistema(db, auth, pago=pago)
    assert sistema.pagar_multa(1, 0) is False

# ===================== PRUEBAS DE REPORTES =====================

def test_reporte_prestamos():
    db = DatabaseStub()
    auth = AuthStub()
    reportes = ReportesStub()
    sistema = BibliotecaSistema(db, auth, reportes=reportes)
    data = sistema.generar_reporte("prestamos")
    assert "total" in data

def test_reporte_no_soportado():
    db = DatabaseStub()
    auth = AuthStub()
