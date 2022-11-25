def bmi(weight,height):
    a=weight/height
    if a<=18.5:
        print("underweight")
    elif a<=25.0:
        print("normal")
    elif a<=30.0:
        print("overweight")
    else:
        print("obese")
    print(a)
bmi(eval(input("enter the weight")),eval(input("enter the height")))
