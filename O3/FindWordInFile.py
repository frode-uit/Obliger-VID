#Caroline Skymoen V22
import os 
from tkinter import *

dircount = 0
filecount = 0
wordcount = 0

def search():
    global dircount, filecount, wordcount

    dircount = 0
    filecount = 0
    wordcount = 0
    
    file = dir.get()
    word = text.get()
    outp.insert(END, ("Search start" + '\n' + '---------------------------------------------' + '\n'))
    find_input(file, word)

    if wordcount !=0:
        result(word)
    else:
        outp.insert(END, ('"' + word + '"' + " does not exist." + '\n\n'))

def find_input(path, word):
    global dircount
    try:
        if not os.path.isfile(path):
            for dir in os.listdir(path):
                dircount += 1
                list = os.path.join(path,dir)
                find_input(list, word) # Recursive call
    
        else: # Base case
            findWord(path, word)
    except:
        outp.insert(END, "Cannot find directory")

def findWord(file, word):
    global filecount, wordcount
    try:
       
        input_file = open(file, "r")
        filecount += 1 
        for line in input_file:
            if word in line:
                wordcount += 1
                outp.insert(END, (file + ":  " + line + '\n'))

        input_file.close()
    
    except:
        outp.insert(END, "Cannot open file")

def result(word):
    outp.insert(END, "---------------------------------------------" '\n' "Search end." '\n')
    outp.insert(END, ("Searched: " + str(dircount) +" directories and " + str(filecount) + 
                        " files, found " + str(wordcount) + " occurences of " + '"' + str(word) + '"' + '\n\n'))

window = Tk()
window.geometry('1000x500')
window.title("Find word in files")

dir = Entry(window)
dir.place( x = 20, y = 20, width = 500, height = 20)
dir.config(fg = "grey")
dir.insert(END, "Directory or filename")

text = Entry(window)
text.place( x = 550, y = 20, width = 370, height = 20)
text.config(fg = "grey")
text.insert(END, "Word")

outp = Text(window)
outp.place( x = 20 , y = 60, width = 960, height = 400)

btn = Button(window, text ="Search", command = search)
btn.place(x = 930, y = 20)
 
def handle_dir(entry):
    dir.delete(0, END)
    dir.config(fg='black')

def handle_text(entry):
    text.delete(0, END)
    text.config(fg='black')

dir.bind("<FocusIn>", handle_dir)
text.bind("<FocusIn>", handle_text)

window.mainloop()