print("Welcome to Angela Cheng's BMI Calculator")
system = input("Do you use the customary system or the metric system?")
if system == "metric":
    height = input("What is your height in meters?")
    weight = input("What is your weight in kilograms?")
    height1 = float(height)
    weight1 = float(weight)
    x = weight1 /height1 ** 2
    print("This is your BMI")
    print(x)


if system == "customary":
    height2 = input("What is your height in feet?")
    weight2 = input("What is your weight in pounds")
    height3 = float(height2)
    weight3 = float(weight2)
    x = weight3 / height3 ** 2 * 703
    print("This is your BMI")
    print(x)


if x < 17:
    print("You are underweight")
if x > 17 and x < 25:
    print("You are healthy")
if x > 25 and x < 30:
    print("You are overweight")
if x > 30 and x < 40:
    print("You are obese")
if x > 40:
    print("You are extremely obese")

print("Thank you for using this calculator")
