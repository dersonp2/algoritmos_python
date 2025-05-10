# aprovação escolar
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1 + nota2) / 2

# se a media for maior ou igual a 7, entao o aluno foi aprovado
# senao, o aluno foi reprovado
print("A sua Média foi: ", media)
if media >=7:
    print("Aprovado")
else:
    print("Reprovado")