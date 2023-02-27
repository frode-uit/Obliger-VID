from tkinter import *
import math


def gift_wrapping(points):

    right_most_lowest_point = get_right_most_lowest_point(points)
    hull = [right_most_lowest_point]
    t0 = right_most_lowest_point

    while True:
        t1 = points[0]
        for point in range(len(points)):
            orientation = find_side(t0[0], t0[1], t1[0], t1[1],
                                    points[point][0], points[point][1])

            if orientation < 0:
                t1 = points[point]
            elif orientation == 0:
                if distance(points[point][0], points[point][1], t0[0], t0[1]) > distance(t1[0], t1[1], t0[0], t0[1]):
                    t1 = points[point]

        if t1[0] == right_most_lowest_point[0] and t1[1] == right_most_lowest_point[1]:
            break
        else:
            hull.append(t1)
            t0 = t1

    return hull


def get_right_most_lowest_point(points):
    right_most_index = 0
    right_most_X = points[0][0]
    right_most_Y = points[0][1]

    for i in range(len(points)):
        if right_most_Y > points[i][1]:
            right_most_Y = points[i][1]
            right_most_X = points[i][0]
            right_most_index = i
        elif right_most_Y == points[i][1] and right_most_X < points[i][0]:
            right_most_X = points[i][0]
            right_most_index = i

    return points[right_most_index]


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def find_side(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)


def add(event):
    points.append([event.x, event.y])
    repaint()


def remove(event):
    for [x, y] in points:
        if distance(x, y, event.x, event.y) <= 10:
            points.remove([x, y])
    repaint()


def repaint():
    canvas.delete("point")
    if len(points) > 0:

        hull = gift_wrapping(points)

        canvas.create_polygon(hull, fill="gray", tags="point")

    for [x, y] in points:
        canvas.create_oval(x - radius, y - radius, x +
                           radius, y + radius, tags="point")


def display_instructions():
    instructions = ["INSTRUCTIONS", "Add:",
                    "Left Click", "Remove:", "Right Click"]
    x = 20
    y = 20
    canvas.create_rectangle(x, y, x + 160, y + 80)
    canvas.create_text(x + 10 + 40, y + 20,
                       text=instructions[0], justify=CENTER)
    for i in range(1, len(instructions), 2):
        canvas.create_text(x + 10 + 40, y + 20 + (i + 1) *
                           10, text=instructions[i], justify=RIGHT)
        canvas.create_text(x + 80 + 40, y + 20 + (i + 1) *
                           10, text=instructions[i + 1], justify=RIGHT)


window = Tk()
window.title("Convex Hull")

width = 500
height = 150
radius = 2
canvas = Canvas(window, bg="white", width=width, height=height)
canvas.pack()

points = []

display_instructions()

canvas.bind("<Button-1>", add)
canvas.bind("<Button-3>", remove)


window.mainloop()
