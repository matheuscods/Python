"""Desafio 023 proposto pelo Professor Guanabara (Curso Python #09 - Manipulando Texto)
->Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""
n=int(input("Digite um número de 0 a 9999:"))
u= n// 1 % 10
d= n // 10 % 10
c= n // 100 % 10
m= n // 1000 % 10
print("número: {}\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(n,u,d,c,m))