from tkinter import *
#from tkinter import ttk, colorchooser
from PIL import ImageTk, Image
import os

os.chdir(os.path.dirname(__file__))
root = Tk()
root.title("img_viewer")

img_1 = ImageTk.PhotoImage(Image.open(r"./Images/orange.jpg"))
img_2 = ImageTk.PhotoImage(Image.open(r"./Images/pear.jpg"))
img_3 = ImageTk.PhotoImage(Image.open(r"./Images/Pear.png"))
img_4 = ImageTk.PhotoImage(Image.open(r"./Images/rabbit.jpg"))

img_list = [img_1, img_2, img_3 , img_4]

Status = Label(root, text = "Image 1 of "+ str(len(img_list)),padx = 5, pady = 5, bd = 2 , relief = SUNKEN, anchor = E)

def forward(img_num):
    global my_label
    global Button_forward
    global Button_back

    my_label.grid_forget()
    my_label = Label(image = img_list[img_num-1])
    Button_forward = Button(root, text = ">>",padx = 20, pady = 10 ,command = lambda : forward(img_num + 1))
    Button_back = Button(root, text = "<<",padx = 20, pady = 10 ,command = lambda: back(img_num - 1))
    
    if img_num == 4:
        Button_forward = Button(root, text = ">>",padx = 20, pady = 10, state = DISABLED)

    my_label.grid(row= 0, column = 0, columnspan = 3)
    Button_back.grid(row= 1, column =0)
    Button_forward.grid(row = 1, column = 2)

    Status = Label(root, text = "Image " + str(img_num) + " of  " + str(len(img_list)),padx = 5, pady = 5, bd = 2 , relief = SUNKEN, anchor = E)
    Status.grid(row = 2 , column = 0, columnspan = 3, sticky = W+E)

    

def back(img_num):
    global my_label
    global Button_forward
    global Button_back

    my_label.grid_forget()

    my_label = Label(image = img_list[img_num-1])
    Button_forward = Button(root, text = ">>",padx = 20, pady = 10 ,command = lambda : forward(img_num + 1))
    Button_back = Button(root, text = "<<",padx = 20, pady = 10 ,command = lambda: back(img_num - 1))

    if img_num == 1:
        Button_back = Button(root, text = "<<",padx = 20, pady = 10, state = DISABLED)

    my_label.grid(row= 0, column = 0, columnspan = 3)
    Button_back.grid(row= 1, column =0)
    Button_forward.grid(row = 1, column = 2)


    Status = Label(root, text = "Image " + str(img_num) + " of  " + str(len(img_list)),padx = 5, pady = 5, bd = 2 , relief = SUNKEN, anchor = E)
    Status.grid(row = 2 , column = 0, columnspan = 3, sticky = W+E)


Button_back = Button(root, text = "<<", padx = 20, pady = 10, command = lambda : back(2))
Button_exit = Button(root, text = "exist",padx = 20, pady=10 ,command = root.quit)
Button_forward = Button(root, text=">>", padx = 20, pady = 10, command = lambda : forward(2))

Button_back.grid(row= 1, column =0)
Button_exit.grid(row =1 , column = 1, pady = 10)
Button_forward.grid(row = 1, column = 2)

my_label = Label(image = img_1)
my_label.grid(row= 0, column = 0, columnspan = 3)
Status.grid(row = 2 , column = 0, columnspan = 3, sticky = W+E)


#Status = Label(root, text = "Image " + str(len(img_list)+1) + " of  " + str(len(img_list)),padx = 5, pady = 5, bd = 2 , relief = SUNKEN, anchor = E)



root.mainloop()