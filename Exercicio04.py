n = int(input(f'Digite um número: '))

if n <= 0:
    print(f'Valor {n} inválido!')
else:
    for n in range(1, n + 1, 1):
        print(n, end=" ")