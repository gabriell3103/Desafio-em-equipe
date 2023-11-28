# Escreva um algoritmo que pegue um array e mova todos os zeros para o final, preservando a ordem dos outros elementos

def move_zeros(arr):
    zeros = []

    for num in arr:
        if num != 0:
            zeros.append(num)

    zeros.extend([0] * (len(arr) - len(zeros)))

    return zeros


array = [0, 5, 31, 0, 9, 0, 0, 10, 50]
resultado = move_zeros(array)
print(resultado)