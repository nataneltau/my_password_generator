import tkinter as tk

#Should call start() first to initialize this variable
root = None

def quit():
    """Closes the GUI."""
    root.destroy()

def start():
    root = tk.Tk()
    root.title("Passwords Generator")
    #root.geometry("300x300")


def __create_entry(entry_title: str) -> tk.Entry:
    label = tk.Label(root, text = entry_title)
    
#watch: https://www.youtube.com/watch?v=ibf5cx221hk