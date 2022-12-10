from tkinter import *

window=Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("Interface")
window.geometry("1920x1080")
window.overrideredirect(True)
window.configure(background="black")
Label(window,text="Welcome to Py GUI",font="Verdana 48", bg="black", fg="white").pack()



def login():
    loginsuccessful["text"]= "Giris Basarili"
 
def close():
    window.destroy()



loginbuton = Button(text="Login",command=login,font="Verdana 24",bg="White", fg="black").pack()
loginsuccessful = Label(text="",font="Verdana 48", bg="black", fg="white")
loginsuccessful.pack(side=BOTTOM,)


closebuton = Button(text="Exit",command=close,font="Verdana 24",bg="White", fg="black")
closebuton.pack()
window.mainloop()