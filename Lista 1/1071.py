inicio = int(input())
fim = int(input())

total = 0

if (inicio>fim):
    for i in range(fim+1, inicio):
        if i%2 != 0:
            total+=1
else:
    for i in range(inicio+1, fim):
        if i%2 != 0:
            total+=1
print(total)