import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("tk")

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)            
tabControl.add(tab1, text = '고양이')    
tab2 = ttk.Frame(tabControl)            
tabControl.add(tab2, text = '강아지')     

tabControl.pack(expand = 1, fill = "both") 


win.mainloop()
