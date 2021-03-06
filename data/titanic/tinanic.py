
headings=[]
import csv


#task1
def load_data(filepath):
    records=0
    print("loading Data....")
    with open(filepath) as file:
        csv_reader=csv.reader(file)
        headings=next(csv_reader)
        for values in csv_reader:
            records+=1
    print (records)

#task2

def display_menu():
    print("Please select one of the following options:")
    print("[1] Display the names of all passengers")
    print("[2] Display the number of passengers that survived")
    print("[3] Display the number of passengers per gender")
    print("[4] Display the number of passengers per age group")
    selected_option=int(input())
    print(f"you have selected option {selected_option}")
    return selected_option

#task 3

def display_passengers_name():
    print("Name of the passengers are:")
    with open("titanic.csv") as file:
        csv_reader = csv.DictReader(file)
        for values in csv_reader:
            print(values['Name'],values['Age'])

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

def run():
    load_data("titanic.csv")
    selected_option=display_menu()
    if selected_option==1:
        display_passengers_name()
    elif  selected_option==2:
        display_num_survivors()
    elif selected_option==3:
        diplay_passenger_per_gender()
    elif selected_option==4:
        display_passengers_per_age_group()
    else: print("You have entered a wrong choice....bye!!")
if __name__=="__main__":
    run()

