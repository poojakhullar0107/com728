def cross_bridge(distance):
    for i in range (distance):
        print("crossed steps")
    if distance>5:
        print("bridge is collapsing")
    else:
        print("we must keep going")
cross_bridge(3)
cross_bridge(6)