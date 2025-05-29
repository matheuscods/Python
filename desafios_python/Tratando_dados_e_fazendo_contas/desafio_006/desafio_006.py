"""
Desafio 008 proposto pelo Professor Guanabara (aula 07 - Operadores aritméticos)
-> Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
"""
n= float(input("Digite o valor em metros: "))
c= n*100
m = c*10
print("{} metros é igual á {} centímetros e {} centímetros é igual à {} milimetros".format(n,c,c,m))
