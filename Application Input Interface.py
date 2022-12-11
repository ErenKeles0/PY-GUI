from tkinter import *
import sqlite3
import string
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
Label(window,text="Welcome to Py GUI",font="Verdana 48", bg="black", fg="white").place(x=660,y=20)

#singup function
def signup():
    #get username and password
    username=usernameentry.get()
    password=passwordentry.get()
    userr=username+"/"+password
    x=0
    if len(username)<8 or len(password)<8:
        loginsuccessful["text"]= "Please enter password and username longer than 8 characters"
    else:
        for i in username:#check usernames letters
            if i in string.punctuation:#if username have special char
                loginsuccessful["text"]= "Please do not use special characters in the username"
                break
            else:#everything okay  
                loginsuccessful["text"]= "SignUp Sucsessfuly"
                x=x+1
                if x == len(username):
                    users.append(userr)



#login function
def login():
    username=usernameentry.get()
    password=passwordentry.get()
    #get username and password
    userss=username+"/"+password


    #Check the accuracy of the information
    if userss in users :
        loginsuccessful["text"]= "Login Sucsessfuly"
    else:  
        loginsuccessful["text"]= "Login Failed"

#close application function
def close():
    window.destroy()


#user name and password boxes
usernameentry = Entry(window,font="Verdana 32",bg="black", fg="white")
usernameentry.place(x=700,y=500)
passwordentry = Entry(window,textvariable=StringVar(), show='*',font="Verdana 32",bg="black", fg="white")
passwordentry.place(x=700,y=600)

#login button
loginbuton = Button(text="Login",command=login,font="Verdana 24",bg="White", fg="black").place(x=800,y=700)
loginsuccessful = Label(text="",font="Verdana 24", bg="black", fg="white")
loginsuccessful.pack(side=BOTTOM,)

signupbuton = Button(text="SignUp",command=signup,font="Verdana 24",bg="White", fg="black").place(x=1000,y=700)

#close button
closebuton = Button(text="Exit",command=close,font="Verdana 24",bg="White", fg="black")
closebuton.place(x=1820,y=0)



usernamelbl = Label(text="Username:",font="Verdana 24", bg="black", fg="white").place(x=510,y=500)
passwordlbl = Label(text="Password:",font="Verdana 24", bg="black", fg="white").place(x=510,y=600)




window.mainloop()