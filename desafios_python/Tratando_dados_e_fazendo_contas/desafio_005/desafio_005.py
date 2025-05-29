"""
Desafio 007 proposto pelo Professor Guanabara (aula 07 - Operadores aritméticos)
-> Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
m= (n1+n2+n3) / 3
print("A primeira nota do aluno foi: {}\nA segunda nota do aluno foi: {}\nA terceira nota do aluno foi: {}\nA média do aluno é: {}".format(n1,n2,n3,m))
