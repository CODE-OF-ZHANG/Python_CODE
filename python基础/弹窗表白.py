import tkinter as tk
import random as ra
import threading as td
import time as ti


def Love1():
    root = tk.Tk()
    width = 200
    height = 50
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = ra.randint(0, screenwidth / 2)
    y = ra.randint(0, screenheight / 2)
    root.title("❤")
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    tk.Label(root, text='I LOVE YOU!', fg='white', bg='pink', font=("Comic Sans MS", 15), width=30, height=5).pack()
    root.mainloop()


def Love2():
    root = tk.Tk()
    width = 200
    height = 50
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    screenheight -= 2 * width
    x = ra.randint(screenwidth / 2, screenwidth)
    y = ra.randint(0, screenheight / 2)
    root.title("❤")
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    tk.Label(root, text='I LOVE YOU!', fg='white', bg='pink', font=("Comic Sans MS", 15), width=30, height=5).pack()
    root.mainloop()


def Love3():
    root = tk.Tk()
    width = 200
    height = 50
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    screenheight -= width
    x = ra.randint(screenwidth / 2, screenwidth)
    y = ra.randint(screenheight / 2, screenheight)
    root.title("❤")
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    tk.Label(root, text='I LOVE YOU!', fg='white', bg='pink', font=("Comic Sans MS", 15), width=30, height=5).pack()
    root.mainloop()


def Love4():
    root = tk.Tk()
    width = 200
    height = 50
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    screenheight -= 2 * width
    x = ra.randint(0, screenwidth / 2)
    y = ra.randint(screenheight / 2, screenheight)
    root.title("❤")
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    tk.Label(root, text='I LOVE YOU!', fg='white', bg='pink', font=("Comic Sans MS", 15), width=30, height=5).pack()
    root.mainloop()


def Heart():
    root = tk.Tk()
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    width = 600
    height = 400
    x = (screenwidth - width) // 2
    y = (screenheight - height) // 2
    root.title("❤")
    root.geometry("%dx%d+%d+%d" % (screenwidth, screenheight, 0, 0))
    tk.Label(root, text='❤', fg='pink', bg='white', font=("Comic Sans MS", 500), width=300, height=20).pack()
    root.mainloop()


Loves = []
t = td.Thread(target=Heart)
t.start()
for i in range(9):
    t1 = td.Thread(target=Love1)
    ti.sleep(0.1)
    t1.start()
    t2 = td.Thread(target=Love2)
    ti.sleep(0.1)
    t2.start()
    t3 = td.Thread(target=Love3)
    ti.sleep(0.1)
    t3.start()
    t4 = td.Thread(target=Love4)
    ti.sleep(0.1)
    t4.start()
