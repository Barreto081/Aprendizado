x=input("Digite um número: ")
y= input ("Digite outro número: ")

x_float= float(x)
y_float= float(y)

if x_float > y_float:
    print("Decrescente!")
elif y_float > x_float:
    print("Crescente")
elif x_float == y_float:
    print ("São iguais!")