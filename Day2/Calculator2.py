print("Welcome to Angela Cheng's calculator")
zzz = input("What do you want to do? Actions: binary to octal, binary to decimal, divide, remainder, multiply, add, subtract")

if zzz = "binary to octal":
    a = input("Please enter the binary you want to convert to octal")
    b = str(a)
    count = 0
    t = 0
    y = 0
    while 3*count < len(b):
        z = a % 1000
        r = z % 8
        y = r * 10 ** t + y
        t = t + 1
        count = count + 1
        a = a / 1000
    print(y)

if zzz = "binary to decimal":
    a = input("Please enter the binary you want to convert to decimal") # binary to decimal
    count = 0
    y = 0
    b = str(a)
    while count <= len(b):
        r = a % 2
        y = r * 2 ** count + y
        a = a / 10
        count = count + 1
    print(y)

if zzz = "divide":
    a = input("First number") # division
    b = input("Second number")
    count = 0
    while a >= b:
        a = a - b
        count = count + 1
    print("Your answer is")
    print(count)
    print("Your remainder is")
    print(a)

if zzz = "remainder":
    a = input("First number") # remainder
    b = input("second number")
    count = 0
    while a >= b:
        a = a - b
        count = count + 1
    print(a)

if zzz = "multiply":
    a = input("First number") # multiplication
    b = input("Second number")
    x = 0
    count = 0
    while count < b:
        x = x + a
        count = count + 1
    print(x)

if zzz = "add":
    a = input("First number") # addition
    b = input("Second number")
    x = a + b
    print(x)

if zzz = "subtract":
    a = input("First number") # subtraction
    b = input("Second number")
    x = a - b
    print(y)
