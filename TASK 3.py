import random
A = random.randrange(-10,10)
B = random.randrange(-10,10)
print("A = ", A)
print("B = ", B)
x = (A>=0) or (B<-2)
print("A >= 0: ", (A>=0))
print("B < -2: ", (B<-2))
print("A>=0 или B<-2: ", x)