import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializa a variável palpite
palpite = 0

# Loop principal do jogo
while palpite != numero_secreto:
    # Lê o palpite do jogador
    palpite = int(input("Digite seu palpite (entre 1 e 100): "))

    # Verifica se o palpite é maior, menor ou igual ao número secreto
    if palpite > numero_secreto:
        print("Tente um número menor.")
    elif palpite < numero_secreto:
        print("Tente um número maior.")

# Mensagem de parabéns quando o jogador acerta
print(f"Parabéns!! Você acertou o número secreto: {numero_secreto}")
