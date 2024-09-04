entrada= input('Qual o seu nome?')

quantidade= len(entrada)


if quantidade <= 4:
    print(f'Seu nome possui {quantidade} letras e seu nome é pequeno.')
elif (quantidade >= 5) and (quantidade < 6):
    print(f'Seu nome possui {quantidade} letras e seu nome é médio.')
elif quantidade > 6:
    print(f'Seu nome possui {quantidade} letras e seu nome é muito grande.')