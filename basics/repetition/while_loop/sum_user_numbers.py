
print ("How many numbers should I sum up?")
count=int(input())
t=count
sum=0
loop=1
while count>0:
    print(f"enter your {loop} number of {t}")
    num=int(input())
    sum+=num
    loop+=1
    count-=1
print (f"The Answer is {sum}")