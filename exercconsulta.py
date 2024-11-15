import os

while True:
    valor_parcelas= float(input("Qual o valor das parcelas?"))
  

    quantidade_parcelas= int(input("Em quantas parcelas o veículo foi financiado? "))
    print("")

    Valor_total= valor_parcelas * quantidade_parcelas

    print(f'Valor total do financiamento: R${Valor_total:,.2f}')

    print("")
    parcelas_pagas= int(input("Quantas parcelas foram pagas? "))
    print("")

    falta_parcelas= quantidade_parcelas-parcelas_pagas

    falta_valor= valor_parcelas * falta_parcelas

    print("")
    print(f'Saldo devedor total: R${falta_valor:,.2f}')

    print("")
    banco= input("Selecione o banco onde foi realizado o financiamento: 1-Santander, 2-Bradesco, 3-Itaú, 4-Pan, 5-omini, 6-Honda, 7-Yamaha. ")

    if banco== '1':
        abatimento= (falta_valor*70)/100
    elif banco == '2':
        abatimento= (falta_valor*70)/100
    elif banco == '3':
        abatimento= (falta_valor*70)/100
    elif banco == '4':
        abatimento= (falta_valor*60)/100
    elif banco == '5':
        abatimento= (falta_valor*60)/100
    elif banco == '6':
        abatimento= (falta_valor*50)/100
    elif banco == '7':
        abatimento= (falta_valor*60)/100
    
        
    quitaca_minima= falta_valor - abatimento

    print("")
    print(f'Saldo devedor total: R${falta_valor:,.2f}')
    print("")
    print(f'Quitação máxima: R${quitaca_minima:,.2f} abaixo')
    print("")
    print(f'Economia de: R${abatimento:,.2f}')
    print("")

    saida= input("Deseja encerrar a simulação? ").lower()


    if saida == "sim":
        os.system("cls")
        break
    else:
        continue

    # quitação máxima se refere ao valor máximo que o cliente irá pagar, ou seja, ele não pagará acima daquele valor