a = float(input("defina a variavel, a:"))
b = float(input("defina a variavel, b:"))
c = float(input("defina a variavel, c:"))
if a > b and a > c:
    print(f'o maior numero é:{a}')
elif b > a and b > c:
    print(f'o maior numero é:{b}')
elif c > a and c > b:
    print(f'o maior numero é:{c}')


if a < b and a < c:
    print(f'o menor numero é:{a}')
elif b < a and b < c:
    print(f'o menor numero é:{b}')
elif c < a and c < b:
    print(f'o menor numero é:{c}')