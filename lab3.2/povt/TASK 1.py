v1 = int(input("Введите скорость первого = "))
v2 = int(input("Введите скорость втоорого = "))
S = int(input("начальное расстояние между ними  = "))
T = int(input("введите время =  "))
S1 = T*(v1+v2)
T1 = S1 + S
print ("расстояние между ними через",T, "часов = ",T1)
