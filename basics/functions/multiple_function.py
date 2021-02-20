#to define a function to print ladder
def display_ladder(steps):
    for count in range(steps):
        print("| |")
        print("***")
    print("| |")
#define a function to take input for step and call display ladder function
def create_ladder():
    print("how many steps you want in ladder")
    step=int(input())
    display_ladder(step)

# to call function
create_ladder()
