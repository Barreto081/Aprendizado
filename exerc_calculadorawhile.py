import os

while True:

    numero1= input("Digite o primeiro número: ")
    numero2= input("Digite o segundo número: ")
    operador= input("Digite o operador (+ - / *)")

    numero_validos = None
    numero1_float= 0
    numero2_float= 0
    
    try:
        numero1_float= float(numero1)
        numero2_float= float(numero2)
        numero_validos= True
    except:
         numero_validos= None
        
         if numero_validos is None:
            print("Um ou ambos dos números digitados são inválidos! ")
            continue
         
    operador_valido = "+-/*"

    if len(operador) >1:
        print("Digite apenas um operador!")   
        continue
    
    if operador not in operador_valido:
        print("Operador inválido.")
        continue

    print('Realizando sua conta, confira o resultado abaixo: ')
    if operador== "+":
        print(numero1_float + numero2_float)
    elif operador == "-":
        print(numero1_float - numero2_float)
    elif operador == "/":
        print (numero1_float / numero2_float)
    elif operador == "*":
        print(numero1_float * numero2_float)
    else:
        print ("não deveria chegar aqui")
        

    sair= input("deseja sair? Digite [s] para sim: ").lower().startswith('s')

    if sair:
        break
os.system('cls')