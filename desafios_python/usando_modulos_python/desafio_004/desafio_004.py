"""Desafio 019 proposto pelo Professor Guanabara (Curso Python #08 - Utilizando Módulos)
-> Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido."""
from random import choice
a1 =str(input("Digite o nome do primeiro aluno: "))
a2 =str(input("Digite o nome do segundo aluno: "))
a3 =str(input("Digite o nome do terceiro aluno: "))
a4 =str(input("Digite o nome do quarto aluno: "))
esc= choice((a1,a2,a3,a4)) #choice aceita apenas um argumento, então eles tem que ficar entre parenteses como se fosse uma lista, separados por virgula
print(f"O aluno escolhido para apagar o quadro foi: {esc}")## o f é para mostrar a variavel dentro da string.