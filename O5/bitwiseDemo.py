# fn apr 22
from tkinter import *
from tkinter.ttk import Combobox

def create_bitstr1(event):
    num1 = int(ent_int1_from_user.get())
    lab_int1_from_user_as_bitstr['text'] = f'{num1:08b}'   
    
def create_bitstr2(event):
    num2 = int(ent_int2_from_user.get())
    lab_int2_from_user_as_bitstr['text'] = f'{num2:08b}'

def btn_check_clicked():
    users_bitstr = ent_bitstr_from_user.get().strip()
    choice = cmb_choose_operator.get()
    op1 = int(ent_int1_from_user.get())
    op2 = int(ent_int2_from_user.get())
    if choice == "AND":
        result = op1 & op2
    elif choice == "OR":
        result = op1 | op2
    elif choice == "OCOMP":
        result = ~op1 & 255
    if choice == "XOR":
        result = op1 ^ op2
    elif choice == "SHIFTLEFT":
        result = op1 << 1 & 255
    elif choice == "SHIFTRIGHT":
        result = op1 >> 1 & 255
    correct_bitstr = f'{result:08b}'
    if users_bitstr == correct_bitstr:
        ent_bitstr_from_user["bg"] = "green"
    else:
        ent_bitstr_from_user["bg"] = "red"
    lbl_correct_bitstr["text"] = correct_bitstr
        

window = Tk()
window.title("Bitwise operators")
window.geometry('700x100')

# Labels for entry fields
Label(window, text="First number, range 0 - 255").grid(column=0, row=0, sticky="w")
Label(window, text="Second number, range 0 - 255").grid(column=0, row=1, sticky="w")
Label(window, text="Your answer").grid(column=0, row=2, sticky="w")
Label(window, text="Correct answer", justify=LEFT).grid(column=0, row=3, sticky="w")
Label(window, text="Only this for SHIFTRIGHT(1), SHIFTLEFT(1), OCOMP").grid(column=3, row=0, sticky="w")

# The entry fields for the two operands from the user
ent_int1_from_user = Entry(window,width=3,text="")
ent_int1_from_user.grid(column=1, row=0)
ent_int2_from_user = Entry(window,width=3,text="")
ent_int2_from_user.grid(column=1, row=1)
# Labels to display bitstr
lab_int1_from_user_as_bitstr = Label(window, width=10)
lab_int1_from_user_as_bitstr.grid(column=2, row=0)
lab_int2_from_user_as_bitstr = Label(window, width=10)
lab_int2_from_user_as_bitstr.grid(column=2, row=1)
#entry for users answer and label for correct
ent_bitstr_from_user = Entry(window,width=8,text="") # the users answer
ent_bitstr_from_user.grid(column=2, row=2)
lbl_correct_bitstr = Label(window, width=8)
lbl_correct_bitstr.grid(column=2, row=3)

# combo box for choosing operation
cmb_choose_operator = Combobox(window)
cmb_choose_operator['values']=("AND", "OR", "OCOMP", "XOR", "SHIFTLEFT", "SHIFTRIGHT")
cmb_choose_operator.current(0)
cmb_choose_operator.grid(column=3, row=2)

# Button to start the show
btn_check = Button(window, text="Check", command=btn_check_clicked)
btn_check.grid(column=4, row=2)
ent_int1_from_user.bind('<FocusOut>', create_bitstr1)
ent_int2_from_user.bind('<FocusOut>', create_bitstr2)

window.mainloop()