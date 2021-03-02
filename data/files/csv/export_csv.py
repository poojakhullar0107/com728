import csv
def export(file_path, no_of_bots):
    with open(file_path,"a") as file:
        for values in range(no_of_bots):
            print("please enter bot id")
            bot_id=int(input())
            print("please enter bot name")
            bot_name=input()
            print("please enter bot paint")
            bot_paint=input()
            file.write(f"{bot_id},{bot_name},{bot_paint}\n")
        print("Done!!")

def run():
    export("exported_bots.csv", 2)

if __name__ == "__main__":
    run()

