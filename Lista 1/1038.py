prices = [float(4), float(4.50), float(5), float(2), float(1.50)]

x, y = map(int, input().split())

total = y*prices[x-1]

print("Total: R$ %.2f" %total)