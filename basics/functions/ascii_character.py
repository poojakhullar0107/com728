print("Program Started!")
print("Please enter an ASCII code:")

code=abs(int(input()))
if code in range (32,127):
    print(f"The character represented by the ASCII code {code} is: {chr(code)}")
else:
    print("please enter the Ascii code within 32-126")
print("Program Ended!")