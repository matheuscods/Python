"""Desafio 024 proposto pelo Professor Guanabara (Curso Python #09 - Manipulando Texto)
->Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""
c=str(input("Digite o nome de uma cidade: ")).strip().upper()
print(c[:5] == 'SANTO')


