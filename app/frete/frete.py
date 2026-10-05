def classificar_frete(peso_kg: float, regiao: str, premiuim: bool) -> str:
    if peso_kg <= 0:
        return "invalido"

    regiao_limpa = regiao.strip().lower()

    if regiao_limpa not in ("local", "estadual", "nacional"):
        return "regiao invalida"

    if premiuim:
        return "frete gratis"

    if regiao_limpa == "local":
        return "frete reduzido"

    return "frete padrao"