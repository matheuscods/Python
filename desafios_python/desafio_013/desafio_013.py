"""
Desafio 015 proposto pelo Professor Guanabara (aula #015 - Aluguel de Carros)
-> Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 0.15 reais por km rodado.
"""
kmp=float(input("Quantos KM você percorreu com o carro? "))
dias=int(input("QUantos dias o carro foi alugado? "))
p=(kmp*0.15)+(dias*60)
print("Você percorreu {}KM com o carro. Você alugou ele por {} dias. O preço total à se pagar é: R${:.2f}".format(kmp,dias,p))