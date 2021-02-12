
print("enter your first whole number")
num1=int(input())
print("enter your second whole number")
num2=int(input())
print("enter your third whole number")
num3=int(input())
count_even=0
count_odd=0
if num1%2==0 :
    count_even=count_even+1
else:
    count_odd=count_odd+1
if num2%2==0:
    count_even = count_even + 1
else:
    count_odd=count_odd+1
if  num3%2==0:
    count_even = count_even + 1
else:
    count_odd=count_odd+1

print(f"{count_even} numbers are even and  {count_odd} numbers are odd")