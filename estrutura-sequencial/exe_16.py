import math

print('----- Cálculo de Tintas -----')
area = float(input('Insira a área a ser pintada: '))
liters = area / 3
tin = liters / 18

print(f'Latas de tintas: {tin:.2f} \t\t->\t Valor: R${(math.ceil(tin) * 80):.2f}')