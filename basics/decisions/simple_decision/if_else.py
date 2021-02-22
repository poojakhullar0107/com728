def run():
    print("what activity you want to perform")
    act_type=input()
    if act_type=="calculate":
        print("Performing calculations..")
    else:
        print("performing activity...")
    print("activity completed")
if __name__ ==  "__main__":
    run()
