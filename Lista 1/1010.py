valor = float()
contador = 0

while contador <= 1:
    code, itens, value = input().split()
    valor += (int(itens)*float(value))
    contador +=1

print("VALOR A PAGAR: R$ %.2f" % valor)