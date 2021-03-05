def likelihood():
    likelihood=(50, 38, 27, 99, 4)
    return (min(likelihood), max(likelihood))

def run():
    value=()
    value=likelihood()
    print(f"Minimum likelihood of falling is : {value[0]} %")
    print(f"Maximum likelihood of falling is : {value[1]} %")

if __name__=="__main__":
    run()