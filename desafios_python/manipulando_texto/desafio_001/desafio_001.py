"""Desafio 022 proposto pelo Professor Guanabara (Curso Python #09 - Manipulando Texto)
-> Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas
-O nome com todas minúsculas
-Quantas letras ao todo (sem considerar espaços).
-Quantas letras tem o primeiro nome."""

nome=str(input("Digite seu nome: ")).strip()
nse = nome.replace(" ", "") #Substitui os espaços por uma string vazia
pn= nome.split()[0]#Dividi em listas e puxei o indice 0, que será o primeiro item da lista
print("Seu nome em maiúsculas é: {}".format(nome.upper()))
print("Seu nome em minúsculas é: {}".format(nome.lower()))
print("Seu nome tem {} letras.".format(len(nse)))
print("Seu primeiro nome tem {} letras.".format(len(pn)))