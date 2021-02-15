

print("where should i look?")
look_type=input()
if look_type=="in the bedroom":
    print("where in the bedroom should i look?")
    bedroom_look_type=input()
    if bedroom_look_type=="under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")
elif look_type=="in the bathroom":
    print("where in the bathroom should i look?")
    bathroom_look_type = input()
    if bathroom_look_type=="in the bath tub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")

elif look_type=="in the lab":
    print("where in thelab should i look?")
    lab_look_type = input()
    if lab_look_type=="on the table":
        print("Yes! I found my battery.")
    else:
        print("Found some tools but no battery")

else:
    print ("I do not know where that is?? but I will keep looking.")
