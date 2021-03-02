import csv
def extract(file_path):
    print("Extracting...", end="")
    with open(file_path) as file:
        csv_reader=csv.reader(file)
        next(csv_reader)
        name=""
        for values in csv_reader:
            name+=f"{values[1]}\n"
        print("Done!")
    print(f"The extracted names are:\n{name}")


def run():
    extract("bots.csv")
run()