"""Desafio 016 proposto pelo Professor Guanabara (Curso Python #08 - Utilizando Módulos)
-> Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira."""
from math import trunc
num=float(input("Digite um número real qualquer: "))
print("A porção inteira de {} é: {}".format(num,trunc(num)))