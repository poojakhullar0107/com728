import matplotlib.pyplot as plt


def read_data(file_name):
    list = []
    with open("temps.txt") as f:
        for line in f:
            list.append(line.strip())
    print(list)
    return list


def run():
    file_name = "temps.txt"
    list = read_data(file_name)
    print(list)
    print(range(len(list)))
    fig, (ax1, ax2) = plt.subplots(1, 2)
    #plt[0,0].plot(li)
    plt.show()
