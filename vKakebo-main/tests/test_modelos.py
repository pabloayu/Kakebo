from datetime import date
from kakebo.modelos import Ingreso, CategoriaGastos, Gasto
import pytest

def test_instanciar_ingreso():
    movimiento = Ingreso("Loteria del niño, premio", date(2024, 1, 5), 1000)

    assert movimiento.concepto == "Loteria del niño, premio"
    assert movimiento.fecha == date(2024, 1, 5)
    assert movimiento.cantidad == 1000

def test_ingreso_concepto_debe_ser_string():
    with pytest.raises(TypeError):
        movimiento = Ingreso(19, date(2024, 1, 5), 1000)

def test_ingreso_fecha_typeError():
    with pytest.raises(TypeError):
        movimiento = Ingreso("Indiferente", "lolailo", 1000)

def test_ingreso_cantidad_typeError():
    with pytest.raises(TypeError):
        movimiento = Ingreso("Indiferente", date.today(), "casa")

    movimiento = Ingreso("Indiferente", date.today(), 1000)
    movimiento = Ingreso("Indiferente", date.today(), 1000.1)
     
"""
Tests que faltan por ahora
   - La cantidad no puede ser cero
   - La fecha del ingreso debe ser menor o igual a hoy (no se admiten movimientos futuros)
   - El concepto debe tener una longitud mayor de 5
"""

def test_cantidad_no_puede_ser_negativo():
    with pytest.raises(ValueError):
        movimiento = Ingreso("loteria", date(2024, 1, 5), 0)

def test_concepto_no_puede_estar_vacio():
    with pytest.raises(ValueError):
        movimiento = Ingreso("", date(2024, 12, 2), 1000)

def test_validar_fecha_posterior_hoy():
    with pytest.raises(ValueError):
        movimiento = Ingreso("Loteria", date(2025, 1, 5), 1000.1)

def test_validar_longitud_concepto():
    with pytest.raises(ValueError):
        movimiento = Ingreso("lo", date(2024, 1, 1), 1000)

def test_crear_gasto():
    movimiento = Gasto("Factura del Agua", date(2024,5,1), 70, CategoriaGastos.NECESIDAD)
    assert movimiento.concepto == "Factura del Agua"
    assert movimiento.fecha == date(2024,5,1)
    assert movimiento.cantidad == 70
    assert movimiento.categoria == CategoriaGastos.NECESIDAD

def test_gasto_categoria_tipo_correcto():
    with pytest.raises(TypeError):
       movimiento = Gasto("Factura del Agua", date(2024,5,1), 70, "Necesidad") 

    
