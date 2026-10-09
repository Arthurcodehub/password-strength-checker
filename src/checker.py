from .config import * 

def verificar_forca(senha):
    tem_maiuscula = tem_minuscula = tem_especiais = tem_numeros = comprimento_minimo = comprimento_ideal = False
    comprimento = len(senha)
    for char in senha:
        if char in MAIUSCULAS:
            tem_maiuscula = True
        if char in MINUSCULAS:
            tem_minuscula = True
        if char in CARACTERES_ESPECIAIS:
            tem_especiais = True
        if char in NUMEROS:
            tem_numeros = True
    if (comprimento >= COMPRIMENTO_MINIMO):
        comprimento_minimo = True
        if (comprimento >= COMPRIMENTO_IDEAL):
            comprimento_ideal = True
    variaveis = [tem_maiuscula,tem_minuscula,tem_especiais,tem_numeros,comprimento_minimo,comprimento_ideal]
    score = sum(variaveis)
    resultados = {
        "maiuscula": tem_maiuscula,
        "minuscula": tem_minuscula,
        "numeros": tem_numeros,
        "especiais": tem_especiais,
        "comprimento": comprimento,
        "comprimento_minimo": comprimento_minimo,
        "comprimento_ideal": comprimento_ideal,
        "score": score
    }
    return resultados