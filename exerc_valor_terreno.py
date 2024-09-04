print("Seja Bem-Vindo!")

largura= float(input("Qual a largura do seu terreno?"))

comprimento= float(input("Qual o comprimento do seu terreno?"))

valor_m2= float(input("Qual o valor do metro quadrado na sua região?"))

area_terreno= largura * comprimento

print(f'Área do terreno {area_terreno}'
      )
print(f'O valor do seu terreno está avaliado em R${area_terreno * valor_m2}')

