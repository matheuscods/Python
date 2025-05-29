"""Desafio 014 proposto pelo Professor Guanabara (aula #014 - Conversor de Temperatura)
-> Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
"""
c=float(input("Digite a temperatura em ⁰C: "))
f=(c*9/5)+32
print("A temperatura de {} ⁰C convertida em ⁰F é de {}⁰F".format(c,f))