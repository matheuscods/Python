"""
Desafio 012 proposto pelo Professor Guanabara (aula 07 - Operadores aritméticos)
-> Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
"""
p= float(input("Digite o preço do produto: "))
vd= p*0.05
d= p - vd
print("O preço do produto é: {} reais\nO valor do desconto é: {} reais\nO novo preço com desconto é: {} reais".format(p,vd,d))

"""
GUanabara fez de um jeito diferente:
preço = float(input('QUal o preço do produto?))
novo = preço - (preço*5/100)
"""