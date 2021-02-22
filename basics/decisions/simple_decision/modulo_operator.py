def run():
    print("please enter whole number")
    num=int(input())
    c=num%2

    if (c == 0):
        print(f"the number{num} is even number")
    else:
        print(f"the number {num} is an odd number")
if __name__ ==  "__main__":
    run()
