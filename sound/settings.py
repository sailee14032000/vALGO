import tkinter as tk
from tkinter import ttk

class algos(object):
    def __init__(self, ances):
        self.parentframe = ances
        self.pgid = 0

    def raise_frame(self):
        self.openframe.tkraise()
    def addalgo(self, name, w, h, img, row, col, openframe):
        self.openframe = openframe
        style_b = ttk.Style()
        style_b.configure('my.TButton', font=('Helvetica', 12))
        fr = ttk.Button(master=self.parentframe,text=name.title(),
                       command= self.raise_frame,compound="top",style="my.TButton")
        fr.image = tk.PhotoImage(file=img)
        fr['image'] = fr.image
        fr.grid(row=row, column=col, sticky="news", pady=5,padx=10)







