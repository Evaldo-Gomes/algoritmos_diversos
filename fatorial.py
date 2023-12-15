# Fatorial

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

# Teste Fatorial

print(f'\n {5}! = {fatorial(5)}')