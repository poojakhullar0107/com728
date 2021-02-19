print("Program Started!")
print("Please enter a letter:")
character=input()
if len(character)==1:
    print (f"The ASCII code for {character} is: {ord(character)}")
else:
    print("please enter single character only")
print("Program Ended!")
