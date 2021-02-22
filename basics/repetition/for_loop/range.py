def run():
    print ("What level of brightness is required?")
    b_level=int(input())
    print("Adjusting Brightness")
    for i in range (2,b_level+1,2):
        print(f"Beeps brightness level   : {'*'* i}")
        print(f"Bops brightness level is : {'*' * i}")
    print("Adjustments Completed..")
if __name__ ==  "__main__":
    run()
