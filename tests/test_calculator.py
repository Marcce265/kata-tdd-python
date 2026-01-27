from src.calculator import standard_deviation

def test_desviacion_vacia():
    assert standard_deviation([]) == 0


def test_desviacion_un_dato():
    assert standard_deviation([5]) == 0