import random
import matplotlib.pyplot as plt
def data():
    paths={}
    print("What type of line your want (:,--,-)")
    line=input()
    print("What Colour your want (r,g,b)")
    colour = input()
    print("What type of marker your want (o,s,^)")
    marker = input()
    paths['line_style'] = line
    paths['colour'] = colour
    paths['marker_style'] = marker
    return paths
def generate():
    print("how many lines would you like to display")
    numbers=int(input())
    for i in range(numbers):
        values=data()
        x = random.sample(range(1, 10), 5)
        y = random.sample(range(1, 10), 5)
        format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
        plt.plot(x, y, format)
    plt.show()
def run():
    print("Running")
    generate()
    print("Done")
if __name__=="__main__":
    run()