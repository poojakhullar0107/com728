def steps():
    likelihood=[("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4) ]
    return likelihood
def run():
    steps_list=steps()
    good_steps=[]
    bad_steps=[]

    for step in steps_list:
        if (step[1])>=50:
            good_steps.append(step)
        else:
            bad_steps.append(step)

    print(f"Good Steps are : {len(good_steps)} and bad steps are {len(bad_steps)}")



if __name__=="__main__":
    run()