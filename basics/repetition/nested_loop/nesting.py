print("please enter a sequence")
sequence=input()
print("please input character for the marker")
character=input()
count=0
sum=0
for i in range (len(sequence)):
    if (count==0) and (sequence[i]==character):
        print("found first character")
        count=1
    elif count==1 and sequence[i]==character :
        print ("found last character")
    elif count==1:
        sum+=1
print(f"Distance between the marker is {sum}")