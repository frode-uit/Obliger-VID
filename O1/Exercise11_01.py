from tkinter import * # Import tkinter

class ComboBoxDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Select Shapes") # Set title

        # Create a combo box to select a country
        var = StringVar()
        var.set("rectangle") # initial value
        comboBox = OptionMenu(window, var, "rectangle", "oval", "arc", 
            "polygon", "line", 
            command = self.processSelection).pack(fill = BOTH)

        self.canvas = Canvas(window)
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "drawing")
        self.canvas.pack()
        
        window.mainloop() # Create an event loop
        
    # Display image for selected country
    def processSelection(self, selectedItem):
        self.canvas.delete("drawing")
        if selectedItem == "rectangle":
            self.canvas.create_rectangle(10, 10, 190, 90, tags = "drawing")
        elif selectedItem == "oval":
            self.canvas.create_oval(10, 10, 190, 90, fill = "red", tags = "drawing")
        elif selectedItem == "arc":
            self.canvas.create_arc(10, 10, 190, 90, start = 0, 
            extent = 90, width = 8, fill = "red", tags = "drawing")
        elif selectedItem == "polygon":
            self.canvas.create_polygon(10, 10, 190, 90, 30, 50, 
                tags = "drawing")
        elif selectedItem == "line":
            self.canvas.create_line(10, 10, 190, 90, fill = "red", 
                tags = "drawing")
            self.canvas.create_line(10, 90, 190, 10, width = 9, 
                arrow = "last", activefill = "blue", tags = "drawing")
            
ComboBoxDemo() # Create GUI 