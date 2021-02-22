def identify():
    print("what lies before us")
    response=input()
    if response=="a large boulder":
        print("it is time to run")
    else:
        print("we are fine here")
def run():
    identify()
if __name__ ==  "__main__":
    run()