def run():
    print("what is your name")
    name = input()
    print("how old are you?( in years)")
    age = int(input())
    print("how tall are you (in metres)")
    tall = float(input())
    print("what is your weight in kilogram")
    weight = float(input())
    bmi = float(weight / (tall ** 2))
    print(f"{name} your age is {age} and your BMI is {round(bmi, 2)}")


