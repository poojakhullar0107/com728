def cross_bridge(distance):
    for i in range (distance):
        print("crossed steps")
    if distance>5:
        print("bridge is collapsing")
    else:
        print("we must keep going")

def run():
    print("please enter the distance in steps")
    distance=int(input())
    cross_bridge(distance)

if __name__ ==  "__main__":
    run()