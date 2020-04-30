from tkinter import *
def Register():
    Screen2 = Toplevel(Screen)
    Screen2.geometry("400x400")
    Screen2.title("User Register")
    Label(Screen2, text = "", width = 100, height = 1).pack()
    Label(Screen2, text = "Login ", width = 100, height = 2, font = ("Calibri",15)).pack()
    Label(Screen2, text = "", width = 100, height = 1).pack()
    Entry(Screen2, text = "Password", width = 100, height = 2, font = ("Calibri",15)).pack()
    
    
def Login_Section():
    print("") 
def Login():
    Screen1 = Toplevel(Screen)
    Screen1.geometry("400x400")
    Screen1.title("User Login")
    Label(Screen1, text = "", width = 100, height = 1).pack()
    Label(Screen1, text = "Login", width = 100, height = 1, font = ("Calibri",15)).pack()
    Label(Screen1, text = "", width = 100, height = 1).pack()
    User_Login = ""
    Entry(Screen1, text = User_Login, width = 20).pack()
    Password_Login = ""
    Entry(Screen1, text = Password_Login, width = 20).pack()
    Button(Screen1, text = "Login", width = 10, command = Login_Section).pack()

    

def main():
    global Screen
    Screen = Tk()
    Screen.geometry("400x400")
    Screen.title("Dashboard")
    Label(Screen, text = "Welcome to User Data Management", width = 100, height = 2, bg = "grey", font = ("Calibri", 18)).pack()
    Label(Screen, text = "", width = 100, height = 1).pack()
    Button(Screen, text = "Login", width = 10, height = 2, command = Login).pack()
    Label(Screen, text = "", width = 100, height = 1).pack()
    Button(Screen, text = "Register", width = 10, height = 2, command = Register).pack()
    Screen.mainloop()

main()