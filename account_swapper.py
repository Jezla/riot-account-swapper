import os
import tkinter as tk
from tkinter import Frame, BOTTOM, simpledialog
import time
import keyboard
from tinydb import TinyDB, Query


def open_exe_with_param(param):
    # Path to the executable you want to open
    pathenv = os.getenv('LOCALAPPDATA')
    dir_path = pathenv + r'\riot_thing'
    db = TinyDB(dir_path + r'\db.json')
    #print(db.all()[param]['user'])
    #print(db.all()[param]['pass'])
    
    try:
        # Launch the executable with the given parameter
        os.startfile(r"C:\Riot Games\Riot Client\RiotClientServices.exe")
        time.sleep(5)
        keyboard.write(db.all()[param]['user'])
        keyboard.press_and_release('tab')
        keyboard.write(db.all()[param]['pass'])
        keyboard.press_and_release('enter')
        exit()
    except Exception as e:
        print(f"Error: {e}")




def centre_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    

def create_gui():
    # Initialize the GUI application
    root = tk.Tk()
    
    root.minsize(400,500)
    root.title("Riot Launcher")
    topFrame = Frame(root)
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    centre_window(root)
    
    

    # Define buttons and their parameters
    
    pathenv = os.getenv('LOCALAPPDATA')
    dir_path = pathenv + r'\riot_thing'
    db = TinyDB(dir_path + r'\db.json')
    for i in db.all():
        print("asd")
    button_configs = [(db.all()[i]['name'], i) for i in range(len(db.all()))]
    
    if len(db.all()) > 0:
    # Create buttons dynamically
        for text, param in button_configs:
            btn = tk.Button(topFrame, width=15, text=text, command=lambda p=param: open_exe_with_param(p))
            btn.pack(pady=8)
    
    btn1 = tk.Button(bottomFrame, width=15, text="Add Account", command=lambda: add_account())

    btn2 = tk.Button(bottomFrame, width=15, text="Exit", command=root.destroy)

    
    btn1.grid(column=0, row = 1, padx=10, pady=10)
    btn2.grid(column=1, row = 1, padx=10, pady=10)
    
    def add_account():
        pathenv = os.getenv('LOCALAPPDATA')
        dir_path = pathenv + r'\riot_thing'
        db = TinyDB(dir_path + r'\db.json')
        USER_INP = simpledialog.askstring(title="New account", prompt="Input data in this format:  display name,username,password:")
        # add error checking I guess
        user_list = USER_INP.split(',')
        db.insert({'name': user_list[0], 'user': user_list[1], 'pass': user_list[2]})
        root.destroy()
        create_gui()
    # Run the application
    root.mainloop()

def check_for_db():
    # old code to check
    pathenv = os.getenv('LOCALAPPDATA')
    dir_path = pathenv + r'\riot_thing'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        db = TinyDB(dir_path + r'\db.json')
    



if __name__ == "__main__":
    check_for_db()
    create_gui()