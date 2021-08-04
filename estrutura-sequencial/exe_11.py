integer_01 = int(input('Insira um número inteiro: '))
integer_02 = int(input('Insira mais um número inteiro: '))
real = float(input('Agora insira um número real: '))

print(f'o produto do dobro do primeiro com metade do segundo = {(integer_01 * 2) * (integer_02 / 2)} \n'
      f'a soma do triplo do primeiro com o terceiro = {((integer_01 * 3) + real)} \n'
      f'o terceiro elevado ao cubo = {real * real * real}')