print("Digite as idades")

conv_idade= 0
soma_idades = 0
qtd_idade= 0 

while True:
   
    idade= input( )
    conv_idade= float(idade)

    if conv_idade < 0: 
        break

    qtd_idade += 1
    soma_idades+= conv_idade


print (f"A soma das idades é: {soma_idades/qtd_idade}")    