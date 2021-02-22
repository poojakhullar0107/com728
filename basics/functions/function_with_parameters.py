
def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining >steps_crossed:
        print("Still some way to go!")
    else:
        print("we are almost there")
def run():
    print("enter steps remaining")
    steps_remaining=int(input())
    print("enter steps crossed")
    steps_crossed = int(input())
    climb_ladder(steps_remaining, steps_crossed)


