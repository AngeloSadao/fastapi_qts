VALOR_BASE_PONTO = 10.0
VALOR_MINIMO_BONUS = 20.0

TABELA_BONUS_CATEGORIA = {
    "ouro": 10,
    "premium": 5,
}


def calcular_pontos_compra(valor_gasto: float, categoria: str) -> int:
    """Calcula os pontos acumulados pelo cliente em uma compra utilizando tabela de bonificacoes."""
    if valor_gasto <= 0:
        return 0

    pontos_base = int(valor_gasto // VALOR_BASE_PONTO)
    categoria_normalizada = categoria.strip().lower() if categoria else ""

    bonus = 0
    if valor_gasto >= VALOR_MINIMO_BONUS:
        bonus = TABELA_BONUS_CATEGORIA.get(categoria_normalizada, 0)

    return pontos_base + bonus