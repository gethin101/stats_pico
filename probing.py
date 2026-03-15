import tkinter as tk
import random

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.title("System")

text = tk.Text(
    root,
    bg="black",
    fg="#00ff9c",
    insertbackground="#00ff9c",
    font=("Consolas", 20),
    bd=0,
)
text.pack(expand=True, fill="both")

lines = [
    "Initializing system scan...",
    "Loading network interfaces...",
    "Checking host configuration...",
    "Scanning local network...",
    "Enumerating active devices...",
]

# generate some fake IP scan lines
for i in range(5):
    lines.append(f"Probing 192.168.0.{random.randint(2,254)} ... OK")

lines += [
    "Collecting system data...",
    "Accessing kernel services...",
    "Establishing secure channel...",
    "Preparing final sequence..."
]

def type_line(line_index=0, char_index=0):
    if line_index >= len(lines):
        root.after(800, start_countdown)
        return

    line = lines[line_index]

    if char_index < len(line):
        text.insert("end", line[char_index])
        text.see("end")
        root.after(20, type_line, line_index, char_index + 1)
    else:
        text.insert("end", "\n")
        root.after(200, type_line, line_index + 1, 0)

count = 5

def start_countdown():
    global count
    text.insert("end", "\n\nFINALIZING...\n")
    text.insert("end", f"\n{count}")
    text.tag_add("big", "end-2c", "end")
    text.tag_config("big", font=("Consolas", 120, "bold"), foreground="#ff3b3b")
    root.after(1000, update_count)

def update_count():
    global count
    count -= 1
    if count >= 0:
        text.insert("end", f"\n{count}")
        text.tag_add("big", "end-2c", "end")
        text.tag_config("big", font=("Consolas", 120, "bold"), foreground="#ff3b3b")
        root.after(1000, update_count)
    else:
        root.after(1000, root.destroy)

root.after(500, type_line)
root.mainloop()
