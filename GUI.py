from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from functools import partial
import os
import emailsender
import InstaSender
import shutil

#clean existing insta config file, if any
configCheck = os.path.abspath(os.getcwd()) + "/config"
if (os.path.isdir(configCheck)):
    if (configCheck == "/"):
        quit()
    shutil.rmtree(configCheck)


root = Tk()
root.geometry('500x500')  
root.title('All-In-One Message Sender')
root.configure(background="#263d42")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#frame for user input
userInput = Frame(root)
textBox = Text(userInput, bg="white", font=('TimesNewRoman', 12))

#email sender input
email = Entry(userInput, bg="white", font=("TimesNewRoman", 12))
emailLabel = Label(userInput, text="Recipient")

#body of message input
userTextLabel = Label(userInput, text="Message")
userText = StringVar()

#subject line input
subjectEntry = Entry(userInput, bg="white", font=("TimesNewRoman", 12))
subjectLabel = Label(userInput, text="Subject")
subjectText = StringVar()

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
"Instagram (.jpg only)",
"Gmail"
]
platform = StringVar(root)

facebookBox = IntVar()
facebookButton = Checkbutton(userInput, text="Facebook", variable=facebookBox)
twitterBox = IntVar()
twitterButton = Checkbutton(userInput, text="Twitter", variable=twitterBox)
instagramBox = IntVar()
def checkInstagram():
    if (instagramBox.get()):
        InstaSender.filename = filedialog.askopenfilename(initialdir = "/", title = "Select an image before continuing", filetypes = (("JPGs", "*.jpg*"), ("All files", "*.*")))
instagramButton = Checkbutton(userInput, text="Instagram", variable=instagramBox, command=checkInstagram)
gmailBox = IntVar()
def checkGmail():
    if (gmailBox.get()):
        email.configure(state="normal")
    else:
        email.configure(state="disabled")
gmailButton = Checkbutton(userInput, text="G-Mail", variable=gmailBox, command=checkGmail)
email.configure(state="disabled")





#---------------------Post Message------------------------------------------#
def post():
    if (facebookBox.get()):
        facebook()

    if (gmailBox.get()):
        r_address = email.get()
        subject = subjectEntry.get()
        msg = textBox.get("1.0", END)
        emailsender.gmail(r_address, subject, msg)

    if (twitterBox.get()):
        twitter()

    if (instagramBox.get()):
        InstaSender.instagram(InstaSender.filename, textBox.get("1.0", END))

    #check if sent folder exists, if not, make it and add post to folder
    path = os.path.abspath(os.getcwd())
    print(path)
    path += "/Sent"
    if (not os.path.isdir(path)):
        os.mkdir(path)
    input = textBox.get("1.0",END)
    fileName = subjectEntry.get()
    toSave = open(fileName, "w")
    toSave.write(input)
    fromDir = os.path.abspath(os.getcwd()) + "/" + fileName
    toDir = os.path.abspath(os.getcwd()) + "/Sent/" + fileName
    shutil.move(fromDir, toDir)


#--------------------------Build GUI-------------------------------------#
def enter():
    #user authenticated
    login.destroy()

    #establish boxes and labels
    email.place(relwidth=0.8, relx=0.14, rely=0.01)
    emailLabel.place(relx=0, rely=0.01)
    textBox.place(relwidth=0.8, relheight=0.8, relx=0.14, rely=0.14)
    userInput.place(relwidth=0.9, relheight=0.85, relx=0.05, rely=0.05)
    userTextLabel.place(relx=0, rely=0.14)
    subjectEntry.place(relwidth=0.8, relx=0.14, rely=0.07)
    subjectLabel.place(relx=0, rely=0.07)

    #establish check boxes
    facebookButton.place(relx=0.08, rely=0.942)
    twitterButton.place(relx=0.3, rely=0.942)
    instagramButton.place(relx=0.49, rely=0.942)
    gmailButton.place(relx=0.73, rely=0.942)

    Button(root, text="Post Message", command=post).grid(row=6, column=0)
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

def test():
    print("test")

def new():
    textBox.delete('1.0', END)

def browse():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Browse Files", filetypes = (("Text files", "*.txt*"), ("All files", "*.*")))
    with open(filename, 'r') as file:
        textBox.insert(INSERT, file.read())

def save():
    data = [('All types(*.*)', '*.*')]
    input = textBox.get("1.0",END)
    newSave = filedialog.asksaveasfile(filetypes = data, defaultextension = ".txt")
    newSave.write(input)


root.mainloop()
