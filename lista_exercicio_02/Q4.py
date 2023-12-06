a = int(input('qual a distância você deseja percorrer?'))
if a <= 200 :
    print(f'o preço da passagem custando 0.50 por km é: {a * 0.50}')
elif a > 200 :
    print(f'o preço da passagem custando 0.50 por km é: {a * 0.45}')


