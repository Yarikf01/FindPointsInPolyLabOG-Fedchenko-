import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import algo
import random
from painter import draw_plot, plt


def app():
    sg.theme('DarkAmber')

    blocks = [[sg.B('example1', key='ex1')], [sg.B('example2', key='ex2')], [sg.B('example3', key='ex3')],
              [sg.B('many random points', key='ex4')], [sg.Canvas(key='controls_cv')],
              [sg.Column(layout=[[sg.Canvas(key='fig_cv', size=(500 * 2, 700))]], pad=(0, 0))]]

    window = sg.Window('Fedchenko labOG', blocks)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'ex1':
            points = [[0, 0], [1, 3], [4, 1], [3, 2], [4, 3]]
            poly = [[1, 2], [3, 3], [4, 4], [5, 2], [3, 1], [1, 2]]
            inside_points = []
            for p in points:
                if algo.ray_tracing_method(p[0], p[1], poly):
                    inside_points.append(p)
            fig, ax = draw_plot(poly, points, inside_points)
            xs, ys = get_bottom_point(points)
            ax.text(xs - 1, ys - 0.5, ("Points inside the poly:", inside_points), fontsize=10)
            draw_polynom(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)
        elif event == 'ex2':
            points = [[0, 0], [1, 3], [4, 0.5], [3, 2], [4, 3]]
            poly = [[1, 2], [5, 4], [7, 4], [10, 4], [9, 3], [8, 2], [6, 1], [2, 1], [1, 2]]
            inside_points = []
            for p in points:
                if algo.ray_tracing_method(p[0], p[1], poly):
                    inside_points.append(p)
            fig, ax = draw_plot(poly, points, inside_points)
            xs, ys = get_bottom_point(points)
            ax.text(xs - 1, ys - 0.5, ("Points inside the poly:", inside_points), fontsize=10)
            draw_polynom(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)
        elif event == 'ex3':
            points = [[0, 0], [1, 3], [4, 0.5], [2, 2], [4, 3], [-1, 2]]
            poly = [[-1, -1], [-2, 2], [1, 4], [3, 0], [1, -1], [-1, -1]]
            inside_points = []
            for p in points:
                if algo.ray_tracing_method(p[0], p[1], poly):
                    inside_points.append(p)
            fig, ax = draw_plot(poly, points, inside_points)
            xs, ys = get_bottom_point(points)
            ax.text(xs - 2, ys - 2, ("Points inside the poly:", inside_points), fontsize=10)
            draw_polynom(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)
        elif event == 'ex4':
            random_points = []
            for i in range(2000):
                random_points.append([random.uniform(-1.0, 12.0), random.uniform(-1.0, 6.0)])
            poly = [[1, 2], [5, 4], [7, 4], [10, 4], [9, 3], [8, 2], [6, 1], [2, 1], [1, 2]]
            inside_points = []
            for p in random_points:
                if algo.ray_tracing_method(p[0], p[1], poly):
                    inside_points.append(p)
            fig, ax = draw_plot(poly, random_points, inside_points)
            xs, ys = get_bottom_point(random_points)
            ax.text(xs - 2, ys - 2, ("Points inside the poly:", inside_points), fontsize=10)
            draw_polynom(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)

    window.close()


# helpers

def get_bottom_point(points):
    xs = []
    ys = []
    for i in points:
        xs.append(i[0])
        ys.append(i[1])
    return np.mean(xs), min(ys)


def draw_polynom(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = NavigationToolbar2Tk(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)
