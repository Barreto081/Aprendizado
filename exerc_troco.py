valor_produto=float(input("Digite o valor do produto: "))
quantidade= int(input("digite a quantidade comprada: "))
pagamento= float(input("Valor pago pelo cliente: "))
valor_apagar= valor_produto*quantidade


print(f"Troco: {pagamento-valor_apagar}")