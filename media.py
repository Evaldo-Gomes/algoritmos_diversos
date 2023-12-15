# Média

def media(valores):
    soma = 0
    for i in range (0, len(valores)):
        soma += valores[i]
    return soma/len(valores)

# Teste Média
# Lista Valores
x = [2, 3, 4, 5, 6]

# Saída
print('A média de ', end='')
for valor in x:
    print(f' {valor} ', end='')
print(' é {:.0f}'.format(media(x)))