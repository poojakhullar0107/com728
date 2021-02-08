print ("press 1 for addition\n")
print ("press 2 for subtration\n")
print ("press 3 for multiplication\n")
print ("press 4 for division\n")

print ("Enter first number\n")
num1=input()
print ("Enter second number\n")
num2=input()

print ("press 1/2/3/4 for suitable arithmetic calculator")
choice =input ()


if choice==1:
    answer=num1+num2

if choice==2:
    answer =num1-num2
if choice == 3:
    answer= num1*num2
if choice== 4:
    answer=num1/num2
print (f"your answer is {answer}")
