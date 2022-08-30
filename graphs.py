from matplotlib import pyplot

def create_chart(x, y, filename):
    figure = pyplot.figure()
    pyplot.scatter(x, y, alpha=0.5)
    pyplot.savefig(f"{filename}.png")
