#to find largest number out of three number
def run():
    print ("Enter first whole number pl")
    num1=int(input())
    print ("Enter second whole number pl")
    num2=int(input())
    print ("Enter third whole number pl")
    num3=int(input())
    if num1==num2 and num1==num3:
        print("All the numbers are same")
    elif num1>num2 and num1>num3:
        print(f"{num1} is largest")
    elif num2>num3 and num2>num1:
        print (f"{num2} is largest")
    else:
        print(f"{num3} is largest")
if __name__ ==  "__main__":
    run()
