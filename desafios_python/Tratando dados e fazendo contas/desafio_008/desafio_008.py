"""
Desafio 010 proposto pelo Professor Guanabara (aula 07 - Operadores aritméticos)
-> Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (dolar a 5.69)
"""
n=float(input("Digite quantos reais você tem na carteira: "))
d= n/5.69
print("Você tem {} reais na carteira. Convertido para dolar para dolar dá: {:.3f} dolares".format(n,d))