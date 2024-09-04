velocidade= 61
local_carro= 100



RADAR1= 60
LOCAL1 = 100
RADAR_DANGER = 1

if velocidade > RADAR1:
    print('Sim, a velocidade foi ultrapassada')
else:
    print ('Não, a velocidade não ultrapassou ou limite')

if local_carro == (LOCAL1 + RADAR_DANGER) or local_carro == (LOCAL1 - RADAR_DANGER) or\
    local_carro== LOCAL1:
    if velocidade > RADAR1:
        print ('O carro foi multado.')
else:
    print('O carro não foi multado.')           
