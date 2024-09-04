x = int(input("Digite um número inteiro: "))

while x != 0:
    if x % 2 !=0:
       x += 1
    print((5 * x) + 20)
    x = int(input("Digite um número inteiro: "))
    if x == 0:
        break

