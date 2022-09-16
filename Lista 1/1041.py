x, y = map(float, input().split())

if x == 0 and y == 0:
    coordinate = "Origem"
elif x == 0 or y == 0:
    coordinate = "Eixo X" if y == float(0) else "Eixo Y"
elif x < float(0):
    coordinate = "Q2" if y > float(0) else "Q3"
elif x > float(0):
    coordinate = "Q1" if y > float(0) else "Q4"

print(coordinate)