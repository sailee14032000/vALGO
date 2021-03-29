import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import footer

class bubblesort_contents(object):

    def __init__(self,ancestorpage,parentframe,width,height):
        self.back = ttk.Button(master=parentframe, text="← Back", command=lambda: self.raise_frame(ancestorpage))
        self.back.pack(anchor="w", padx=40, pady=20)

        self.x = 20
        self.y = 0

        self.heading = ttk.Label(master=parentframe, text="Bubble Sort", font=('Helvetica', 14))
        self.heading.pack(fill=tk.X, padx=40, pady=10)

        self.definition = ttk.Label(master=parentframe, wraplength=width - 10, font=('Helvetica', 12), justify='left',
                                    text="Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.")
        self.definition.pack(fill=tk.X, padx=40, pady=10)

        self.set_of_operations = tk.Frame(master=parentframe, padx=40, bg="#464646")

        self.node = ttk.Entry(master=self.set_of_operations,width=50)
        self.node.insert(0, "29,4,150,34,90,12,36,87,45")
        self.output_frame = ttk.Frame(master=parentframe)

        self.output = tk.Canvas(master=self.output_frame, bg="#464646", bd=1, highlightthickness=1, highlightbackground="#d8d8d8",
                           relief=tk.FLAT, scrollregion=(0, 0, 100, 100))

        self.sort = ttk.Button(master=self.set_of_operations, text="SORT", command=lambda: self.sort_(self.output))
        self.node.pack(side=tk.LEFT, ipady=4, ipadx=4)
        self.sort.pack(side=tk.LEFT, padx=2)
        self.set_of_operations.pack(fill=tk.X)

        self.horscroll = tk.Scrollbar(master=self.output_frame, orient=tk.HORIZONTAL)
        self.horscroll.configure(command=self.output.xview)
        self.horscroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.verscroll = tk.Scrollbar(master=self.output_frame,orient=tk.VERTICAL)
        self.verscroll.configure(command=self.output.yview)
        self.verscroll.pack(side=tk.RIGHT,fill=tk.Y)

        self.output.configure(xscrollcommand=self.horscroll.set,yscrollcommand=self.verscroll.set)

        self.output.pack(fill=tk.BOTH, expand=1)
        self.output_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=1)
        self.end = footer.footerlabel(parentframe)
    def sort_(self,output):
        self.rectangles = []

        self.x = 40
        output.delete(tk.ALL)
        input = self.node.get()
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return
        numbers = list(map(int,input.strip().split(',')))
        max_ = max(numbers)
        self.y = max_ + 40
        for i in numbers:
            rect = output.create_rectangle(self.x,self.y,self.x+40,self.y-i)
            text = output.create_text(self.x+20,self.y+10,text=str(i))
            self.x +=50
            self.rectangles.append([rect,text])
        time.sleep(0.3)
        n = len(numbers)

        sr = list(map(int, output.cget('scrollregion').split()))
        if max_+120>int(output['height']):
            sr[3] = max_ + 120
        output['scrollregion'] = (sr[0],sr[1],sr[0]+ n*(50)+50,sr[3])
        output.yview_moveto(1)
        output.update()
        sr = list(map(int, output.cget('scrollregion').split()))


        for i in range(n):
            output.xview_moveto(0)
            output.update()

            for j in range(n-i-1):
                output.itemconfig(self.rectangles[j][0], fill="#736AFF")
                output.itemconfig(self.rectangles[j][1], fill="#736AFF")
                output.itemconfig(self.rectangles[j + 1][0], fill="#736AFF")
                output.itemconfig(self.rectangles[j + 1][1], fill="#736AFF")
                output.update()
                time.sleep(0.3)

                if numbers[j]>numbers[j+1]:
                    output.itemconfig(self.rectangles[j][0],fill="#3779D2")
                    output.itemconfig(self.rectangles[j][1],fill="#3779D2")
                    output.itemconfig(self.rectangles[j+1][0],fill="#3779D2")
                    output.itemconfig(self.rectangles[j+1][1],fill="#3779D2")

                    output.move(self.rectangles[j][0],50,0)
                    output.move(self.rectangles[j][1], 50, 0)

                    output.move(self.rectangles[j+1][0], -50, 0)
                    output.move(self.rectangles[j+1][1], -50, 0)
                    output.update()
                    time.sleep(0.6)


                    numbers[j] ,numbers[j+1] = numbers[j+1],numbers[j]
                    self.rectangles[j],self.rectangles[j+1] = self.rectangles[j+1],self.rectangles[j]
                output.itemconfig(self.rectangles[j][0], fill="")
                output.itemconfig(self.rectangles[j][1], fill="#d8d8d8")
                output.itemconfig(self.rectangles[j + 1][0], fill="")
                output.itemconfig(self.rectangles[j + 1][1], fill="#d8d8d8")

                x,y,x1,y1 = output.coords(self.rectangles[j][0])
                if x/sr[2]>0.4:
                    output.xview_moveto(x/sr[2])
                output.update()

            output.itemconfig(self.rectangles[n-i-1][0],fill="#3CBC3C")
            output.itemconfig(self.rectangles[n - i - 1][1], fill="#3CBC3C")
            output.update()

    def raise_frame(self,ancestorpage):
        ancestorpage.tkraise()
