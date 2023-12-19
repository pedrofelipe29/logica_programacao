def numeros_pares_ou_impares(valor, escolha):
    
    print(f"Números {escolha}s até {valor}:")
    for i in range(1, valor + 1):
        if (escolha == 'par' and i % 2 == 0) or (escolha == 'ímpar' and i % 2 != 0):
            print(i, end=' ')
    print("\n")

valor_usuario = int(input("Digite um valor: "))
escolha_usuario = input("Deseja números pares ou ímpares? (par/ímpar): ")


numeros_pares_ou_impares(valor_usuario, escolha_usuario)

#a.
def multiplicacao(a, b):
    resultado = 0
    
    for _ in range(b):
        resultado += a
    return resultado

#b.
def divisao_inteira_e_resto(dividendo, divisor):
    quociente = 0
    
    while dividendo >= divisor:
        dividendo -= divisor
        quociente += 1
    
    resto = dividendo
    return quociente, resto


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


resultado_multiplicacao = multiplicacao(numero1, numero2)
print(f"A multiplicação de {numero1} por {numero2} é: {resultado_multiplicacao}")


quociente, resto = divisao_inteira_e_resto(numero1, numero2)
print(f"A divisão inteira de {numero1} por {numero2} é: {quociente}")
print(f"O resto da divisão de {numero1} por {numero2} é: {resto}")

