from tkinter import * 
import tkinter
from PIL import ImageTk, Image
def box():
    from tkinter import messagebox
    import Level1
    messagebox.showinfo("SET - CARDS", "Thank You")
    print(e1.get())
def clear():
    e1 = Entry(top).place(x = 390, y = 218)  
    e2 = Entry(top).place(x = 400, y = 300)  
top= Tk()
top.title("Set-cards")
#top.wm_icobitmap('User.ico')
img = ImageTk.PhotoImage(Image.open('back.gif'))
w = Label(top,image = img)
w.pack(side = "bottom", fill = "both", expand = "yes")
w = Label(top,text="SET CARD GAME ",font =('SET CARD GAME',20))
w.pack()
top.geometry("800x600")
top.config(bg='grey')
name = Label(top, text = "Full Name").place(x = 316,y = 218)
nick = Label(top, text = "Nick Name").place(x = 314, y =300)  
resetbtn = Button(top, text = "Reset",command =clear ,activebackground = "pink", activeforeground = "blue").place(x = 466, y = 416)
sbmitbtn = Button(top, text = "Play",command = box,activebackground = "pink", activeforeground = "blue").place(x = 426, y = 416)
e1 = Entry(top).place(x = 390, y = 218)  
e2 = Entry(top).place(x = 400, y = 300) 
#e1.Pack()
#e2.Pack()
#sbmitbtn.Pack()
#name.Pack()
#nick.Pack()

w.config(bg='green')
w.config(fg='white')
top.mainloop()