name = input("name: ")
weight = float(input("weight: "))
height = float(input("height: "))

bmi = weight/(height**2)

print(f"Hello {name}, your BMI is: {bmi:.1f}")

if bmi < 18.5:
    print("you are too thin to work")
elif bmi < 24:
    print("you are normal and healthy")
elif bmi <28:
    print("you are a little overweight")
else :
    print("you are too heavy that you will collapse the seat")
