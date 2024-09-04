entrada=input('Digite um número inteiro: ')


if entrada.isdigit():
     entrada_int= int(entrada)
     parOUimpar= entrada_int %2 ==0 
     par_impar= 'impar'

     if parOUimpar:
        par_impar= "par"

     print(f'O Número {entrada} é {par_impar}')
else:
     print(f'{entrada} não é um número inteiro')

