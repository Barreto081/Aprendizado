entrada= input("Que horas são?")

entrada_int= int(entrada)

if (entrada_int >= 0) and (entrada_int< 11):
    saudacao= "Bom Dia"
elif (entrada_int >11 ) and (entrada_int <=17 ):
    saudacao= "Boa Tarde"
elif (entrada_int >=18) and (entrada_int <= 24):
    saudacao= "Boa Noite"
else:
    saudacao=(f"{entrada} não é um horário compativel")    

print(saudacao)