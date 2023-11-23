# Escreva uma função que faça uma lista de strings representando todas as maneiras pelas quais você pode “equilibrar” n pares de parênteses

def balanced_parens(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['()']

    resultado = []
    for i in range(n):
        for esquerda in balanced_parens(i):
            for direita in balanced_parens(n - 1 - i):
                resultado.append(f'({esquerda}){direita}')

    return resultado

n = 4
parenteses = balanced_parens(n)
print(parenteses)