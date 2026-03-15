import tkinter as tk

count = 5

def countdown():
    global count
    if count > 0:
        label.config(text=str(count))
        count -= 1
        root.after(1000, countdown)
    else:
        label.config(text="1")

root = tk.Tk()
root.title("Countdown")

# Make window large
root.attributes("-fullscreen", True)

label = tk.Label(root, text="5", font=("Arial", 120))
label.pack(expand=True)

root.after(1000, countdown)

root.mainloop()
