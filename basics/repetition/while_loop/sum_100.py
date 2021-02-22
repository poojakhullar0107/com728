def run():
    print("Calculating the sum of first 100 numbers")
    count=1
    sum=0
    while count<101:
        sum+=count
        count+=1
    print(f"Done !!, The Answer is {sum}")

if __name__ ==  "__main__":
    run()
