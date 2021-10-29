

price = int(input("Цена за 1 кг = "))
print('Цена 1 кг конфет: ', price)
print()
for i in range(0, 10):
    x = 0.1 + 0.1 * i
    print('Стоимость {0:.1f} кг: {1:.2f}'.format(x, x * price))
print()
