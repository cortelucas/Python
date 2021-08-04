print('----- Cálculo de download -----')
file_size = float(input('Insira o tamanho do arquivo de download: '))
internet_speedy = float(input('Insira a velocidade do link da internet: '))

time_calc = ((file_size / internet_speedy) * 60)

print(f'Tempo aproximado de downlaod: {time_calc:.0f} min.')