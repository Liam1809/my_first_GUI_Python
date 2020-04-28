from tkinter import *
def Register():
    Screen2 = Toplevel(Screen)
    Screen2.geometry("400x400")
    Screen2.title("User Register")
    
    
def Login():
    Screen1 = Toplevel(Screen)
    Screen1.geometry("400x400")
    Screen1.title("User Login")
    

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