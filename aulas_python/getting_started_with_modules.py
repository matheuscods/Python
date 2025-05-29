###Aprendendo a usar módulos no Python!###
"""
para importar uma biblioteca você tem que usar import. Vamos usar de exemplo a biblioteca math, que já vem com o python.

import math --> No inicio do seu código, quando você for importar sua biblioteca, você fará dessa forma. Porém você vai importar todos os recursos dessa biblioteca, o que
pode acabar consumindo mais memória do que o necessário se você precisar de apenas uma funcionalidade dessa biblioteca.

Por exemplo, temos na biblioteca math, algumas funcionalidades como:
ceil -> faz um arredondamento para cima
floor -> faz um arredondamento para baixo
trunc -> vai 'truncar' o número, ou seja, eliminar da virgula para frente, sem fazer arredondamento nenhum
pow -> função power, potência, funciona de maneira semelhante aos *
sqrt -> calcula a raiz quadrada, squareroot
factorial -> calculo fatorial de um número

Vamos supor que você quer importar apenas uma dessas funcionalidades dessa biblioteca, sem importar tudo você pode usar:
from math import sqrt -> dessa forma, você vai importar apenas a funcionalidade de squareroot, diminuindo a memória que você utilizaria se importasse TUDO, otimizando.
Da mesma forma, você pode importar mais de uma, se você precisar:
from math import sqrt,ceil -> Agora você está importando duas funcionalidades dessa biblioteca, podendo utilizar SOMENTE elas, já que você chamou apenas elas.
"""
##Agora vamos testar.##
"""
import math #Importei toda a biblioteca math, como no primeiro exemplo.
num = int(input("Digite um número: "))
raiz= math.sqrt(num) #quando você importa toda a biblioteca, todas as funcionalidades vão estar disponíveis para você usar, porém, fica menos otimizado, pois consome mais memória.
print("A raíz de {} é igual a {}".format(num, math.ceil(raiz))) #Também podemos chamar dentro do format, por exemplo. Aqui vai arredondar a raiz para cima.
"""
##Agora vamos testar da segunda forma, chamando apenas funcionalidades especificas da biblioteca.##
from math import sqrt, floor #importei apenas as funcionalidades sqrt(raiz) e floor(arredondar para baixo)
num = int(input("Digite um número: "))
raiz=sqrt(num)
print("A raíz de {} é igual à {:.2f}".format(num,floor(raiz))) #Novamente chamei o floor dentro do format

##Você pode usar outras bibliotecas quem com o python3 se quiser, acessando o python.org -> documentação -> selecione a versão do python -> Library Reference | PYpi
##Você pode explorar muita coisa no site do python, tanto bibliotecas, tanto sintaxe, e outras coisas. Por exemplo, vamos importar outra biblioteca, a random.
import random
#num = random.radom() -> O metódo random da classe random gera um número float aleatório entre 0 e 1
num = random.randint(1,10) #Você também pode gerar um número aleatório inteiro com o randint, nesse exemplo vai ser um número int de 1 até 10
print(num)