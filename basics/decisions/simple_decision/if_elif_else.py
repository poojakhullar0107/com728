def run():
    print("towards which direction i should paint(up, down, left or right)")
    direction_type=input()
    if direction_type =="up":
        print(f"i am painting in {direction_type}ward direction")
    elif direction_type =="down":
        print(f"i am painting in {direction_type}ward direction")
    elif direction_type =="left":
        print (f"i am painting in {direction_type} direction")
    elif direction_type =="right":
        print(f"i am painting in {direction_type} direction")
    else:
        print ("i am not painting")
if __name__ ==  "__main__":
    run()
