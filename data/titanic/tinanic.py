
headings=[]
import csv
import pandas as pd
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
    print(" [1] Display the names of all passengers")
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
            print(values['Name'])

def run():
    load_data("titanic.csv")
    selected_option=display_menu()
    if selected_option==1:
        display_passengers_name()



if __name__=="__main__":
    run()

