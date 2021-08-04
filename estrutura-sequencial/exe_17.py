import math

M2_PER_LITER = 6
GALLON_PRICE = 80
GALLON_LITER = 18
TIN_PRICE = 25
TIN_LITER = 3.6
SECURITY_MARGIN = 1.1

print('----- Cálculo de Tintas -----')
area = float(input('Insira a área a ser pintada: '))

consumption_per_liter = (area / M2_PER_LITER) * SECURITY_MARGIN

gallon_amount_only = math.ceil(consumption_per_liter / GALLON_LITER)
gallon_value_only = gallon_amount_only * GALLON_PRICE

tin_amount_only = math.ceil(consumption_per_liter / TIN_LITER)
tin_value_only = tin_amount_only * TIN_PRICE

mixed_gallon_amount = consumption_per_liter // GALLON_LITER
mixed_tin_amount = math.ceil((consumption_per_liter - mixed_gallon_amount * GALLON_LITER) / TIN_LITER)
mixed_gallon_value = mixed_gallon_amount * GALLON_PRICE
mixed_tin_value = mixed_tin_amount * TIN_PRICE

print(f'\nConsumo de tinta: {consumption_per_liter:.2f} lt\n'
      f'\nQuantidade de galões de 18lt: {mixed_gallon_amount:.0f}'
      f'\nValor total de galões de 18lt: R$ {gallon_value_only:.2f}\n'
      f'\nQuantidade de latas de 3,6 lt: {mixed_tin_amount:.0f}'
      f'\nValor total de latas de 3,6 lt: R$ {tin_value_only:.2f}\n'
      f'\n-----------------------------------\n'
      f'\n- Quantidade de galões: \t\t{mixed_gallon_amount:.0f}'
      f'\n- Quantidade de latas: \t\t{mixed_tin_amount:.0f}'
      f'\n- Quantidade total mista: \t{mixed_gallon_amount + mixed_tin_amount:.0f}'
      f'\n'
      f'\n- Valor total: \t\t\tR$ {mixed_gallon_value + mixed_tin_value:.2f}'
)