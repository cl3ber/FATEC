number = float(input())

if number < round(float(0),2) or number > round(float(100),2):
    print("Fora de intervalo")

inc = float(25)
validar = True
while validar and inc <= 100:
    base = (inc-25)
    if (number <= inc and number > base) or number == 0:
        start = "(" if number > base and base > 0 and number <= inc else "["
        print("Intervalo %s%i,%i]" %(start, (inc-25), inc))
        break
    inc += 25