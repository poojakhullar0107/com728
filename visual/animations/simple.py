import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    global ax
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.plot(frame, frame, 'r-o')


# your code here

def run():
    global fig
    ani = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
    plt.show()


if __name__ == "__main__":
    run()
