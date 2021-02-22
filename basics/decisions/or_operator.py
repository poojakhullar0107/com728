def run():
    print("what type of adventure should i have?")
    type=input()
    if type=="scary" or type=="short":
        print("Entering the dark forest!")
    elif type=="safe" or type=="long":
        print("taking the  safe route!")
    else:
        print(" not sure which route to take")

