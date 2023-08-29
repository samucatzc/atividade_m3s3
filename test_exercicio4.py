from exercicio4 import gerar_codigo, imprimir_peca, cadastrar_peca

def test_gerar_codigo():
    assert gerar_codigo() == 1

def test_imprimir_peca():
    assert imprimir_peca({
        'codigo': 100,
        'nome': 'bababa',
        'fabricante': 'julia',
        'valor': 1000.0
    }) == '100 bababa julia 1000.0'

def test_cadastrar_peca():
    assert cadastrar_peca() == 1