print("Digite dois números: ")

x=int(input(" "))
y=int(input(" "))


ran= range(x,y)
impares= 0 
soma_impares= 0

for z in ran:
    if z % 2 != 0:
        impares= z
        soma_impares = soma_impares + impares

print(f'Soma dos impares= {soma_impares}')

"""
CÓDIGO FRAGIL COM ERRO QUE AINDA NÃO SEI RESOLVER ESTÁ DANDO ERRO DE ACORDO COM A ORDEM
DO X E DO Y
"""