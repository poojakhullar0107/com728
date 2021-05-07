import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(frame):
    print(f"Frame Number is : {frame}")


# your code here

def run():
    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig,animate,frames=10,interval=1000)
    plt.show()
run()