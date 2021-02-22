def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print(f"|       |")
    print(f"| {word} |")
    print(f"|       |")
    print("-" * num_dashes)

def display_lower_case(word):
    print(word.lower())
def display_upper_case(word):
    print(word.upper())
def display_mirrored(word):
    p=len(word)
    for letter in range(p-1,-1, -1):
        print(f"{word[letter]}", end='')
def display_repeated(word):
     print("How many times should the word be Repeated?")
     repetitions= int(input())
     for repetition in range(repetitions):
         if (repetition % 2 == 0):
            display_lower_case(word)
         else:
            display_upper_case(word)
def run():
    print("Please enter a word:")
    word = input()
    ch='y'
    while (ch=='y'):

        print("What would you like to do with this word")
        print("1. Display in a box")
        print("2. Display lower-case")
        print("3. Display upper-case")
        print("4. Display mirrored")
        print("5. repeated")
        print("6 Quit")
        print("Please enter your choice")
        response = int(input())
        if response == 1:
            display_box(word)
        elif response == 2:
            display_lower_case(word)
        elif response == 3:
            display_upper_case(word)
        elif response == 4:
            display_mirrored(word)
        elif response == 5:
            display_repeated(word)
        elif response == 6:
            exit
        else:
            print("Unknown option.")

        print("\n   you want to do it again press y or n")
        ch = input()
        if ch!='y':
            print("bye.. have a wonderful day")
if __name__ ==  "__main__":
    run()