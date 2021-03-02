import os
def display_chars(path,no_of_letters):
    with open(path) as file:
        letters=file.read(no_of_letters)
        print(letters)


def display_line(path):
    with open(path) as file:
        line=file.readline().strip()
        print(line)

def display_text(path):
    with open(path) as file:
       data=file.read()
       print(data)

def run():

    print("how many letters you want to read")
    no_of_letters=int(input())
    display_chars("library.txt",no_of_letters)
    display_line("library.txt")
    display_text("library.txt")

if __name__ ==  "__main__":
    run()
