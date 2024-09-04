import os
os.system('cls')

palavra_secreta= "capivara"

letra_acertada= ""

tentativas= 0

while True:
    letra= input("Digite uma letra: ").lower()
    tentativas+=1

    if len(letra) > 1:
        print("Digite apenas uma letra")
        continue


    if letra in palavra_secreta:
       letra_acertada += letra
    
    
    palavra_formada= ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada+=letra_secreta
        else: 
            palavra_formada+= '*'
    print(f"Palavra formada: {palavra_formada}")

    if palavra_formada == palavra_secreta:

        os.system('cls')
        if tentativas > 12:
            print("VOCÊ PERDEU, FEZ MAIS DE 8 TENTATIVAS")
        elif tentativas <= 12: 
            print("VOCÊ GANHOU, PARABÉNS")
        print(f'Você tentou {tentativas} vezes.')
        print(f'A palavra secreta é: {palavra_secreta}')
        break
