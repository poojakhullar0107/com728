def gang():
    print("Loading gang....")
    friends = ["Scooby Doo", "Shaggy Rogers", "Fred Jones", "Daphne Blake", "Velma Dinkley"]
    print(friends)
    print("....Done")
    return (friends)


def phrases(friends):
    quotes ={}
    for index in range(len(friends)):
        print(f"What does {friends[index]} say?")
        quote = input()
        quotes.update({friends[index]: quote})
    return (quotes)


def save(quotes):

    f = open("quotes.txt", "w")
    for key, value in quotes.items():
        f.write(f"'{key}': '{value}',\n")

    f.close()
    with open("quotes.txt") as file:
        lines=file.readlines()
        for line in lines:
            print(line)


friends = gang()
quotes = phrases(friends)
print("Phrases:")
print(quotes)
save(quotes)
