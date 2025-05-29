"""Desafio 018 proposto pelo Professor Guanabara (Curso Python #08 - Utilizando Módulos)
-> Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,cosseno e tangente desse ângulo."""
from math import sin,cos,tan,radians #O sin,cos,tan esperam o valor do angulo em radianos, não em graus, por isso temos que converter
ag=float(input("Digite um ângulo qualquer em graus: "))
ar= radians(ag) #converti o angulo de graus para radianos ar-> angulos radianos e ag ->angulos graus
sen= sin(ar)#agora os angulos estao convertidos
coss= cos(ar)
tang= tan(ar)
print("O ângulo {}⁰ tem o seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.".format(ag,sen,coss,tang))