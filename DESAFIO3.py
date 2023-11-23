# Escreva uma função que gire uma matriz bidimensional (uma matriz) no sentido horário ou anti-horário em 90 graus e retorne a matriz girada.
# A função aceita dois parâmetros: uma matriz e uma string especificando a direção ou rotação. A direção será "clockwise" ou "counter-clockwise"

def rotate_matriz(matriz: list, sentido: str) -> list:
    if sentido == 'clockwise':

    elif sentido == 'counter-clocwise':

    else:
        return print('Esse sentido não existe!')



matriz =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
        ]
sentido = 'clockwise'
print(rotate_matriz(matriz))