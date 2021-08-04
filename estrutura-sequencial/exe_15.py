print('----- Cálculo de Salário -----')
salary = float(input('Insira o salário BRUTO: R$'))
ir = salary * 0.11
inss = salary * 0.08
syndicate = salary * 0.05
net_salary = salary - ir - inss - syndicate

print(f'+ Salário Bruto: \tR${salary:.2f} \n'
      f'- IR (11%): \t\tR${ir:.2f} \n'
      f'- INSS (8%): \t\tR${inss:.2f} \n'
      f'- Sindicato (5%): \tR${syndicate:.2f}\n'
      f'= Salário Líquido: \tR${net_salary:.2f}'
)