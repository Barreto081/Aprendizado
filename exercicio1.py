primeiro_valor = input("Digite um número: ")
segundo_valor = input("Digite outro número: ")

if primeiro_valor > segundo_valor:
    print (f'{primeiro_valor=} é maior que o {segundo_valor=}')
elif segundo_valor > primeiro_valor: 
    print (f'{segundo_valor=} é maior que o {primeiro_valor=}')
elif primeiro_valor == segundo_valor: 
    print (f"{primeiro_valor=} é igual ao {segundo_valor=}")    