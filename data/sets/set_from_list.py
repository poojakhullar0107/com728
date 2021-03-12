def observed():
    observations=[]
    for _ in range(7):
        print("Enter  an observation")
        observations.append(input())
    return(observations)

def run():

    observation_set=set()

    print("Counting observations...")
    observations=observed()

    for observation in observations:
        data = (observation, observations.count(observation))
        observation_set.add(data)


    for data in observation_set:
        print(f"{data[0]} observed {data[1]} times.")
run()