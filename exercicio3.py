entrada = input ('Você deseja Entrar ou Sair?')
senha_digitada = input ("Digite sua senha: ")
senha_permitida = '123456'

if (entrada == 'entrar' or entrada =='ENTRAR') and (senha_digitada ==senha_permitida ): 
     print ('Você entrou no sistema!!!')
elif (entrada == 'sair' or entrada =='SAIR') and (senha_digitada == senha_permitida):
    print ('Você saiu do sistema!!!')
else:
    print (" algo deu errado!!!")           