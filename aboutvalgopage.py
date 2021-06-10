import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import footer
from tkinter import PhotoImage
import webbrowser

class aboutvalgo_contents(object):
    def __init__(self,ancestorpage,parentframe,width,height):
        self.back = ttk.Button(master=parentframe, text="← Back", command=lambda: self.raise_frame(ancestorpage))
        self.back.pack(anchor="w", padx=40, pady=20)

        self.heading = ttk.Frame(master=parentframe)

        self.canvas = tk.Canvas(master=self.heading, width=100, height=80, bg="#464646")
        self.mainimg = PhotoImage(file="png\\mimg4.png")
        self.canvas.create_image(50, 50, image=self.mainimg)

        self.canvas.config(highlightthickness=0)
        self.canvas.grid(row=0,column=1,padx=(40,0))



        self.title = ttk.Label(master=self.heading, text="vALGO", font=('Helvetica', 16))
        self.title.grid(row=0,column=2)
        self.heading.pack(anchor="c", padx=40)

        self.content = ttk.Label(master=parentframe)

        self.image = PhotoImage(file="png\\sailee.png")

        self.sailee = tk.Label(master=self.content, image=self.image, bg="#464646")
        self.sailee.image = self.image
        self.sailee.pack(side=tk.LEFT, padx=(40,0))

        self.definition = ttk.Label(master=self.content, wraplength=width - 10, font=('Helvetica', 12), justify='left',
                                    text="Hey! Sailee Salgonkar here. This gui helps to visualise of various data structures. It also includes audio explanation to help you understand it in better format")
        self.definition.pack(side=tk.LEFT,anchor="c", padx=(0,40), pady=(40,0))
        self.content.pack(anchor="c")

        self.aboutimg = PhotoImage(file="png\\about.png")

        self.details_dscontents = ttk.Frame(master=parentframe)
        self.details = tk.Label(master=self.details_dscontents, image=self.aboutimg, bg="#464646")
        self.details.image = self.aboutimg
        self.details.pack(side=tk.LEFT,anchor="c",padx=(80,0))

        self.dscontents = ttk.Label(master=self.details_dscontents, font=('Helvetica', 12),text="Data Structures:\n> Stack\n> LinkedList\n> Queue\n> Mergesort\n> Selectionsort\n> Insertionsort\n> BFS\n> DFS\n> Binary search tree")
        self.dscontents.pack(anchor="c",padx=80)


        self.details_dscontents.pack(anchor="n")



        self.end = footer.footerlabel(parentframe)

    def raise_frame(self,ancestorpage):
        ancestorpage.tkraise()



