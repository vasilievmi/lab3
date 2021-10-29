N = int(input("Введите N = "))
A1 = 2
for i in range(1,N):
    A2 = 2 + 1/A1
    A1 = A2
print ("A = ",A2)