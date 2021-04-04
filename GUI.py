from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from functools import partial
import os

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
"LinkedIn",
"Instagram"
]

platform = StringVar(root)
platform.set(platforms[0]) # default value is Facebook


def changeOption(*args):
    platform.set(platform.get())
    print ("Platform selected is " + platform.get())

platform.trace('w', changeOption)



#---------------------Post Message------------------------------------------#
def post():
    current = platform.get()
#    if (current == "Facebook"):
#        facebook()
#    else if (current == "Twitter"):
#        twitter()
#    else if (current == "LinkedIn"):
#        linkedin()
#    else:
#        instagram()
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
    filemenu.add_command(label="New", command=test)
    filemenu.add_command(label="Open", command=test)
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

def save():
    data = [('All tyes(*.*)', '*.*')]
    input = textBox.get("1.0",END)
    file = asksaveasfile(filetypes = data, defaultextension = ".txt")
    file.write(input)


root.mainloop()
"""
class App:

    def __init__(self, master):

        frame = tk.Frame(master, height=700, width=700, bg="#263D42")
        frame.pack()

        self.newMessage = tk.Button(root, text="New Message", padx=10, pady=5, bg="#263D42", fg="white")
        self.newMessage.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print ("hello world")

root = tk.Tk()

app = App(root)

root.mainloop()
"""
