from src.calculator import standard_deviation

def test_desviacion_vacia():
    assert standard_deviation([]) == 0

def test_desviacion_un_dato():
    assert standard_deviation([10]) == 0

def test_desviacion_varios_datos():
    # Desviación de 4 y 8 es 2.828
    assert standard_deviation([4, 8]) == 2.828