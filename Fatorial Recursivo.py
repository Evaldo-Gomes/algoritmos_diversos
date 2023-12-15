# Fatorial recursivo

def fat_recursivo(n):
    if n > 1:
        fat = n * fat_recursivo(n - 1)
        return fat
    else: return 1

# Teste Fatorial Recursivo

print(f'{5}! = {fat_recursivo(5)}')