##Aprendendo tipos primitivos e saída de dados!
"""
int = 3, 4, 5 etc.. (números inteiros)
float = 4.5, 0.076 (números reais, de ponto flutuante)
bool = True | False (verdadeiro ou falso, 1 ou 0)
str = 'batata', '8.5', '' (é uma string, uma palavra )
"""
#neste exemplo, a saída vai ser uma string;
n1 = input('Digite um valor: ')
print(type(n1))
#já nesse, como declarei como inteiro, vai ser int! EU poderia fazer essa conversão com qualquer outro tipo primitivo, como str, float ou bool.
n2 = int(input('Digite outro valor: '))
print(type(n2))
#Eu também posso perguntar outras coisas e testar tipos como:
n = input('Digite algo')
print(n.isnumeric()) #Ele pode ser convertido para númerico ou int?
print(n.isalpha())   #Ele é uma letra?
print(n.isalnum)     #Ele é alfabético e númerico? Alpha númerico
print(n.isupper)      #Está em maiúsculo?
#Agora, vamos somar! Nesse print, usei o .format, ele permite a substituição dos {} para um valor já declarado antes.
ns1 = int(input('Digite um valor: '))
ns2 = int(input('Digite outro valor: '))
s = ns1 + ns2
print('A soma entre {} e {} vale {}'.format(ns1,ns2,s))
