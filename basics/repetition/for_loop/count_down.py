print("How far are we from the cave?")
distance=int(input())
d=distance
for i in range  (0,distance,1):
    print(f"{d} steps remaining")
    d=d-1
print("we have reached the cave")
