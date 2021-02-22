def run():
    print("how many bars should be charged")
    num=int(input())
    count=1

    while (count<=num):
        print(f"Charging :{ '█ ' * count} ")
        count+=1
if __name__ ==  "__main__":
    run()

