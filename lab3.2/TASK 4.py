for i in range(-2, 7):
    x = i / 2
    if x <= 0:
        y = -x
    elif x < 2:
        y = x * x
    else:
        y = 4
    print("x = {0} : f(x) = {1}".format(x, y))

