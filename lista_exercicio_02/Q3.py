print('''informe o tipo de usuario pela sigla;
Residencial (R)
Comercial (C)
Industrial (I)''')
tipo = (input('sua resposta:'))
energia = int(input('informe a quantidade de energia gasta (kwh)'))

match tipo:
    case 'R':
        if energia <= 500:
            resi = energia * 0.40
            print(f'voce deve pagar {resi} de energia!')
        elif energia > 500:
            resi = energia * 0.65
            print(f'voce deve pagar {resi} de energia!')
    case 'c':
        if energia <= 1000:
            come = energia * 0.55
            print(f'voce deve pagar {come} de energia!')
        elif energia > 1000:
            come = energia * 0.60
            print(f'voce deve pagar {come} de energia!')
    case 'i':
        if energia <= 5000:
            indu = energia * 0.55
            print(f'voce deve pagar {indu} de energia!')
             
                                         