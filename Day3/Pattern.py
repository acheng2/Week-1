x = input("What pattern do you want to print? 1, 2, or 3")

if x == 3:
    a = int(input("Number of lines"))
    b = int(input("Width of triangle"))
    e = 1
    f = a % e
    while a > 0:
        a = a - 1
        while e <= b:
            print("*" * e)
            e = e + 1
        while e > 0:
            print("*" * e)
            e = e - 1

if x = 2:
    a = input("Number of lines")
    b = a
    while a > 0:
        print ("*" * b)
        a = a - 1
        b = b - 1

if x == 1:
    a = input("Number of lines")
    b = 1
    while a > 0:
        print ("*" * b)
        a = a - 1
        b = b + 1
