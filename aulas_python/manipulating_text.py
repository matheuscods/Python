###Aprendendo a manipular texto em Python!
"""

[C][U][R][S][O][ ][P][Y][T][H][O][N]
 0  1  2  3  4  5  6  7  8  9 10 11

 frase = 'CURSO PYTHON'

 #Quando você atribui uma string, o python vai atribuir essa frase dentro da memória do computador, cortando a frase em mini espaços começando apartir do zero, como o ex acima
 -> Cada um desses mini espaços vai receber um indice, ou seja, o caracter 'C' recebe o indice zero
 -> Os espaços nas frases também contam como um caracter, como é o caso do inidice 5
 -> O python é case sensitive, ou seja, C maiúsculo não é a mesma coisa que c minúsculo.

 #Com isso, o python permite algumas operações como:
 -> Fatiamento: Fatiar uma string, é pegar um pedaço dela.
    frase[9] -> Aqui estou puxando apenas o indice 9 da lista, ou seja, o caracter H

    frase[0:4] -> Essa maneira de fatiamento, só vai pegar o caracter entre 1 e 4, excluindo o caracter 4, então só vai pegar C(0),U(1),R(2),S(3).
        Caso eu queira pegar até o indice 4, eu tenho que fazer frase[0:5], pois ele exclui o ultimo indice, ou seja, C(0),U(1),R(2),S(3),O(4) -> Excluindo o espaço(5)

    frase[0:6:2] -> Assim, ele vai contar de dois em dois, ou seja, vai pular o indice 0,1 e vai pegar o 2(R), vai pular o 3 e 4, e mostrar o 5(espaço)

    frase[:5] -> Quando você omite onde ele vai começar, ele sempre vai começar do indice 0

    frase[1:] -> Quando você omite onde ele vai terminar, ele vai começar de onde você colocou o inicio, nesse caso o 1, e vai até o final da frase.

    frase[9::3] -> Besse exemplo, eu falei onde vai começar (9), omiti onde vai terminar então ele vai até o final, e coloquei para pular de 3 em 3.

-> Análise: Analisar uma string é saber algumas informações dela como: QUal o tamanho dela, quando ela termina, quando ela acaba, qual a primeira palavra inteira, etc..
    len(frase) -> Vai mostrar o comprimento da string, quantos caracteres ela tem nela, no exemplo acima temos o valor 12. Porque começa do 0 e vai até o 11, totalizando 12

    frase.count('O') -> Nessa funcionalidade, estou pedindo para que o python conte quantas vezes aparece a letra O maiúscula na frase.
        frase.count('O',0,12) -> POsso fazer a contagem já com o fatiamento, basicamente estou pedindo para contar quantos O tem do indice 0 até o 12.

    frase.find('CURSO') -> Vai te dizer em que indice começou o 'CURSO' dentro da string, ou seja, indice 0.

    'CURSO' in frase -> Vai perguntar se a palavra curso existe na string, retornando true ou false. Nesse caso, vai ser TRUE.

-> Transformação: Uma lista de string é imutável, mnão podemos mexer diretamente nos elementos, mas podemos mudar através de métodos.
    frase.replace('PYTHON','LINUX') -> vai procurar por PYTHON e vai substituir por 'LINUX'

    frase.upper() -> Vai manter os maísculos e deixar as letras minúsculas em maiúsculas.

    frase.lower() -> O contrário do upper, vai manter as minúsculas e transformar as maiúsculas em minuscúlas.

    frase.capitalize() -> Vai jogar tudo pra minúsculo e a primeira em maiúscula. Exemplo> 'Curso python'

    frase.title() -> Vai analisar quantas palavras tem na string apartir da posição dos espaços, e depois vai fazer o capitalize em cada palavra, palavra por palavra.

    frase.strip() -> Vai remover todos os espaços inúteis no início e no final da string.
    frase.rstrip() -> right strip, vai remover os espaços inúteis da direita.
    frase.lstrip() -> left strip, vai remover os espaços inúteis da esquerda.

-> Divisão: você também pode dividir strings.
    frase.split() -> o split é feito nos espaços, vai ocorrer uma divisão na string considerando os espaços, pegando onde tiver espaços e criando uma divisão
        O split refaz os indices, fazendo com que cada palavra receba uma indexação nova, colocando cada uma das palavras dentro de uma nova lista.
    
->Junção: De forma analoga ao split, temos a junção. Após fazer o split, você pode também fazer a junção dessas listas criadas apartir do split.
    '-'.join(frase) -> Vai gerar uma string unica apartir do split, juntando as palavras das listas separadas. EX: 'CURSO-PYTHON'
        você pode colocar qualquer coisa dentro disso, ou seja, se você tivesse feito '.'.join(frase) seria 'CURSO.PYTHON'
    

"""

