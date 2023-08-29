from exercicio1 import desconto

def test_desconto():
    assert desconto(100, 20) == (1900, 2000)
    assert desconto(200,300) == (54000.0, 60000)
    assert desconto(100,100000) == (8500000.0, 10000000)