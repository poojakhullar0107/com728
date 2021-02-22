def run():
    print("pl enter the number of lives")
    lives=int(input())
    print("Please enter the energy level")
    energy=int(input())
    print("please enter the shield level")
    shield=int(input())
    print("Health has been set...")
    print(f" Lives - {'♥' * lives}")
    print(f" Energy- {'♦' * energy}")
    print(f"Shield - {'♦' *  shield}")

if __name__ ==  "__main__":
    run()
