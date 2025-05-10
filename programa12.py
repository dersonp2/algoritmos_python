#jogo de advinhação
import random
numero_secreto = random.randint(1,10)
tentativas = 0
print("Bem-vindo ao jogo de adivinhação!")

while True:
    palpite = int(input("Digite um número entre 1 e 10: "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
        break