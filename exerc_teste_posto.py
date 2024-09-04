numeros_validos = 1234
codigo= 0
alcool = 0
gasolina= 0
diesel= 0
while codigo != 4 :
    codigo= int(input("Informe um código: 1,2,3 ou 4 para encerrar: "))
   
    if (codigo > 1 ) and (codigo >4):
        print("Digite um código válido!")
    else:
        if codigo == 1:
            alcool += 1
        if codigo == 2: 
            gasolina += +1
        if codigo == 3:
            diesel += 1
        if codigo== 4:
                print("MUITO OBRIGADO!") 
    

print(f'{alcool=}')
print(f'{gasolina=}')
print(f'{diesel=}')
