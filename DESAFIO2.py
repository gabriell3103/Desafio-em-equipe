# Escreva um algoritmo que pegue um array e mova todos os zeros para o final, preservando a ordem dos outros elementos

def move_zeros(lista: list) -> list:
    for i in range(0, len(lista)):
       if lista[i] == 0:
           zero = lista.pop(i)
           lista.append(zero) 
    return lista


lista = [4, 0, 3.5, -3.5, 4, 0, -5, 975]
print(move_zeros(lista))