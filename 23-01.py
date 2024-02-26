def contarCaracteres(texto):
    return len(texto)

def contarPalavras(texto):
    return len(texto.split())

while True:
    print("Escolha uma Opção: ")
    print("1. Contar Caracteres")
    print("2. Contar Palavras")
    print("3. Sair.")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        texto = input("Digite o texto: ")
        resultado = contarCaracteres(texto)
        print(f"O número de caracteres é de: {resultado}")

    elif escolha == "2":
        texto = input("Digite o texto: ")
        resultado = contarPalavras(texto)
        print(f"O número de palavras é de: {resultado}")
    
    elif escolha == "3":
        print("Programa encerrado! Bye!")
        break

    else:
        print("Opção inválida. Escolha novamente!")



        



        
    