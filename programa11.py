# Jogo da senha
senha_correta = "1234A"
tentativa = input("Digite a senha: ")

while tentativa != senha_correta:
    print("Senha incorreta. Tente novamente.")
    tentativa = input("Digite a senha: ")
    
    
print("Senha correta! Acesso permitido.")