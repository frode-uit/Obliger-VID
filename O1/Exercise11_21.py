from tkinter import * # Import tkinter

class Ball:
    def __init__(self):
        self.x = 0 # Starting x position
        self.y = 0
        self.dx = 2
        self.dy = 2
        self.radius = 3
        self.color = getRandomColor()

# Return a random color string in the form #RRGGBB
from random import randint
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15))
    return color

# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if hexValue <= 9 and hexValue >= 0:
        return chr(hexValue + ord('0'))
    else:  # hexValue <= 15 && hexValue >= 10
        return chr(hexValue - 10 + ord('A'))

width = 350 # Width of the canvas
height = 150 # Width of the canvas
    
class MainGUI:
    def __init__(self):                               
        window = Tk() # Create a window
        window.title("Bouncing Balls") # Set a title
        
        self.ballList = [] 
        self.sleepTime = 100 # Set a sleep time 
        self.isStopped = False
        
        self.canvas = Canvas(window, bg = "white", width = width, height = height)
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume", command = self.resume)
        btResume.pack(side = LEFT)
        btAdd = Button(frame, text = "+", command = self.add)
        btAdd.pack(side = LEFT)
        btRemove = Button(frame, text = "-", command = self.remove)
        btRemove.pack(side = LEFT)
        btFaster = Button(frame, text = "Faster", command = self.faster)
        btFaster.pack(side = LEFT)
        btSlower = Button(frame, text = "Slower", command = self.slower)
        btSlower.pack(side = LEFT)
        
        import random 
        color = "#" + hex(random.randint(0, 15)) 
        print(color)
        #canvas.create_oval(10, 10, 40, 40, fill = "#AABBCC")
        self.animate()
        
        window.mainloop() # Create an event loop
        
    def stop(self): # Stop animation
        self.isStopped = True

    def resume(self): # Resume animation
        self.isStopped = False   
        self.animate()
    
    def add(self): # Add a new ball
        self.ballList.append(Ball())
    
    def remove(self): # Remove the last ball 
        self.ballList.pop()
        
    def faster(self): # Speed up the animation
        if self.sleepTime > 5:
            self.sleepTime -= 20
               
    def slower(self): # Slow down the animation
        self.sleepTime += 20
                                
    def animate(self): # Move the message
        while not self.isStopped:
            self.canvas.after(self.sleepTime) # Sleep for 100 milliseconds
            self.canvas.update() # Update canvas
            self.canvas.delete("ball") 
            
            for ball in self.ballList:
                self.redisplayBall(ball)
    
    def redisplayBall(self, ball):
        if ball.x >= width:
            ball.dx = -2
        elif ball.x < 0:
            ball.dx = 2
            
        if ball.y >= height:
            ball.dy = -2
        elif ball.y < 0:
            ball.dy = 2
    
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius, ball.x + ball.radius, ball.y + ball.radius, fill = ball.color, tags = "ball")
        
MainGUI()
