from .checker import *

def exibir_resultado(resultados):
    print(f"=== ANÁLISE DE FORÇA ===\n")
    print(f"Critérios:")
    for chave, valor in resultados.items():
        if isinstance(valor, bool):
            emoji = "✅" if valor else "❌"
            print(f"{chave}: {emoji}")
    print(f"Comprimento:")
    comprimento = resultados["comprimento"]
    print(f"Sua senha: {comprimento}")
    print(f"Minimo: 8")
    print(f"Ideal: 12")

    print(f"=== Score Final ===\n")
    
    score = resultados["score"]
    if score <= 2:
        print(f"Score: {score}/6 - FRACA 🔴")
    elif score <= 4:
        print(f"Score: {score}/6 - MÉDIA 🟡")
    else:
        print(f"Score: {score}/6 - FORTE 🟢")

    print("=====================================")

def menu_principal():
    while True:
        senha = input("Digite sua Senha: ")
        resultado = verificar_forca(senha)
        exibir_resultado(resultado)
        r = input("Deseja testar outra? (S/N)").lower()
        if r == "s":
            continue
        elif r == "n":
            break
        else:
            print("Resposta Invalida!")