print("=========================")
print("  C A L C U L A D O R ")
print("        D E     ")
print("     M E D I A    ")
print("=========================")

nome = input("Qual seu nome? ")
materia = input("Qual o nome da matéria? ")
n1 = int(input("Digite a nota do Primeiro Bimestre: "))
n2 = int(input("Digite a nota do Segundo Bimestre: "))
n3 = int(input("Digite a nota do Terceiro Bimestre: "))
n4 = int(input("Digite a nota do Quarto Bimestre: "))

media = (n1 + n2 + n3 + n4) / 4
if n1 < 7:
    print(nome, "Voce foi REPROVADO. Sua média em ", materia, " foi", media)
elif n2 < 7:
    print(nome, "Voce foi REPROVADO. Sua média em ", materia, " foi", media)
elif n3 < 7:
    print(nome, "Voce foi REPROVADO. Sua média em", materia, " foi", media)
elif n4 < 7:
    print(nome, "Voce foi REPROVADO. Sua média em ", materia, " foi", media)

else:
    print("Voce foi APROVADO Sua média em ", materia, " foi", media)
