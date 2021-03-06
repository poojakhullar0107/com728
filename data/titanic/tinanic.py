headers=[]
import csv

#task1

def load_data():
    records=0
    with open("titanic.csv") as file:
        csv_reader = csv.reader(file)
        headers=next(csv_reader)
        print("loading Data....")
        for values in csv_reader:
            records+=1
    print (f"Total number of passsengers are : {records}")

#task2

def display_menu():
    print("Please select one of the following options:")
    print("[1] Display the names of all passengers")
    print("[2] Display the number of passengers that survived")
    print("[3] Display the number of passengers per gender")
    print("[4] Display the number of passengers per age group")
    print("[5] Display the number of survivors per age group")
    selected_option=int(input())
    print(f"you have selected option {selected_option}")
    return selected_option

#task 3

def display_passengers_name():
    print("Name of the passengers are:")
    with open("titanic.csv") as file:
        csv_reader = csv.DictReader(file)
        for values in csv_reader:
            print(values['Name'])

#task 4

def display_num_survivors():
    print("Number of passengers who survived are:")
    Num_survived=0
    with open("titanic.csv") as file:
        csv_reader = csv.DictReader(file)
        for values in csv_reader:
            if values['Survived'] == '1':
                Num_survived+=1
    print(Num_survived)

#task 5
def diplay_passenger_per_gender():
    with open("titanic.csv") as file:
        csv_reader = csv.DictReader(file)
        males=females=0
        for values in csv_reader:
            if values['Sex'].lower() == 'male':
               males+=1
            else:
               females+=1
    print(f"Number of male passenger are : {males}")
    print(f"Number of female passenger are : {females}")

#task 6
def display_passengers_per_age_group():
    with open("titanic.csv",) as file:
        csv_reader = csv.DictReader(file)
        children = adults = elderly = 0
        for values in csv_reader:
            if values['Age']< '18':
                children += 1
            elif values['Age'] >= '18' and values['Age']< '65':
                adults += 1
            else:
                elderly += 1
        print(f"Number of Young passengers are : {children}")
        print(f"Number of Adult passenger are : {adults}")
        print(f"Number of Elderly passengers are : {elderly}")

#task 7
def display_survivors_per_age_group():
    with open("titanic.csv",) as file:
        csv_reader = csv.DictReader(file)
        children = adults = elderly = 0
        children_survived=adults_survived= elderly_survived=0
        for values in csv_reader:
            if values['Age']< '18':
                children += 1
                if values['Survived']=='1':
                    children_survived+=1
            elif values['Age'] >= '18' and values['Age']< '65':
                adults+=1
                if values['Survived']=='1':
                    adults_survived+=1
            elif values['Age']>='65':
                elderly += 1
                if values['Survived']=='1':
                    elderly_survived+=1
        print(f"Number of Young passengers survived are :{children_survived}/{children}")
        print(f"Number of Adult passenger survived are : {adults_survived}/{adults}")
        print(f"Number of Elderly passengers survived are :{elderly_survived}/{elderly}")

def run():
    load_data()
    selected_option=display_menu()
    if selected_option==1:
        display_passengers_name()
    elif  selected_option==2:
        display_num_survivors()
    elif selected_option==3:
        diplay_passenger_per_gender()
    elif selected_option==4:
        display_passengers_per_age_group()
    elif selected_option==5:
        display_survivors_per_age_group()
    else: print("You have entered a wrong choice....bye!!")
if __name__=="__main__":
    run()

