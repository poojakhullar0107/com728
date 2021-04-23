import matplotlib.pyplot as plt


def coordinate():
    print("Please give value of x")
    x = int(input())
    print("Please give value of y")
    y = int(input())
    return (x,y)

def path():
    print("Retrieving Path...")
    x_values=[]
    y_values=[]
    for i in range (4):
        data=coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]


def run():
    values=path()

    plt.plot(values[0],values[1],"ro--")
    plt.show()

if __name__ =="__main__":
    run()