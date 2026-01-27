def test_desviacion_vacia(self):
    calc = Calculator()
    assert calc.standard_deviation([]) == 0