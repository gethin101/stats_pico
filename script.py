import tkinter as tk
import random

root = tk.Tk()
root.title("Terminal")
root.attributes("-fullscreen", True)
root.configure(bg="black")

text = tk.Text(
    root,
    bg="black",
    fg="#00ff00",
    insertbackground="#00ff00",
    font=("Consolas", 18),
    bd=0
)
text.pack(expand=True, fill="both")

commands = [
    "scan --network",
    "enumerate --devices",
    "probe --gateway",
    "inject --payload",
    "crack --auth"
]

passwords = [
    "admin123",
    "password",
    "letmein",
    "123456",
    "root",
    "guest",
]

def type_text(string, i=0, callback=None):
    if i < len(string):
        text.insert("end", string[i])
        text.see("end")
        root.after(random.randint(15,40), type_text, string, i+1, callback)
    else:
        text.insert("end", "\n")
        if callback:
            root.after(200, callback)

def progress_bar(label, percent=0, callback=None):
    if percent <= 100:
        bar = "#" * (percent // 4)
        text.insert("end", f"\r{label} [{bar:<25}] {percent}%")
        text.see("end")
        root.update()
        root.after(40, progress_bar, label, percent+2, callback)
    else:
        text.insert("end", "\n")
        if callback:
            root.after(300, callback)

def password_crack(attempt=0):
    if attempt < 8:
        pw = random.choice(passwords) + str(random.randint(0,99))
        text.insert("end", f"Trying password: {pw}\n")
        text.see("end")
        root.after(200, password_crack, attempt+1)
    else:
        text.insert("end", "\nACCESS GRANTED\n")
        text.tag_add("access", "end-2l", "end-1l")
        text.tag_config("access", foreground="#00ff9c", font=("Consolas",22,"bold"))
        root.after(1000, start_countdown)

count = 5

def start_countdown():
    text.insert("end", "\nFinalizing operation...\n\n")
    update_count()

def update_count():
    global count
    text.insert("end", f"{count}\n")
    text.tag_add("big", "end-2l", "end-1l")
    text.tag_config("big", font=("Consolas",100,"bold"), foreground="#ff3b3b")
    text.see("end")

    if count > 0:
        count -= 1
        root.after(1000, update_count)
    else:
        root.after(1000, root.destroy)

def start_sequence():

    def step5():
        password_crack()

    def step4():
        progress_bar("Injecting payload", callback=step5)

    def step3():
        progress_bar("Probing gateway", callback=step4)

    def step2():
        progress_bar("Enumerating devices", callback=step3)

    def step1():
        progress_bar("Scanning network", callback=step2)

    type_text(f"> {random.choice(commands)}", callback=step1)

root.after(500, start_sequence)

root.mainloop()
