def analisar_lead(lead):
    score = 0
    motivos = []

    pontuacao_categoria = {
        "automacao": 50,
        "desenvolvimento": 40,
        "dados": 40,
        "bi": 20,
        "outro": 20
    }

    categoria = lead["categoria"]

    if categoria in pontuacao_categoria:
        pontos = pontuacao_categoria[categoria]
        score += pontos
        motivos.append(
            f"+{pontos} pontos categoria '{categoria}'"
        )

    if lead["empresa"]:
        score += 20
        motivos.append("+20 pontos empresa informada")

    if lead["mensagem"]:
        score += 30
        motivos.append("+30 pontos mensagem informada")

    if score >= 80:
        classificacao = "quente"
    elif score >= 50:
        classificacao = "morno"
    else:
        classificacao = "frio"

    return {
        "score": score,
        "motivos": motivos,
        "classificacao": classificacao
    }