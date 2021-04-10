import tkinter as tk
from tkinter.messagebox import showwarning
import subprocess

root = tk.Tk()
root.geometry("600x500")

label = tk.Label(root, text="Example of xterm embedded in frame")
label.pack(fill=tk.X)

xterm_frame = tk.Frame(root)
xterm_frame.pack(fill=tk.BOTH, expand=True)

xterm_frame_id = xterm_frame.winfo_id()

try:
    p = subprocess.Popen(
        ["xterm", "-into", str(xterm_frame_id), "-geometry", "80x20"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
except FileNotFoundError:
    showwarning("Error", "xterm is not installed")
    raise SystemExit

root.mainloop()
