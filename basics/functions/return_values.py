def sum_weight(bop_weight, beep_weight):
    sum=bop_weight+beep_weight
    return sum
def calc_avg_weight(bob_weight, beep_weight):
    avg=sum_weight(bob_weight, beep_weight)/2
    return(avg)
def run():
    print("enter bop's weight pl ")
    bop_weight=float(input())
    print("enter beep's weight pl ")
    beep_weight = float(input())
    print("enter your choice ( Sum / average)")
    choice=input()
    if choice=="sum":
        sum=sum_weight(bop_weight, beep_weight)
        print (f"sum  is {sum:.2f}")
    elif choice=="average":
        avg=calc_avg_weight(bop_weight, beep_weight)
        print(f"average weight  is       {avg:.2f}")
    else:
        print ("Please enter right choice")

if __name__ ==  "__main__":
    run()