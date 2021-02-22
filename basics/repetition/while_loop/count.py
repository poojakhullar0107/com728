def run():
    print("How many live cables should i avoid")
    no_of_cables=int(input())
    count=1
    while (count<=no_of_cables):
        print(f"Avoiding...Done!{count} Live cables avoided")
        count+=1
if __name__ ==  "__main__":
    run()


