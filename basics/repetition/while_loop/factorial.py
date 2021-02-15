print("Please enter a number:")
num=int(input())
num1=num
fact=1
while num>1:
    fact*=num
    num-=1
print(f"factorial of {num1} is {fact} ")