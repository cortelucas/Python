import math

print('----- Área de um círculo -----')
radius = float(input('Insira o raio do circulo: '))
circle_area = (math.pi * (radius * radius))

print(f'A área do círculo é {round(circle_area, 2)} m².')