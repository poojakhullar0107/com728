print ("What phrase do you see?")
string=input()
lenght_of_string=len(string)
print ("reverse is: ", end="")
for i in range (lenght_of_string-1,-1,-1):
    print (f"{string[i]}", end='')