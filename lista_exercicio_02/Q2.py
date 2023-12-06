salario = float(input('informe seu salario'))

parametro = 1250

if salario > parametro:
    aumento = salario * 0.10
    print(f'o aumento é de:{aumento} ')
elif salario <= parametro:
    aumento = salario * 0.15
    print(f'o aumemto é de:{aumento}')
    