"""
Desafio 006 proposto pelo Professor Guanabara (aula 07 - Operadores aritméticos)
-> Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada.
"""
n1= int(input("Digite um número: "))
dob= int(n1*2)
triplo=int(n1*3)
raiz=n1**(1/2)
print("O dobro de {} é igual à {}\nO triplo de {} é igual à {}\nA raiz quadrada de {} é igual à {:.3f}".format(n1,dob,n1,triplo,n1,raiz)) #{:.3f} é para mostrar apenas 3 casas depois do ponto.