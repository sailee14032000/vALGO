import tkinter as tk
from tkinter import ttk
import webbrowser
class footerlabel(object):
    def __init__(self,parentframe):
        self.footerlabel = ttk.Label(parentframe, text="Made with ❤ by Sailee Salgaonkar",cursor="hand2",font=('Helvetica', 10))
        self.footerlabel.bind('<Button-1>',lambda e:webbrowser.open_new("https://www.linkedin.com/in/sailee-salgaonkar-1403/"))
        self.footerlabel.pack(fill=tk.Y, side=tk.BOTTOM,pady=5)

