import random
A = random.randrange(1,100)
B = random.randrange(1,A)
print("A = ", A)
print("B = ", B)
x = A%B
print("Длина незанятой части отрезка A: ", x)