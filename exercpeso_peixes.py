peso_total= float(input("Quantos Kgs você trouxe? "))

if peso_total >50:
    excesso= peso_total- 50
    multa= excesso * 4

if peso_total > 50:
    print(f"Você excedeu o limite em {excesso:.2f} quilos ")
    print(f'A multa é de R${multa:.2f}')
    
else:
    print("Peso não excedido!")