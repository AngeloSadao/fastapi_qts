from app.fidelidade.pontos import calcular_pontos_compra


def test_compra_comum_de_cinquenta_reais_gera_cinco_pontos():
    # Regra base: cada 10 reais gastos geram 1 ponto
    resultado = calcular_pontos_compra(valor_gasto=50.0, categoria="padrao")
    assert resultado == 5

def test_compra_com_valor_zero_ou_negativo_gera_zero_pontos():
    assert calcular_pontos_compra(valor_gasto=0.0, categoria="padrao") == 0
    assert calcular_pontos_compra(valor_gasto=-25.0, categoria="padrao") == 0

def test_cliente_premium_recebe_cinco_pontos_de_bonus_acima_de_vinte_reais():
    # 30 reais geram 3 pontos base mais 5 pontos de bonus = 8 pontos
    resultado = calcular_pontos_compra(valor_gasto=30.0, categoria="premium")
    assert resultado == 8


def test_cliente_premium_com_compra_baixa_nao_recebe_bonus():
    # 15 reais geram 1 ponto base sem bonus
    resultado = calcular_pontos_compra(valor_gasto=15.0, categoria="premium")
    assert resultado == 1

def test_cliente_ouro_recebe_dez_pontos_de_bonus():
    # 40 reais geram 4 pontos base mais 10 pontos de bonus = 14 pontos
    resultado = calcular_pontos_compra(valor_gasto=40.0, categoria="ouro")
    assert resultado == 14