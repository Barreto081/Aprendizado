lista= [ ]
import os
while True:
    
        print('selecione uma opção: ')

        opcao= input("[i]nserir,[a]pagar,[l]istar,[t]erminar ").casefold()

        if opcao== "t":
            break    
        if opcao == "i":
                
            escolha= input('Digite o produto: ')

            lista.append(escolha)
            
        if opcao== 'l':
            lista_enumerada= list(enumerate(lista))

            os.system('cls')

            for item in lista_enumerada:
                indice,escolha= item
                print(indice, escolha)

        if opcao == "a":
            try:
                apagar=int(input('Qual indice deseja apagar? '))
                lista.pop(apagar)
            except:
                 print('INDICE ERRADO, TENTE NOVAMENTE COM UM INDICE VÁLIDO: ')    