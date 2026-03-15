import tkinter as tk

count = 5

def update_count():
    global count
    label.config(text=str(count))
    
    if count > 0:
        count -= 1
        root.after(1000, update_count)
    else:
        root.after(1000, root.destroy)

root = tk.Tk()
root.title("System Process")

# Fullscreen dark window
root.attributes("-fullscreen", True)
root.configure(bg="black")

frame = tk.Frame(root, bg="black")
frame.pack(expand=True)

title = tk.Label(
    frame,
    text="System integrity check in progress...",
    font=("Consolas", 28),
    fg="#00ff9c",
    bg="black"
)
title.pack(pady=40)

label = tk.Label(
    frame,
    text="5",
    font=("Consolas", 200, "bold"),
    fg="#ff3b3b",
    bg="black"
)
label.pack()

sub = tk.Label(
    frame,
    text="Please do not interrupt this process",
    font=("Consolas", 18),
    fg="white",
    bg="black"
)
sub.pack(pady=40)

root.after(1000, update_count)

root.mainloop()
