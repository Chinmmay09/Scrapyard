import tkinter as tk
import time 
import psutil

def detection():
    while True:
        running = "Code.exe" in [p.name() for p in psutil.process_iter()]
        
        return running
print(detection())

root = tk.Tk()
root.overrideredirect(True) 
root.geometry("400x300")  


srs_cat = tk.PhotoImage(file='srs_cat.png')

srs_cat_label = tk.Label(root,image=srs_cat)
srs_cat_label.pack()





root.mainloop()
