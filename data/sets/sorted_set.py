def observed():
    observations=[]
    print("Counting Observations....")
    for _ in range(5):
        print("Enter  an observation")
        observations.append(input())
    return(observations)

def remove_observations(observations):
    choice = "y"
    while choice == "y":
        print("Do you wish to remove an observation (y/n)?")
        choice = input()

        if (choice == "y"):
            print("Please enter the observation you wish to remove")
            observation = input()
            observations.remove(observation)
            print("Done!!!")
        else:
            choice = "n"

def run():
    observation_set = set()
    observations = observed()

    remove_observations(observations)

    for observation in observations:
        data = (observation, observations.count(observation))
        observation_set.add(data)

    for data in sorted(observation_set):
        print(f"{data[0]} observed {data[1]} times.")

    print(observation_set)
if __name__=="__main__":
    run()