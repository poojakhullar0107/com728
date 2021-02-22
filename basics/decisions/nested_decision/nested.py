def run():
    print("what type of book cover do you have?")
    type= input()
    if type=="soft":
        print("Is the book perfect - bound?")
        choice= input()
        if choice=="yes":
            print("Soft cover, perfect bound books are very popular!")
        else:
            print (" Soft cover books with no perfect bound  are less popular!" )
    else:
        print("Books with hard covers can be more expensive!")
if __name__ ==  "__main__":
    run()
