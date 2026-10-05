import time
import pytest
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atrasado, retorno_esperado",
    [
        (0.0,   "BASICO",      1,  -1.0),
        (10.0,  "BASICO",     -1,  -1.0),
        (10.0,  "AVANCADO",    0,  -2.0),
        (10.0,  "",            0,  -2.0),
        (10.0,  "  basico  ",  0,  10.0),
        (10.0,  "  premium  ", 0,   9.0),
        (100.0, "BASICO",      0, 100.0),
        (100.0, "PREMIUM",     0,  90.0),
        (100.0, "EMPRESARIAL", 0,  80.0),
        (100.0, "BASICO",      1, round(100 + 5 + 100 * 1 * 0.005, 2)),
        (100.0, "BASICO",     30, round(100 + 5 + 100 * 30 * 0.005, 2)),
        (100.0, "PREMIUM",    15, round(90 + 5 + 90 * 15 * 0.005, 2)),
        (100.0, "BASICO",     31, round(100 + 25 + 100 * 31 * 0.01, 2)),
        (100.0, "PREMIUM",    45, round(90 + 25 + 90 * 45 * 0.01, 2)),
        (100.0, "EMPRESARIAL",31, round(80 + 25 + 80 * 31 * 0.01, 2)),
    ]
)
def test_processar_cobranca_funcional(valor_base, plano, dias_atrasado, retorno_esperado):
    assert processar_cobranca(valor_base, plano, dias_atrasado) == retorno_esperado


def test_processar_cobranca_desempenho():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "BASICO", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado is not None
    assert tempo_decorrido < 0.1