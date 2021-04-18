from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from functools import partial
import os
import emailsender
import InstaSender


root = Tk()
root.geometry('500x500')  
root.title('All-In-One Message Sender')
root.configure(background="#263d42")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

textBox = Text(root, bg="white", font=('TimesNewRoman', 12))

#-------------Login------------------------------------------------#
def validateLogin(username, password):
    print("Username: ", username.get())
    print("Password: ", password.get()) 
    #check input against dummy values to verify login
    #real implementation should involve real credentialing
    if (username.get() == "321" and password.get() == "dl4"):
        enter()
    else:
        newWindow = Toplevel()
        newWindow.geometry('200x80') 
        popup = Message(newWindow, text = "Invalid Credentials\n").grid(row = 5, column=5)
        newWindow.mainloop()
    return

login = Frame(root)
login.place(relwidth=0.6, relheight=0.2, relx=0.2, rely=0.3)


#username label and text entry box
usernameLabel = Label(login, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(login, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(login,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(login, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(login, text="Login", command=validateLogin).grid(row=4, column=0)


#--------------------Select Platform---------------------------------#
platforms = [
"Facebook",
"Twitter",
"Instagram",
"Gmail"
]

platform = StringVar(root)
platform.set(platforms[0]) # default value is Facebook

def changeOption(*args):
    platform.set(platform.get())
    print ("Platform selected is " + platform.get())
    if (platform.get() == "Gmail"):
        textBox.delete('1.0', END)
        emailInput()
    elif (platform.get() == "Facebook"):
        textBox.delete('1.0', END)
        facebookInput()
    elif (platform.get() == "Twitter"):
        textBox.delete('1.0', END)
        twitterInput()
    elif (platform.get() == "Instagram"):
        textBox.delete('1.0', END)
        instagramInput()
        instagramSetup()

platform.trace('w', changeOption) 


#--------------------Platform Setup---------------------------------#
def emailInput():
    textBox.insert("1.0", "For proper functionality, please type under each prompt.\n")
    textBox.insert("2.0", "Enter the email address of the receiving party:\n\n")
    textBox.insert("4.0", "Subject of your email:\n\n")
    textBox.insert("6.0", "Main Message:\n\n")
    
def facebookInput():
    textBox.insert("1.0", "Please enter your post below:\n")

def twitterInput():
    textBox.insert("1.0", "Please enter your Tweet below\n")

def instagramInput():
    textBox.insert("1.0", "*Note: all images uploaded should be jpg*\n")
    textBox.insert("2.0", "File Opened: None\n")
    textBox.insert("3.0", "Please enter your caption below\n")

def instagramSetup():
    InstaSender.filename = filedialog.askopenfilename(initialdir = "/", title = "Select an image before continuing", filetypes = (("JPGs", "*.jpg*"), ("All files", "*.*")))
    textBox.delete("2.0", "2.0 lineend")
    textBox.insert("2.0", "File Opened: " + InstaSender.filename)

#---------------------Post Message------------------------------------------#
def post():
    current = platform.get()
    if (current == "Facebook"):
        facebook()

    elif (current == "Gmail"):
        r_address = textBox.get("3.0", "3.0 lineend")
        subject = textBox.get("5.0", "5.0 lineend")
        msg = textBox.get("7.0", "7.0 lineend")
        emailsender.gmail(r_address, subject, msg)
        textBox.delete("1.0", END)
        emailInput()

    elif (current == "Twitter"):
        twitter()

    else:
        InstaSender.instagram(InstaSender.filename, textBox.get("4.0", "4.0 lineend"))
        textBox.delete("1.0", END)
        instagramInput()
        instagramSetup()

    print("Posted to " + current)




#--------------------------Build GUI-------------------------------------#
def enter():
    login.destroy()
    textBox.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)
    newMessage = Button(root, text="Post Message", command=post).grid(row=6, column=0)
    platformSelect = OptionMenu(root, platform, *platforms).grid(row=5, column=0)
    #Menu bar
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=new)
    filemenu.add_command(label="Open", command=browse)
    filemenu.add_command(label="Save", command=save)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=test)
    helpmenu.add_command(label="About...", command=test)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

#def test():
#    print("test")

def new():
    textBox.delete('1.0', END)

def browse():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Browse Files", filetypes = (("Text files", "*.txt*"), ("All files", "*.*")))
    with open(filename, 'r') as file:
        textBox.insert(INSERT, file.read())

def save():
    data = [('All types(*.*)', '*.*')]
    input = textBox.get("1.0",END)
    file = asksaveasfile(filetypes = data, defaultextension = ".txt")
    file.write(input)


root.mainloop()

