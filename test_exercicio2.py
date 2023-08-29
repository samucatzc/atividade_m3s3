from exercicio2 import valor, menu #o * importa tudo

def test_valor():
    assert valor(100) == 9.00
    assert valor(101) == 11.00
    assert valor(102) == 12.00
    assert valor(103) == 12.00
    assert valor(104) == 14.00
    assert valor(105) == 17.00
    assert valor(200) == 5.00
    assert valor(201) == 4.00

def test_menu():
    assert menu(100) == 9.00
    assert menu(101, 102) == 23.00
    assert menu(100, 103, 104, 201) == 39.00

