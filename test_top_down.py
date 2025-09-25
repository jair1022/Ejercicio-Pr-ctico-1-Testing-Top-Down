import pytest
from biblioteca_sistema import BibliotecaSistema
from stubs.database_stub import DatabaseStub
from stubs.auth_stub import AuthStub
from stubs.notificacion_stub import NotificacionStub
from stubs.catalogo_stub import CatalogoStub
from stubs.multa_stub import MultaStub

# --- Pruebas originales (prestamo exitoso, no autorizado, no disponible) ---

def test_usuario_con_multas():
    """Usuario con multas no puede prestar"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    multa_stub = MultaStub()
    sistema = BibliotecaSistema(db_stub, auth_stub, multa=multa_stub)

    resultado = sistema.prestar_libro(usuario_id=5, libro_id=2)
    assert resultado == "Usuario con multas pendientes"

def test_prestamo_con_notificacion():
    """Préstamo exitoso envía notificación"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    notif_stub = NotificacionStub()
    sistema = BibliotecaSistema(db_stub, auth_stub, notificacion=notif_stub)

    resultado = sistema.prestar_libro(usuario_id=1, libro_id=2)
    assert resultado == "Préstamo exitoso"

def test_buscar_libro_existente():
    """Buscar un libro que existe en catálogo"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    catalogo_stub = CatalogoStub()
    sistema = BibliotecaSistema(db_stub, auth_stub, catalogo=catalogo_stub)

    libro = sistema.buscar_libro("Python Básico")
    assert libro is not None
    assert libro["titulo"] == "Python Básico"

def test_buscar_libro_inexistente():
    """Buscar un libro que no existe en catálogo"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    catalogo_stub = CatalogoStub()
    sistema = BibliotecaSistema(db_stub, auth_stub, catalogo=catalogo_stub)

    libro = sistema.buscar_libro("Historia Antigua")
    assert libro is None


