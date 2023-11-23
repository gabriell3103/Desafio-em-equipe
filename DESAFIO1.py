# Escreva uma função chamada sum_intervals que aceite uma matriz de intervalos e retorne a soma de todos os
# comprimentos dos intervalos. Os intervalos sobrepostos devem ser contados apenas uma vez.

def sum_intervals(matriz_intervalo: list) -> int:
    soma = 0
    tamanho_matriz = len(matriz_intervalo)
    for i in range(0,tamanho_matriz):
        soma += (matriz_intervalo[i][1] - matriz_intervalo[i][0])
    return soma


matriz = [
    [1, 4],
    [7, 10],
    [3, 5]
]

print(sum_intervals(matriz))


