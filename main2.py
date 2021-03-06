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
import bfspage
import dfspage
import mergesortpage
import quicksortpage
import aboutvalgopage
import os
class vALGO(object):
    def __init__(self):
        self.window = ThemedTk(theme="equilux", className="vALGO")
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.logo = PhotoImage(file="png\\logoc.png")
        self.window.iconphoto(False, self.logo)

        self.width = self.window.winfo_screenwidth() * 3 // 4
        self.height = self.window.winfo_screenheight() * 3 // 4

        #Pages

        self.queuepage = ttk.Frame(master=self.window)
        self.stackpage = ttk.Frame(master=self.window)
        self.linkedlistpage = ttk.Frame(master=self.window)
        self.binarysearchtreepage = ttk.Frame(master=self.window)
        self.bfspage = ttk.Frame(master=self.window)
        self.dfspage = ttk.Frame(master=self.window)
        self.bubblesortpage = ttk.Frame(master=self.window)
        self.insertionsortpage = ttk.Frame(master=self.window)
        self.mergesortpage = ttk.Frame(master=self.window)
        self.quicksortpage = ttk.Frame(master=self.window)
        self.aboutvalgopage = ttk.Frame(master=self.window)
        self.selectionsortpage = ttk.Frame(master=self.window)
        self.dashboardpage = ttk.Frame(master=self.window)

        self.pages = [self.selectionsortpage,self.mergesortpage,self.quicksortpage, self.insertionsortpage, self.bubblesortpage, self.dfspage, self.bfspage,
                      self.binarysearchtreepage, self.queuepage, self.stackpage, self.linkedlistpage,
                      self.dashboardpage,self.aboutvalgopage]

        for page in self.pages:
            page.grid(row=0, column=0, sticky='news')

        stackcontents = stackpage.stackpage_contents(self.dashboardpage, self.stackpage, self.width, self.height)
        llcontents = linkedlistpage.linkedlist_contents(self.dashboardpage, self.linkedlistpage, self.width,
                                                        self.height)
        queuecontents = queuepage.queue_contents(self.dashboardpage, self.queuepage, self.width,
                                                 self.height)

        # sorting
        bubblesortcontents = bubblesortpage.bubblesort_contents(self.dashboardpage, self.bubblesortpage, self.width,
                                                                self.height)
        insertionsortcontents = insertionsortpage.insertionsort_contents(self.dashboardpage, self.insertionsortpage,
                                                                         self.width,
                                                                         self.height)
        selectionsortcontents = selectionsortpage.selectionsort_contents(self.dashboardpage, self.selectionsortpage,
                                                                         self.width,
                                                                         self.height)
        mergesortcontents = mergesortpage.mergesort_contents(self.dashboardpage, self.mergesortpage,
                                                                         self.width,
                                                                         self.height)

        quicksortcontents = quicksortpage.quicksort_contents(self.dashboardpage, self.quicksortpage,
                                                             self.width,
                                                             self.height)

        # tree
        binarysearchtreecontents = binarysearchtreepage.binarysearchtree_contents(self.dashboardpage,
                                                                                  self.binarysearchtreepage, self.width,
                                                                                  self.height)

        # graph
        bfs = bfspage.bfs_contents(self.dashboardpage, self.bfspage, self.width, self.height)
        dfs = dfspage.dfs_contents(self.dashboardpage, self.dfspage, self.width, self.height)

        dfs = aboutvalgopage.aboutvalgo_contents(self.dashboardpage, self.aboutvalgopage, self.width, self.height)

    def dashboard_page(self, parentframe):

        heading = ttk.Frame(master=parentframe)

        canvas = tk.Canvas(master=heading, width=100, height=80, bg="#464646")
        self.mainimg = PhotoImage(file="png\\mimg4.png")
        canvas.create_image(50, 50, image=self.mainimg)

        canvas.config(highlightthickness=0)
        canvas.pack(side=tk.LEFT, anchor=tk.CENTER)

        title = ttk.Label(master=heading, text="vALGO", font=('Helvetica', 16))
        title.pack(side=tk.LEFT, anchor=tk.CENTER)

        heading.pack()

        contents = ttk.Frame(master=parentframe)

        algo = settings.algos(contents)
        algoimg = "png\\stack2.png"
        algo.addalgo("stack", self.width, self.height, algoimg, 0, 0, self.stackpage)

        algo = settings.algos(contents)
        algoimg = "png\\ll.png"
        algo.addalgo("Linkedlist", self.width, self.height, algoimg, 0, 1, self.linkedlistpage)

        algo = settings.algos(contents)
        algoimg = "png\\queue.png"
        algo.addalgo("Queue", self.width, self.height, algoimg, 0, 2, self.queuepage)

        algo = settings.algos(contents)
        algoimg = "png\\selectionsort.png"
        algo.addalgo("Selection sort", self.width, self.height, algoimg, 1, 0,
                     self.selectionsortpage)

        algo = settings.algos(contents)
        algoimg = "png\\bubblesort.png"

        algo.addalgo("Bubble sort", self.width, self.height, algoimg, 2, 1,
                     self.bubblesortpage)

        algo = settings.algos(contents)
        algoimg = "png\\insertionsort.png"
        algo.addalgo("Insertion sort", self.width, self.height, algoimg, 1, 2,
                     self.insertionsortpage)

        algo = settings.algos(contents)
        algoimg = "png\\binarytree.png"
        algo.addalgo("Binary Search Tree", self.width, self.height, algoimg, 2, 0, self.binarysearchtreepage)

        algo = settings.algos(contents)
        algoimg = "png\\bfs.png"
        algo.addalgo("BFS", self.width, self.height, algoimg, 1, 1, self.bfspage)

        algo = settings.algos(contents)
        algoimg = "png\\dfs.png"
        algo.addalgo("DFS", self.width, self.height, algoimg, 2, 2, self.dfspage)

        algo = settings.algos(contents)
        algoimg = "png\\mergesort.png"
        algo.addalgo("Mergesort", self.width, self.height, algoimg, 0, 3, self.mergesortpage)

        algo = settings.algos(contents)
        algoimg = "png\\quicksort.png"
        algo.addalgo("Quicksort", self.width, self.height, algoimg, 1, 3, self.quicksortpage)

        algo = settings.algos(contents)
        algoimg = "png\\info.png"
        algo.addalgo("About valgo", self.width, self.height, algoimg, 2, 3, self.aboutvalgopage)


        contents.pack()
        self.end = footer.footerlabel(parentframe)

    def start(self):
        self.window.mainloop()




if __name__ == "__main__":
    valgo = vALGO()
    valgo.dashboard_page(valgo.dashboardpage)
    valgo.start()
