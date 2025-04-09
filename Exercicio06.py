cont10a20 = 0
contacima20 = 0
for x in range(1, 11, 1):
    valor = int(input(f'Digite um valor: '))
    if valor >= 10 and valor <= 20:
        print(f'Entre 10 a 20: {cont10a20}')
        cont10a20 = cont10a20 + 1
        print(valor, end='\n')

    elif valor > 20:
        print(f'Maiores que 20: {contacima20}')
        contacima20 = contacima20 + 1
        print(valor, end='\n')

print(f'Obtivemos {cont10a20} entre 10 e 20.\n'
      f'Obtivemos {contacima20} maiores que 20.')