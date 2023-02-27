from tkinter import * # Import tkinter
import tkinter.messagebox # Import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import os

class DirectorySearch:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Find word in files") # Set title

        frame2 = Frame(window)
        frame2.pack()

        self.filename = StringVar()
        self.filename.set("Directory or filename")
        textBox = Entry(frame2, width = 20, textvariable = self.filename).pack(side = LEFT)
        self.word = StringVar()
        self.word.set("Word")
        textBox = Entry(frame2, width = 20, textvariable = self.word).pack(side = LEFT)
        Button(frame2, text = "Search", command = self.searchDirectory).pack(side = LEFT)

        frame1 = Frame(window) 
        frame1.pack()

        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill = Y)
        self.text = Text(frame1, width = 120, height = 40, wrap = WORD, 
                    yscrollcommand = scrollbar.set)
        self.text.pack()
        scrollbar.config(command = self.text.yview)
        window.mainloop() # Create an event loop

    def findInFile(self, file, word):
        if not os.path.isfile(file):
            self.dirCount +=1
            lst = os.listdir(file) # All files and subdirectories
            for subdirectory in lst:
                self.findInFile(file + "//" + subdirectory, word) 
        else: # Base case, it is a file
            self.fileCount +=1
            self.findWord(file, word)

    def findWord(self, filename, word):
        try:
            with open(filename, "r") as  inputFile: # Open the file
                for line in inputFile:   
                    if line.__contains__(word):
                        self.hits +=1
                        self.text.insert(INSERT, filename + ": " + line + "\n")
        except:
            self.openFail+=1

    def searchDirectory(self): 
        try:
            self.hits =0
            self.openFail = 0
            self.dirCount = 0 
            self.fileCount = 0
            self.text.delete(1.0, 'end')
            self.text.insert(END, "Search start... \n ............................")
            self.findInFile(self.filename.get(), self.word.get())
            self.text.insert(END, "............................ \nSearch end... \n")
            self.text.insert(END, "Searched: " + str(self.dirCount) + " directories and " + str(self.fileCount) + " files, found: " + str(self.hits) + " Unreadable: " + str(self.openFail) + " \n")

        except IOError:
            self.text.delete(1.0, 'end')
            tkinter.messagebox.showwarning("Count words", 
                                        "Directory " + str(self.filename.get()) + " does not exist")

DirectorySearch()