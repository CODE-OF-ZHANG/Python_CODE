import tkinter as tk
import random


def spin_chamber():
    return random.random() <= 0.25


def fire_gun():
    global bullet_prob
    if bullet_prob < 1.0:
        bullet_prob += 1 / 6
    if spin_chamber():
        result_label.config(text="儿子真乖！")
    else:
        result_label.config(text="不叫？再给你一次机会！")


root = tk.Tk()
root.title("叫你一声儿子你敢答应吗？")
root.geometry('400x300')

label = tk.Label(root, text="叫爸爸！！！", font=('华文宋体', 20))
label.pack(padx=50, pady=30)

result_label = tk.Label(root, text="")
result_label.place(x=110, y=100)

call_button = tk.Button(root, text="叫", command=fire_gun, font=('华文宋体', 30))
call_button.place(x=80, y=120)

no_call_button = tk.Button(root, text="不叫？", command=fire_gun, font=('华文宋体', 30))
no_call_button.place(x=180, y=120)

bullet_prob = 1 / 6
root.mainloop()
