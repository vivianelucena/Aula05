cont = 0
for x in range(1, 10, 1):
    valor = int(input(f'Digite um valor: '))
    if valor < 0:
        print(cont)
        cont = cont + 1
print(cont)