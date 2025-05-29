"""Desafio 017 proposto pelo Professor Guanabara (Curso Python #08 - Utilizando Módulos)
-> Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa"""
from math import hypot
s=float(input("Digite o cateto oposto: "))
c=float(input("Digite o adjacente: "))
hip= hypot(s,c)
print("O valor da hipotenusa é: {:.2f}".format(hip))