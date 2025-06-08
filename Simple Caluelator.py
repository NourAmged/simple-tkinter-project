from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root,width=50, borderwidth = 3)

e.grid(row = 0, column= 0, columnspan = 3, padx = 10, pady = 10)


def button_click(num):
        #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(num))

def button_clear():
    e.delete(0,END)

def button_add():
    num_1 = e.get()
    global num
    global math
    math = "add"  
    num  = float(num_1)
    e.delete(0,END)

def button_equal():
    num_2 = e.get()
    e.delete(0,END)
    if math == "add":
        e.insert(0, num + int(num_2))
        
    if math == "divide":
        e.insert(0, num / int(num_2))

    if math == "substract":
        e.insert(0, num - int(num_2))
        
    if math == "multiply":
        e.insert(0, num * int(num_2))

def button_divide():
    num_1 = e.get()
    global num
    global math
    math = "divide"  
    num  = float(num_1)
    e.delete(0,END)

def button_substract():
    num_1 = e.get()
    global num
    global math
    math = "substract"  
    num  = float(num_1)
    e.delete(0,END)

def button_multiply():
    num_1 = e.get()
    global num
    global math
    math = "multiply"  
    num  = float(num_1)
    e.delete(0,END)



Button_1 = Button(root, text="1", padx = 50, pady = 20 , command = lambda : button_click(1))
Button_2 = Button(root, text="2", padx = 50, pady = 20 , command = lambda : button_click(2))
Button_3 = Button(root, text="3", padx = 50, pady = 20 , command = lambda : button_click(3))
Button_4 = Button(root, text="4", padx = 50, pady = 20 , command = lambda : button_click(4))
Button_5 = Button(root, text="5", padx = 50, pady = 20 , command = lambda : button_click(5))
Button_6 = Button(root, text="6", padx = 50, pady = 20 , command = lambda : button_click(6))
Button_7 = Button(root, text="7", padx = 50, pady = 20 , command = lambda : button_click(7))
Button_8 = Button(root, text="8", padx = 50, pady = 20 , command = lambda : button_click(8))
Button_9 = Button(root, text="9", padx = 50, pady = 20 , command = lambda : button_click(9))
Button_0 = Button(root, text="0", padx = 50, pady = 20 , command = lambda : button_click(0))

Button_add = Button(root, text="+", padx = 49, pady = 20, command = button_add)
Button_equal = Button(root, text="=", padx = 104, pady = 20 , command = button_equal)
Button_clear = Button(root, text="Clear", padx = 94, pady = 20 , command = button_clear) 

Button_divide = Button(root, text="/", padx = 50, pady = 20, command = button_divide)
Button_substract = Button(root, text="-", padx = 50, pady = 20, command = button_substract)
Button_multiply= Button(root, text="*", padx = 48, pady = 20, command = button_multiply)


Button_1.grid(row = 3 , column = 0)
Button_2.grid(row = 3, column = 1)
Button_3.grid(row = 3, column = 2)

Button_4.grid(row = 2, column = 0)
Button_5.grid(row = 2, column = 1)
Button_6.grid(row = 2, column = 2)

Button_7.grid(row = 1, column = 0)
Button_8.grid(row = 1, column = 1)
Button_9.grid(row = 1, column = 2)

Button_0.grid(row = 4, column = 0)

Button_equal.grid(row = 5, column = 1,columnspan = 2)
Button_add.grid(row = 5, column = 0)
Button_clear.grid(row = 4, column = 1,columnspan = 2)

Button_substract.grid(row = 6, column = 0)
Button_multiply.grid(row = 6, column = 1)
Button_divide.grid(row = 6, column = 2)


root.mainloop()