#Um Word Square é um conjunto de palavras escritas em uma grade quadrada, de forma que as mesmas palavras
# possam ser lidas tanto horizontal quanto verticalmente. O número de palavras, igual ao número de letras de cada palavra, é conhecido como ordem do quadrado.
#Dada uma sequência de várias letras maiúsculas, chamado letters, verifique se um Word Square pode ser formado a partir dela.
# Observe que você deve usar cada letra do letters o número exato de vezes que ela ocorre na string. 
# Se um Word Square puder ser formado, retorne true, caso contrário, retorne false.

def isPerfectSquare(n):
    # Função para verificar se n é uma raiz quadrada perfeita
    raiz = int(n**0.5)
    return raiz * raiz == n


def WordSquare(letters):
    n = len(letters)

    # Verifique se o comprimento é uma raiz quadrada perfeita
    if not isPerfectSquare(n):
        return False

    tamanho = int(n**0.5)

    # Crie um array bidimensional
    quadrado_palavras = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]

    # Preencha o array bidimensional com as letras da string
    for i in range(tamanho):
        for j in range(tamanho):
            quadrado_palavras[i][j] = letters[i * tamanho + j]

    # Verifique se as palavras nas linhas são iguais às palavras nas colunas
    for i in range(tamanho):
        palavra_linha = ''.join(quadrado_palavras[i])
        palavra_coluna = ''.join(
            quadrado_palavras[j][i] for j in range(tamanho))
        if palavra_linha != palavra_coluna:
            return False

    return True


# Exemplos de uso:
letras1 = "SATORAREPOTENETOPERAROTAS"
print(WordSquare(letras1))  # Deve imprimir True

letras3 = "NOTSQUARE"
print(WordSquare(letras3))  # Deve imprimir False