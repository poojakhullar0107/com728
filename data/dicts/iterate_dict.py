def display_keys(data):
    for key in data.keys():
        print(key)



def display_values(data):
    for value in data.values():
        print(value)

def display_items(data):
    for key, value in data.items():
        print(f"{key},{value}")

def run():
    data = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence":1}
    print("Dictionary:")
    print(data)
    print("Keys:")
    display_keys(data)
    print("Values:")
    display_values(data)
    print("Pairs")
    display_items(data)
if __name__ == "__main__":
    run()