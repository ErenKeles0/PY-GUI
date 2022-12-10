from tkinter import *
import sqlite3
#user info
users=[]


#window create
window=Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title("Interface")
window.geometry("1920x1080")
window.overrideredirect(True)
window.configure(background="black")

#welcome title
Label(window,text="Welcome to Py GUI",font="Verdana 48", bg="black", fg="white").pack()

#singup function
def signup():
    #get username and password
    username=usernameentry.get()
    password=passwordentry.get()
    users.append(username+"/"+password)





#login function
def login():
    username=usernameentry.get()
    password=passwordentry.get()
    #get username and password
    userss=username+"/"+password


    #Check the accuracy of the information
    if userss in users :
        loginsuccessful["text"]= "Giris Basarili"
    else:  
        loginsuccessful["text"]= "Giris Basarisiz"

#close application function
def close():
    window.destroy()


#user name and password boxes
usernameentry = Entry(window,font="Verdana 32",bg="black", fg="white")
usernameentry.pack()
passwordentry = Entry(window,textvariable=StringVar(), show='*',font="Verdana 32",bg="black", fg="white")
passwordentry.pack()

#login button
loginbuton = Button(text="Login",command=login,font="Verdana 24",bg="White", fg="black").pack()
loginsuccessful = Label(text="",font="Verdana 48", bg="black", fg="white")
loginsuccessful.pack(side=BOTTOM,)

signupbuton = Button(text="signup",command=signup,font="Verdana 24",bg="White", fg="black").pack()

#close button
closebuton = Button(text="Exit",command=close,font="Verdana 24",bg="White", fg="black")
closebuton.pack()
window.mainloop()