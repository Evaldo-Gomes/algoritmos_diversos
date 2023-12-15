# BubbleSorting - Implementação

# Apresentação
print('\n\t\t\t -- Bubble Sorting -- \n')
n = []

# Entrada
qtd = int(input('Quantos números você deseja ordenar? '))

for i in range(0, qtd):
    n.append(int(input('Informe 0 {}º valor: '.format((i+1)))))

# Processamento
for i in range(0, len(n)-1):
    for j in range((i+1), qtd):
        if n[i] > n[j]:
            swap = n[j]
            n[j] = n[i]
            n[i] = swap

# Saída
for i in range(0, len(n)):
    if i < len(n) + 1:
        print('{}.'.format(n[i]), end='')