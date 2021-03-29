import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import footer
class stackpage_contents(object):
    def __init__(self,ancestorpage,parentframe,width,height):
        self.back = ttk.Button(master=parentframe, text="← Back", command=lambda: self.raise_frame(ancestorpage))
        self.back.pack(anchor="w", padx=40, pady=20)

        self.stacklist = []
        self.stack_lr = []
        self.stack_lrt = []
        self.x = 20
        self.y = 40


        self.heading = ttk.Label(master=parentframe, text="Stack", font=('Helvetica', 14))
        self.heading.pack(fill=tk.X, padx=40, pady=10)

        self.definition = ttk.Label(master=parentframe, wraplength=width - 10, font=('Helvetica', 12), justify='left',
                               text="A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.")
        self.definition.pack(fill=tk.X, padx=40, pady=10)

        self.set_of_operations = tk.Frame(master=parentframe, padx=40, bg="#464646")

        self.node = ttk.Entry(master=self.set_of_operations)
        self.node.insert(0, "Enter node value")


        self.output_frame = ttk.Frame(master=parentframe)

        self.output = tk.Canvas(master=self.output_frame, bg="#464646", bd=1, highlightthickness=1, highlightbackground="#d8d8d8",
                           relief=tk.FLAT, scrollregion=(0, 0, 100, 100))

        self.push_b = ttk.Button(master=self.set_of_operations, text="PUSH", command=lambda: self.push(self.output))
        self.pop_b = ttk.Button(master=self.set_of_operations, text="POP", command=lambda: self.pop(self.output))
        self.top_b = ttk.Button(master=self.set_of_operations, text="PEEK", command=lambda: self.top(self.output))
        self.size_b = ttk.Button(master=self.set_of_operations, text="SIZE", command=lambda: self.size_(self.output))

        self.node.pack(side=tk.LEFT, ipady=4, ipadx=4)
        self.push_b.pack(side=tk.LEFT, padx=2)
        self.pop_b.pack(side=tk.LEFT, padx=2)
        self.top_b.pack(side=tk.LEFT, padx=2)
        self.size_b.pack(side=tk.LEFT, padx=2)

        self.set_of_operations.pack(fill=tk.X)

        self.horscroll = tk.Scrollbar(master=self.output_frame, orient=tk.HORIZONTAL)
        self.horscroll.configure(command=self.output.xview)
        self.horscroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.output.configure(xscrollcommand=self.horscroll.set)

        self.output.pack(fill=tk.BOTH, expand=1)
        self.output_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=1)
        self.end = footer.footerlabel(parentframe)
    def raise_frame(self,ancestorpage):
        ancestorpage.tkraise()


    def push(self,output):
        input = self.node.get()
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input",message="Please enter input")
            return
        self.stacklist.append(input)
        curr_rect = output.create_rectangle(self.x,self.y,self.x+40,self.y+40,fill='#3779D2')
        self.stack_lr.append(curr_rect)

        curr_text = output.create_text(self.x + 20, self.y + 20,text=self.stacklist[-1],fill="#d8d8d8")
        self.stack_lrt.append(curr_text)
        self.x += 40
        sr = list(map(int, output.cget('scrollregion').split()))
        output['scrollregion'] = (sr[0], sr[1], sr[2] + 40, sr[3])
        output.xview_moveto((self.x+40)/(sr[2]+40))

        output.update()
        time.sleep(0.2)
        output.itemconfig(curr_rect,fill="")

        output.update()

    def pop(self,output):

        if len(self.stacklist)==0:
            msg.showwarning(title="Empty stack",message="Stack is empty")
            return
        todelr = self.stack_lr.pop()
        todelrt = self.stack_lrt.pop()
        output.move(todelr,40,self.y + 20)
        output.move(todelrt,40, self.y + 20)

        arrow = output.create_line(self.x-40,self.y+20, output.coords(todelr)[0],output.coords(todelr)[1], arrow=tk.LAST, capstyle=tk.BUTT, fill='black')
        output.itemconfig(todelr,fill="#DC143C")
        output.update()

        time.sleep(0.09)
        output.itemconfig(todelr, fill="#800000")
        output.update()

        time.sleep(0.1)
        output.itemconfig(todelr,fill="#DC143C")
        output.update()

        time.sleep(0.09)

        output.delete(arrow)
        output.delete(todelr)
        output.delete(todelrt)
        self.stacklist.pop()

        self.x -= 40



    def top(self,output):
        if len(self.stacklist) == 0:
            msg.showwarning(title="Empty List", message="List is empty")
            return
        top = "Top element is " + str(self.stacklist[-1])
        msg.showinfo(title="Top", message=top)

    def size_(self,output):
        length = "Length is {}".format(len(self.stacklist))
        msg.showinfo(title="Length", message=length)



