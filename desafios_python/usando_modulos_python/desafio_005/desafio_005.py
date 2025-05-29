"""Desafio 020 proposto pelo Professor Guanabara (Curso Python #08 - Utilizando Módulos)
-> O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
e mostre a ordem sorteada."""
from random import shuffle ##Essa funcionalidade embaralha a ordem dos elementos de uma sequencia
a1 =str(input("Digite o nome do primeiro aluno: "))
a2 =str(input("Digite o nome do segundo aluno: "))
a3 =str(input("Digite o nome do segundo aluno: "))
a4 =str(input("Digite o nome do quarto aluno: "))
esc= [a1,a2,a3,a4]# tem que ser entre colchetes, por que entre () torna imutável, sendo impossível embaralhar.
shuffle(esc)
print(f"A ordem de apresentação dos trabalhos vai ser: {esc}")
