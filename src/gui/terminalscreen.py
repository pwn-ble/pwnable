import tkinter as tk
from tkinter.messagebox import showwarning
import subprocess

def open_terminal_win():
    popen = subprocess.Popen(["xterm"], stdout=subprocess.PIPE)
    
    for stdout_line in iter(popen.stdout.readline, ""):
        print(stdout_line)
        
    # popen.stdout.close()
    return_code = popen.wait()

    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

open_terminal_win()

# root = tk.Tk()
# root.geometry("600x500")

# label = tk.Label(root, text="Example of xterm embedded in frame")
# label.pack(fill=tk.X)

# xterm_frame = tk.Frame(root)
# xterm_frame.pack(fill=tk.BOTH, expand=True)

# xterm_frame_id = xterm_frame.winfo_id()

# except FileNotFoundError:
#     showwarning("Error", "xterm is not installed")
#     raise SystemExit

# root.mainloop()
