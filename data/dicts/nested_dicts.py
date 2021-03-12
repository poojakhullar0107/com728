def short_pattern():
    pattern={"sequence":"101","occurrences":5 }
    return(pattern)
def medium_pattern():
    pattern={"sequence":"111000","occurrences": 25 }
    return(pattern)
def long_pattern():
    pattern={"sequence":"1100110011001100","occurrences":50 }
    return (pattern)
def run():
    pattern={"short sequence":short_pattern(),
             "Medium sequence": medium_pattern(),
             "long sequence": long_pattern()}
    for key, value in pattern.items():
        print(f"{key} : {value}")
if __name__ == "__main__":
    run()