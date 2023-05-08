################## Imports ##################
from pynput import keyboard
import win32clipboard
import time

################## Configuration Variables ##################

# get original clipboard on app open
win32clipboard.OpenClipboard()
clipboard = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

# Add new text to front or back, 1 = front, 0 = end
order = 0

# the hotkey to do the fanc add copy
copy_command = "<ctrl>+c"
clear_command = "<ctrl>+m"

# This is the phrase that will seperate all the copies, feel free to leave it blank
seperator = " !!! "

################## Change the clipboard ##################
def update_clipboard():
    
    # kinda slopy solution to the fact that sometimes this program runs faster than the computers copy function
    time.sleep(0.1)
    
    # make that puppy global cause otherwise stuff don't work
    global clipboard
    
    # Get the new clipboard
    win32clipboard.OpenClipboard()
    temp_clipboard = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    
    # Add it to the old clipboard with the seperator
    if order == 0:
        combined = clipboard + seperator + temp_clipboard
    elif order == 1:
        combined = temp_clipboard + seperator + clipboard
        
    # Change the clipboard and make the old clipboard the new one
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(combined)
    win32clipboard.CloseClipboard()
    clipboard = combined

# clear the clipboard
def clear_clipboard():
    global clipboard
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()
    clipboard = None
    
################## Detecting Hotkey ##################
listener = keyboard.GlobalHotKeys({copy_command: update_clipboard, clear_command: clear_clipboard})
listener.start()
listener.join()
