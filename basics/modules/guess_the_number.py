import random
print("please input minimum number")
min_number=int(input())
print("please input maximum number")
max_number=int(input())
number=random.randint(min_number,max_number)
ch='y'
print(f"I am choosing one number from {min_number} to {max_number}")
while(ch=='y'):
    print("Please guess the number I choose")
    user_number=int(input())
    if user_number<number:
        print("its wrong... your guess is low.. think higher number")
        print ("want to try again??")
        choice=input()
        if choice!="y":
            print("its sad to say you bye!!! see u later")
            break
    elif user_number>number:
        print("its wrong... your guess is higher.. think lower number")
        print("want to try again??")
        choice = input()
        if choice != "y":
            print("its sad to say you bye!!! see u later")
            break
    else :
        print("Congratulations!!!! you guessed the right number")
        ch='n'
