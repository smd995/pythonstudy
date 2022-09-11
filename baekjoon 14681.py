x = input()
y = input()
x = int(x)
y = int(y)
if x > 0 and y > 0:
    print(1)
else:
    if x < 0 and y > 0:
        print(2)
    else:
        if x > 0 and y < 0:
            print(4)
        else:
            print(3)



