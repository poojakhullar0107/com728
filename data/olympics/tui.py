line_size=160


def started(msg=""):
    print(f"{'-' * line_size}")
    print(f"Operation started: {msg}...\n")


def completed():

    print("Operation Completed.")
    print(f"{'-' * line_size}")


def error(msg):
    print(f"Error!! {msg}\n")


def menu():
    print(f"""Please select one of the following options:
    {"[years]":<10} List unique years
    {"[tally]":<10} Tally up medals
    {"[team]":<10} Tally up medals for each team
    {"[exit]":<10} Exit the program
    """)
    response = input()
    print(f"Your Selection is : {response:>10}")
    return response.lower().strip()


def display_medal_tally(tally):
    print(f"|{'Gold':<10}|{tally['Gold']:<10}|")
    print(f"|{'Silver':<10}|{tally['Silver']:<10}|")
    print(f"|{'Bronze':<10}|{tally['Bronze']:<10}|")


def display_team_medal_tally(team_tally):
    for key, value in team_tally.items():
        print(key)
        print(f"Gold:\t{value['Gold']}, Silver:{value['Silver']}, Bronze:{value['Bronze']}")


def display_years(year):
    year_sorted = sorted (year, reverse=True)
    for years in year_sorted:
        print(years)

