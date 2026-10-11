from .checker import verificar_forca
EXCECOES = (KeyboardInterrupt, EOFError)
def exibir_resultado(resultados):
    resultados_formatado = {
        "maiuscula": "Maiúscula",
        "minuscula": "Minúscula",
        "numeros": "Números",
        "especiais": "Especiais",
        "comprimento": "Comprimento",
        "comprimento_minimo": "Comprimento Mínimo",
        "comprimento_ideal": "Comprimento Ideal",
        "score": "Score"
    }
    print(f"=== ANÁLISE DE FORÇA ===\n")
    print(f"Critérios:")
    for chave, valor in resultados.items():
        if isinstance(valor, bool):
            emoji = "✅" if valor else "❌"
            print(f"    {emoji} {resultados_formatado[chave]}")
    
    print(f"Comprimento:")
    comprimento = resultados["comprimento"]
    print(f"    Sua senha: {comprimento}")
    print(f"    Mínimo: 8")
    print(f"    Ideal: 12\n")

    print(f"=== Score Final ===\n")
    
    score = resultados["score"]
    if score <= 2:
        print(f"Score: {score}/6 - FRACA 🔴\n")
    elif score <= 4:
        print(f"Score: {score}/6 - MÉDIA 🟡\n")
    else:
        print(f"Score: {score}/6 - FORTE 🟢\n")

    print("===================\n")

def menu_principal():
    print("=== VERIFICADOR DE SENHAS ===")
    while True:
        try:
            senha = input("Digite sua Senha: ")
            resultado = verificar_forca(senha)
            exibir_resultado(resultado)
            r = input("Deseja testar outra? (S/N) ").lower()
            while r not in ("s", "n"):
                print("Resposta Inválida!")
                r = input("Deseja testar outra? (S/N) ").lower()

            if r == "n":
                print("\nSaindo...")
                break
        except EXCECOES:
            print("\nSaindo...")
            break