
a = float(input('Informe a Variavel A: '))
b = float(input('Informe a Variavel B: '))
c = float(input('Informe a Variavel C: '))

lados = [a, b, c]
lados.sort(reverse = True) # Tive ir atrás de algo para fazer essa converção, então essa parte do codigo não fui eu que fiz!

a, b, c = lados

if a >= b + c:
    print(f'As variaveis {a}, {b} e {c} fornecidas não podem formar um Triangulo!')
elif a**2 == b**2 + c**2:
    print('Triangulo Retangulo!')
elif a**2 > b**2 + c**2:
    print('Triangulo Obtusangulo!')
elif a**2 < b**2 + c**2:
    print('Triangulo Acutangulo!')
elif a == b == c:
    print('Triangulo Equilatero!')
elif a == b or b == c or a == c:
    print('Triangulo Isosceles!')