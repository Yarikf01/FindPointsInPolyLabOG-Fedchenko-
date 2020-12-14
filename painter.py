import matplotlib.pyplot as plt


def draw_plot(edges, points, inside_points):
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(*zip(*points), color="k")
    ax.scatter(*zip(*inside_points))
    x_list = [x for [x, y] in edges]
    y_list = [y for [x, y] in edges]
    ax.plot(x_list, y_list, color="r")
    return fig, ax
