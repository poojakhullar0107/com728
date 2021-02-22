
def run():
    print ("What did I hear?")
    hear=input()
    print("what did I see")
    see=input()
    if hear.lower().strip()=="grrr" and see.lower().strip()=="two red eyes" :
        print("There is a scary creature , I should get out of there!!")
    else:
        print("I am little scared ! but i will continue")

if __name__ ==  "__main__":
    run()
