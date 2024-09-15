import tkinter as tk
import random as ra
import threading as td
import time as ti
def Death():
    root = tk.Tk()
    width = 200
    height = 50
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = ra.randint(0, screenwidth)
    y = ra.randint(0, screenheight)
    root.title("警告")
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    tk.Label(root, text='你的电脑已中毒!', fg='white', bg='black', font=("Comic Sans MS", 15), width=30, height=5).pack()
    root.mainloop()
def Start():
    for i in range(50):
        t = td.Thread(target=Death)
        ti.sleep(0.1)
        t.start()
Start()