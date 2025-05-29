##Aprendendo operadores aritméticos em Python
"""
+ é adição -> 5+2 == 7
- é subtração -> 5-2 == 3
* é multiplicação -> 5*2 == 10
/ é divisão -> 5/2 == 2.5
** é potência -> 5**2 == 25
// é divisão inteira -> 5//2 == 2
% é resto da divisão -> 5%2 == 1
"""
##Também temos a ordem de precedência
"""
1 lugar -> ()
2 lugar -> ** 
3 lugar -> *, /, //, %
4 lugar -> +, -
"""
##Alguns operadores aritméticos podem funcionar com strings também.
print('Oi'+'Olá') #vai concatenar;
print('Oi'*5) #vai printar 'Oi' 5 vezes;
##Também podemos alinhar, adicionar espaços etc...
nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) #o nome vai vai ganhar 20 espaços de diferença
print('Muito bom te ver {:>20}!'.format(nome)) #agora vai aparecer à 20 caractéres e alinhou à direita
print('Muito legal te ver {:<20}!'.format(nome)) #agora vai aparecer à 20 caractéres e alinhou à esquerda
print('QUe alegria em te ver {:^20}!'.format(nome)) #agora vai aparecer à 20 caracteres e centralizou
print('Você é muito divertido(a) {:=^20}!') #agora vai aparecer à 20 caracteres e centralizar entre =
##Vamos praticar alguns operadores aritméticos:
n1=input('Digite um valor: ')
n2=input('Digite outro valor: ')
soma= n1+n2
mult= n1*n2
divi= n1/n2
resdivi= n1//n2
poten= n1**n2
print('A soma é: {}, o produto é: {}, e a divisão é: {}'.format(soma,mult,divi))
print('A divisão inteira é: {} e potência é: {}'.format(resdivi,poten))
