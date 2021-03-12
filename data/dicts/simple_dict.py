def pattern():
    sequences={"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return(sequences)

def run():
    sequences=pattern()
    print(f"My Dictionary has : {sequences}")

if __name__ =="__main__":
    run()
