"""
Desafio 005 proposto pelo Professor Guanabara (aula 07 - Operadores aritméticos)
-> Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor
"""
n= int(input("Digite um número: "))
su = n + 1
ant = n - 1
print("O sucessor de {} é: {} e o antecessor de {} é: {}".format(n,su,n,ant))