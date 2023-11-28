# Escreva uma função que gire uma matriz bidimensional (uma matriz) no sentido horário ou anti-horário em 90 graus e retorne a matriz girada.
# A função aceita dois parâmetros: uma matriz e uma string especificando a direção ou rotação. A direção será "clockwise" ou "counter-clockwise"

def girar_matriz(matriz: list, direcao: str) -> list:
    if not matriz or not matriz[0]:
        return matriz

    linhas, colunas = len(matriz), len(matriz[0])

    # Criar uma matriz vazia do mesmo tamanho para armazenar o resultado
    matriz_resultante = [[0] * colunas for _ in range(linhas)]

    if direcao == "clockwise":
        for i in range(linhas):
            for j in range(colunas):
                matriz_resultante[j][linhas - 1 - i] = matriz[i][j]
    if direcao == "counter-clockwise":
        for i in range(linhas):
            for j in range(colunas):
                matriz_resultante[colunas - 1 - j][i] = matriz[i][j]

    return matriz_resultante


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


girada_horario = girar_matriz(matriz, "clockwise")
girada_anti_horario = girar_matriz(matriz, "counter-clockwise")


print("Rotação no sentido horário:")
for linha in girada_horario:
    print(linha)

print("\nRotação anti-horária:")
for linha in girada_anti_horario:
    print(linha)