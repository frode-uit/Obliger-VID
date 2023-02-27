from tkinter import * # Import tkinter
import math

def add(event):
    points.append([event.x, event.y])
    repaint()

def remove(event):
    for [x, y] in points:
        if distance(x, y, event.x, event.y) <= 10:
            points.remove([x, y])
    repaint()

def distance(x, y, x1, y1):
    return ((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 0.5

def repaint():
    canvas.delete("point")
    if len(points) > 0:
        H = getConvexHull(points)
        canvas.create_polygon(H, fill = "gray", tags = "point")

    for [x, y] in points:
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, tags = "point")
    
def displayInstructions():
    instructions = ["INSTRUCTIONS", "Add:", "Left Click", "Remove:", "Right Click"]
    x = 20
    y = 20
    canvas.create_rectangle(x, y, x + 160, y + 80)
    canvas.create_text(x + 10 + 40, y + 20, text = instructions[0], justify = CENTER)
    for i in range(1, len(instructions), 2):
        canvas.create_text(x + 10 + 40, y + 20 + (i + 1) * 10, text = instructions[i], justify = RIGHT)
        canvas.create_text(x + 80 + 40, y + 20 + (i + 1) * 10, text = instructions[i + 1], justify = RIGHT)
        
# Return the points that form a convex hull 
def getConvexHull(myPoints):   
    # Step 1
    h0 = getRightmostLowestPoint(myPoints)
    
    H = [h0]    
    t0 = h0
        
    # Step 2 and Step 3
    while True:   
        t1 = myPoints[0]
        for i in range(1, len(myPoints)):
            status = whichSide(t0[0], t0[1], t1[0], t1[1], myPoints[i][0], myPoints[i][1])
        
            if status < 0:  # Right side of the line
                t1 = myPoints[i]
            elif status == 0:
                if distance(myPoints[i][0], myPoints[i][1], t0[0], t0[1]) > distance(t1[0], t1[1], t0[0], t0[1]):
                    t1 = myPoints[i]
      
        if t1[0] == h0[0] and t1[1] == h0[1]: 
            break; # A convex hull is found
        else:
            H.append(t1)
            t0 = t1
    
    return H
  
# Return the rightmost lowest point in S 
def getRightmostLowestPoint(p):
    rightMostIndex = 0;
    rightMostX = p[0][0];
    rightMostY = p[0][1];
    
    for i in range(1, len(p)):
        if rightMostY > p[i][1]:
            rightMostY = p[i][1]
            rightMostX = p[i][0]
            rightMostIndex = i
        elif rightMostY == p[i][1] and rightMostX < p[i][0]:
            rightMostX = p[i][0]
            rightMostIndex = i   
    
    return p[rightMostIndex]
  
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
  
# Is (x2, y2) on the right side of [x0, y0] and [x1, y1]  
def whichSide(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

window = Tk() # Create a window
window.title("Convex Hull") # Set title

width = 500
height = 150
radius = 2
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

# Create a 2-D list for storing points
points = []

displayInstructions()

canvas.bind("<Button-1>", add)
canvas.bind("<Button-3>", remove)


window.mainloop() # Create an event loop
