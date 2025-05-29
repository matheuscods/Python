"""
Desafio 013 proposto pelo Professor Guanabara (aula #013 - Reajuste Salarial)
-> Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
"""
s=float(input("Digite o seu salário: "))
ns=s+(s*15/100)
print("O valor do seu salário é: {:.2f}\nO seu salário com aumento de 15% é: {:.2f}".format(s,ns))