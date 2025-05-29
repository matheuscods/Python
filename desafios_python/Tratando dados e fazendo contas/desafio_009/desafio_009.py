"""
Desafio 011 proposto pelo Professor Guanabara (aula 07 - Operadores aritméticos)
-> Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
pinta uma área de 2m²
"""
l= int(input("Digite a largura da parede em metros: "))
a=int(input("DIgite a altura da parede em metros: "))
ar= a*l
lt= ar/2
print("A largura da parede é: {}m\nA altura da parede é de: {}m\nA área da parede é de: {}m²\nA quantidade em litros de tinta necessária para pintar a parede é de: {}L".format(l,a,ar,lt))