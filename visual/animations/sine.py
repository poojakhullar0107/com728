import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    global ax
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    PI = 3.14
    x_values = np.arange(0, frame)
    y_values_in_radians = x_values * (PI / 180)
    y_values = np.sin(y_values_in_radians)
    ax.plot(x_values, y_values)



# your code here
def run():
    global fig
    ani = animation.FuncAnimation(fig, animate, frames=720, interval=100)
    plt.show()


if __name__ == "__main__":
    run()
