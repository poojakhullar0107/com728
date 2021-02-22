
def escape_by(plan):
    if plan=="jumping over":
        print ("We cannot escape that way! the boulder is too big.")
    elif plan=="running around":
        print("We cannot escape that way!the boulder is moving too fast.")
    elif plan == "going deeper":
        print("That might just work! let's go deeper.")
    else:
        print("Not sure about that plan...")
def run():
    escape_by("jumping over")
    escape_by("running around")
    escape_by("going deeper")
if __name__ ==  "__main__":
    run()