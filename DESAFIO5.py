# Escreva uma função que conte quantas maneiras diferentes você pode fazer troco por uma quantia de dinheiro, dada uma série de denominações de moedas.
# Por exemplo, existem 3 maneiras de dar troco por 4 se você tiver moedas com denominação 1 e 2

def count_change(money, coins):

    maneiras = [1] + [0] * (money + 1)

    for coin in coins:

        for i in range(coin, money + 1):

            maneiras[i] += maneiras[i - coin]

    return maneiras[money]

dindin = 4
moeditchas = [1, 2]
# dindin = 10
# moeditchas = [5, 2, 3]
# dindin = 11
# moeditchas = [5, 7]
dividindo_moedas = count_change(dindin, moeditchas)
print(dividindo_moedas)