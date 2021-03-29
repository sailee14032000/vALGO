import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from ttkthemes import ThemedTk
import settings
import stackpage
import linkedlistpage
import queuepage
import binarysearchtreepage
import bubblesortpage
import insertionsortpage
import selectionsortpage
import footer


class vALGO(object):
    def __init__(self):
        self.window = ThemedTk(theme="equilux",className="vALGO")
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0, weight=1)
        self.logo = PhotoImage(file="D:/python projects/logos/png/logoc.png")
        self.window.iconphoto(False, self.logo)

        self.width = self.window.winfo_screenwidth() * 3 // 4
        self.height = self.window.winfo_screenheight() * 3 // 4

        #Pages

        self.queuepage = ttk.Frame(master=self.window)
        self.stackpage = ttk.Frame(master=self.window)
        self.linkedlistpage = ttk.Frame(master=self.window)
        self.binarysearchtreepage = ttk.Frame(master=self.window)
        self.bubblesortpage = ttk.Frame(master=self.window)
        self.insertionsortpage = ttk.Frame(master=self.window)
        self.selectionsortpage = ttk.Frame(master=self.window)
        self.dashboardpage = ttk.Frame(master=self.window)

        self.pages = [self.selectionsortpage,self.insertionsortpage,self.bubblesortpage,self.binarysearchtreepage,self.queuepage,self.stackpage,self.linkedlistpage,self.dashboardpage]
        for page in self.pages:
            page.grid(row=0,column=0,sticky='news')

        stackcontents = stackpage.stackpage_contents(self.dashboardpage,self.stackpage,self.width,self.height)
        llcontents = linkedlistpage.linkedlist_contents(self.dashboardpage, self.linkedlistpage, self.width, self.height)
        queuecontents = queuepage.queue_contents(self.dashboardpage, self.queuepage, self.width,
                                                        self.height)

        #sorting
        bubblesortcontents = bubblesortpage.bubblesort_contents(self.dashboardpage, self.bubblesortpage, self.width,
                                                        self.height)
        insertionsortcontents = insertionsortpage.insertionsort_contents(self.dashboardpage, self.insertionsortpage, self.width,
                                                        self.height)
        selectionsortcontents = selectionsortpage.selectionsort_contents(self.dashboardpage, self.selectionsortpage,
                                                                         self.width,
                                                                         self.height)

        #tree
        binarysearchtreecontents = binarysearchtreepage.binarysearchtree_contents(self.dashboardpage, self.binarysearchtreepage, self.width,
                                                                                    self.height)


    def dashboard_page(self,parentframe):

        heading = ttk.Frame(master=parentframe)

        canvas = tk.Canvas(master=heading, width=100, height=100, bg="#464646")
        self.mainimg = PhotoImage(file="D:/python projects/logos/png/mimg4.png")
        canvas.create_image(50, 50, image=self.mainimg)

        canvas.config(highlightthickness=0)
        canvas.pack(side=tk.LEFT, anchor=tk.CENTER)

        title = ttk.Label(master=heading, text="vALGO", font=('Helvetica', 16))
        title.pack(side=tk.LEFT, anchor=tk.CENTER)

        heading.pack()

        contents = ttk.Frame(master=parentframe)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/stack2.png"
        algo.addalgo("stack",self.width, self.height, algoimg, 0, 0, self.stackpage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/ll.png"
        algo.addalgo("Linkedlist", self.width, self.height, algoimg, 0, 1, self.linkedlistpage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/ptree.png"
        algo.addalgo("Queue", self.width, self.height, algoimg, 0, 2, self.queuepage)


        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/ptree.png"
        algo.addalgo("Selection sort", self.width, self.height, algoimg, 1, 0,
                                  self.selectionsortpage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/bubblesort.png"

        algo.addalgo("Bubble sort", self.width, self.height, algoimg, 1,1,
                                  self.bubblesortpage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/insertionsort.png"
        algo.addalgo("Insertion sort", self.width, self.height, algoimg, 1, 2,
                                        self.insertionsortpage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/binarytree.png"
        algo.addalgo("Binary Search Tree", self.width, self.height, algoimg, 2, 0, self.binarysearchtreepage)


        contents.pack()
        self.end = footer.footerlabel(parentframe)
    def start(self):
        self.window.mainloop()
if __name__=="__main__":
    valgo = vALGO()
    valgo.dashboard_page(valgo.dashboardpage)
    valgo.start()
