# Escreva uma função chamada sum_intervals que aceite uma matriz de intervalos e retorne a soma de todos os
# comprimentos dos intervalos. Os intervalos sobrepostos devem ser contados apenas uma vez.

def sum_intervals(intervalos):
    # Ordenar os intervalos com base no início do intervalo
    intervalos_ordenados = sorted(intervalos, key=lambda x: x[0])

    # Inicializar a variável para armazenar a soma dos comprimentos dos intervalos
    comprimento_total = 0

    # Inicializar as variáveis para armazenar o intervalo atual
    inicio_atual, fim_atual = intervalos_ordenados[0]

    # Iterar sobre os intervalos
    for intervalo in intervalos_ordenados[1:]:
        inicio, fim = intervalo

        # Verificar se os intervalos se sobrepõem
        if inicio <= fim_atual:
            # Atualizar o intervalo atual se houver sobreposição
            fim_atual = max(fim_atual, fim)
        else:
            # Adicionar o comprimento do intervalo atual à soma total
            comprimento_total += fim_atual - inicio_atual

            # Atualizar o intervalo atual para o próximo intervalo não sobreposto
            inicio_atual, fim_atual = inicio, fim

    # Adicionar o comprimento do último intervalo à soma total
    comprimento_total += fim_atual - inicio_atual

    return comprimento_total


intervalos = [
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11]
]

resultado = sum_intervals(intervalos)
print(resultado)