print("please enter a sequence")
sequence=input()
print("please input character for the marker")
character=input()
p1=-1
p2=-1
for p in range(len(sequence)):
    if sequence[p]==character:
        if p1==-1:
            p1=p
        else:
            p2=p
print(f"Difference between marker is {p2-p1-1}")