nome=input("Nome: ")
valor_hora= float(input("Valor por hora: "))
horas_trabalhadas= int(input("Horas trabalhadas: "))

print(f'O pagamento para {nome} deve ser de R${horas_trabalhadas * valor_hora}')