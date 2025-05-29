"""
Desafio 004 proposto pelo Professor Guanabara (aula 06)
-> Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""
a = input("Digite algo: ")
print(a)
print("O tipo primitivo desse valor é: ", type(a))
print("É numérico? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("Só tem espaços? ", a.isspace())
print("É alfanúmerico? ", a.isalnum())
print("Está em minúsculas? ", a.islower())
print("Está em maiúsculas? ", a.isupper())
print("Está capitalizada? ", a.istitle)