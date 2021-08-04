print('----- Sistema de cobranças -----')
fish_weight = float(input('Insira quantos quilos de peixe: '))
excess = fish_weight - 50
fine = excess * 4

print(f'O valor a pagar é: R${fine:.2f}')