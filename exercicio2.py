nome= input('Qual o seu nome?')
idade= input("Qual sua idade?")

if (nome != '') and (idade != ''):
    print(f'seu nome é: {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome NÃO contém espaços')

    print (f'sua idade é: {idade}')
    print (f'seu nome contém {len(nome)} letras')
    print (f'a primeira letra do seu nome é : {nome[0]}')
    print (f'a última letra do seu nome é: {nome[-1]}')
else: 
    print("Desculpe, você deixou campos vazios.")    