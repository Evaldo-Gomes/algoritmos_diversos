# Tabuada

def tabuada(x):
    tabuada = []
    for i in range(1, 11):
        tabuada.append(str(x) + ' x ' + str(i) + ' = ' + str(x*i))
    return tabuada

# Pulando uma linha a cada interação
def imprimir_tabuada(tabuada):
    for linha in tabuada:
        print(linha)

# Teste Tabuada

print(imprimir_tabuada(tabuada(2)))