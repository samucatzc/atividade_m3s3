from exercicio3 import calcular_preco_volume, calcular_multiplicador_rota

def test_calcular_preco_volume():
    assert calcular_preco_volume(100) == 10.0
    assert calcular_preco_volume(5555) == 20.0
    assert calcular_preco_volume(11111) == 30.0
    assert calcular_preco_volume(33333) == 20.0

def test_calcular_multiplicador_rota():
    assert calcular_multiplicador_rota('rs') == 1.0
    assert calcular_multiplicador_rota('bs') == 1.2
    assert calcular_multiplicador_rota('br') == 1.5