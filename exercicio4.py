x= int(input('Quantos números você deseja digitar? '))

rg= range(1,x+1)

for i in rg:
    y= int(input("Digite um número: "))
    if y % 2 == 0:
        if y > 0:
            print("PAR POSITIVO")
        elif y < 0: 
            print("PAR NEGATIVO")
    elif y % 2 !=0:
        if y > 0:
            print("IMPAR POSTIVO")
        elif y < 0:
            print("IMPAR NEGATIVO")
    if y == 0:
        print("NULO")