def run():
    print("enter your first number")
    num1=float(input())
    print("enter your second number")
    num2=float(input())
    if num1>num2:
        print ("first number is bigger")
    elif num2>num1:
        print("second number is bigger")
    else:
        print("both the enumbers are same")
if __name__ ==  "__main__":
    run()
