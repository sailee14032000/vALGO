import time
import tkinter as tk
from tkinter.font import Font 
from tkinter import PhotoImage
from tkinter import ttk  
from ttkthemes import ThemedTk
import settings
import tkinter.messagebox as msg
def raise_frame(frame):
    frame.tkraise()


window = ThemedTk(theme="equilux",className="vALGO")
width = window.winfo_screenwidth()*3//4
height = window.winfo_screenheight()*3//4
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

#font



#pages

queuepage = ttk.Frame(master=window)
stackpage = ttk.Frame(master=window)
linkedlistpage = ttk.Frame(master=window)
mainpage = ttk.Frame(master=window)


for frame in (queuepage,linkedlistpage,stackpage,mainpage):
    frame.grid(row=0, column=0, sticky='news')

#queue
class queueclass(object):
    def __init__(self):
        self.queue_l = []
        self.queue_canvas = []
        self.x = 20
        self.y = 40
    def enqueue(self,output):
        input = node_q.get()
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return
        self.queue_l.append(input)
        curr_rect = output.create_rectangle(self.x, self.y, self.x + 40, self.y + 40)
        curr_text = output.create_text(self.x + 20, self.y + 20, text=input, fill="#d8d8d8")
        arrow = output.create_line(self.x+40,self.y+20,self.x+60,self.y+20,
                                      arrow=tk.LAST, capstyle=tk.BUTT, fill='black')
        self.queue_canvas.append([curr_rect,curr_text,arrow])

        self.x += 60

        sr = list(map(int, output.cget('scrollregion').split()))
        output['scrollregion'] = (sr[0], sr[1], sr[2] + 60, sr[3])
        output.xview_moveto((self.x + 60) / (sr[2] + 60))
        output.update()
    def dequeue(self,output):
        self.queue_l.pop(0)
        output.move(self.queue_canvas[0][0],0,40)
        output.move(self.queue_canvas[0][1],0,40)
        output.move(self.queue_canvas[0][2],0,40)
        output.update()
        time.sleep(0.3)
        output.delete(*self.queue_canvas[0])
        output.move(tk.ALL,-60,0)
        self.x -=60
        self.queue_canvas.pop(0)
    def peek(self,output):
        msg.showinfo(title="Top element",message="Top element is  "+self.queue_l[-1])

    def size_(self, output):
        msg.showinfo(title="Top element", message="Size of list is %d"%(len(self.queue_l)))


back = ttk.Button(master=queuepage,text="← Back",command=lambda:raise_frame(mainpage))
back.pack(anchor="w",padx=40,pady=20)
heading = ttk.Label(master=queuepage, text="Queue",font=('Helvetica',14))
heading.pack(fill=tk.X,padx=40,pady=10)

definition = ttk.Label(master=queuepage,wraplength=width-10,font=('Helvetica', 12),justify='left',text="")
definition.pack(fill=tk.X,padx=40,pady=10)

set_of_operations = tk.Frame(master=queuepage,padx=40,bg="#464646")

node_q= ttk.Entry(master=set_of_operations)
node_q.insert(0,"Enter node value")

queue = queueclass()

output_frame = ttk.Frame(master=queuepage)

outputq = tk.Canvas(master=output_frame,bg="#464646",bd=1, highlightthickness=1,  highlightbackground="#d8d8d8",relief=tk.FLAT,scrollregion=(0,0,100,100))

enqueue_b = ttk.Button(master=set_of_operations,text="ENQUEUE",command = lambda:queue.enqueue(outputq))
dequeue_b = ttk.Button(master=set_of_operations,text="DEQUEUE",command = lambda:queue.dequeue(outputq))

top_b = ttk.Button(master=set_of_operations,text="PEEK",command = lambda:queue.peek(outputq))
size_b = ttk.Button(master=set_of_operations,text="SIZE",command = lambda:queue.size_(outputq))

node_q.pack(side=tk.LEFT,ipady=4,ipadx=4)
enqueue_b.pack(side=tk.LEFT,padx=2)
dequeue_b.pack(side=tk.LEFT,padx=2)
top_b.pack(side=tk.LEFT,padx=2)
size_b.pack(side=tk.LEFT,padx=2)


set_of_operations.pack(fill=tk.X)


horscroll = tk.Scrollbar(master=output_frame,orient=tk.HORIZONTAL)
horscroll.configure(command=outputq.xview)
horscroll.pack(side=tk.BOTTOM,fill=tk.X)

outputq.configure(xscrollcommand=horscroll.set)

outputq.pack(fill=tk.BOTH,expand=1)
output_frame.pack(pady=20,padx=40,fill=tk.BOTH,expand=1)

#queuepage ends



#linkedlist
class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
class linkedlistclass(object):
    def __init__(self):
        self.head = None
        self.x = 20
        self.y = 40
        self.allnodes = []

    def add_lb(self,output_ll):
        input = nodell.get()
        new_node = Node(input)
        new_node.next = self.head
        self.head = new_node

        #canvas part
        output_ll.move(tk.ALL,62,0)
        ll_rect = output_ll.create_rectangle(20,40,60,80)
        ll_rectnext  = output_ll.create_rectangle(60,40,65,80)
        ll_text = output_ll.create_text(40, 60,text=input,fill="#d8d8d8")
        arrow = output_ll.create_line(62.5,60,80.5,60,
                                   arrow=tk.LAST, capstyle=tk.BUTT, fill='black')
        sr = list(map(int,output_ll['scrollregion'].split()))
        output_ll['scrollregion'] = (sr[0], sr[1], sr[2] + 65, sr[3])
        #output_ll.xview_moveto((self.x + 45) / (sr[2] + 45))
        output_ll.xview_moveto(0)

        output_ll.update()
        self.x += 62
        self.allnodes.insert(0,[ll_rect,ll_rectnext,ll_text,arrow])
    def append_lb(self,output_ll):
        input = nodell.get()
        temp = self.head
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return

        if not self.head:
            return self.add_lb(output_ll)
        else:
            while temp:
                prev = temp
                temp = temp.next
            new_node = Node(input)
            prev.next = new_node

        #canvas
        ll_rect = output_ll.create_rectangle(self.x, self.y, self.x + 40, self.y + 40)

        ll_text = output_ll.create_text(self.x + 20, self.y + 20, text=input, fill="#d8d8d8")
        ll_rectnext = output_ll.create_rectangle(self.x+40, 40, self.x + 45, 80)

        arrow = output_ll.create_line(self.x+42.5,self.y+20,self.x+60.5,self.y+20,
                                      arrow=tk.LAST, capstyle=tk.BUTT, fill='black')
        sr = list(map(int, output_ll['scrollregion'].split()))
        output_ll['scrollregion'] = (sr[0], sr[1], sr[2] + 65, sr[3])
        output_ll.xview_moveto((self.x + 45) / (sr[2] + 45))
        self.allnodes.append([ll_rect, ll_rectnext, ll_text, arrow])
        output_ll.update()
        self.x += 62

        window.update()
    def remove_lb(self,output_ll):
        input = nodell.get()
        temp = self.head
        found = False
        i = 0
        while temp:
            if temp.val == input:
                found = True
                break
            else:
                prev = temp
                temp = temp.next
                i+=1
        #print(found,input,i,self.allnodes)
        if not found:
            msg.showwarning(title="Error",message="Element not found")
            return
        if found:
            if i==0:
                self.head = temp.next
            else:
                prev.next = temp.next
            #canvas
            x,y,x1,y1 = output_ll.coords(self.allnodes[i][0])
            sr = list(map(int, output_ll['scrollregion'].split()))
            output_ll.xview_moveto((x - 45) / (sr[2] + 45))

            output_ll.move(self.allnodes[i][0],0,60)
            output_ll.move(self.allnodes[i][1],0,60)
            output_ll.move(self.allnodes[i][2],0,60)
            output_ll.move(self.allnodes[i][3],0,60)
            output_ll.update()
            time.sleep(0.3)
            output_ll.delete(self.allnodes[i][1],self.allnodes[i][0],self.allnodes[i][3],self.allnodes[i][2])
            for j in range(i+1,len(self.allnodes)):
                output_ll.move(self.allnodes[j][0], -62,0)
                output_ll.move(self.allnodes[j][1], -62,0)
                output_ll.move(self.allnodes[j][2], -62,0)
                output_ll.move(self.allnodes[j][3], -62,0)
                output_ll.update()
            self.x -= 62

            self.allnodes.pop(i)

    def size_lb(self):
        msg.showinfo(title="Size of linkedlist",message="Size of linkedlist is %d"%(len(self.allnodes)))
        return
    def insert_lb(self):
        input = nodell.get()
        atpos = int(atposll.get())

        if int(atpos)>=len(self.allnodes):
            msg.showwarning(title="Error",message="Index out of range")
            return
        i = 0
        temp = self.head
        prev = None

        new_node = Node(input)
        while i<atpos:
                i+=1
                prev = temp
                temp = temp.next
        if atpos==0:
            new_node.next = temp
            self.head = new_node
            x, y, x1, y1 = 20,80,60,120

        else:
            prev.next = new_node
            new_node.next = temp
            x, y, x1, y1 = output_ll.coords(self.allnodes[i][0])
            y += 40
            y1 += 40

        sr = list(map(int, output_ll['scrollregion'].split()))
        output_ll.xview_moveto((x-45) / (sr[2] + 45))

        ll_rect = output_ll.create_rectangle(x, y + 40, x1, y1 + 40)
        ll_rectnext = output_ll.create_rectangle(x + 40, y + 40, x + 45, y1 + 40)
        ll_text = output_ll.create_text(x + 20, y + 60, text=input, fill="#d8d8d8")
        arrow = output_ll.create_line(x + 42.5, y + 60, x + 60, y + 60,
                                      arrow=tk.LAST, capstyle=tk.BUTT, fill='black')
        self.allnodes.insert(atpos, [ll_rect, ll_rectnext, ll_text, arrow])

        output_ll.update()

        for j in range(i + 1, len(self.allnodes)):
            output_ll.move(self.allnodes[j][0], 62, 0)
            output_ll.move(self.allnodes[j][1], 62, 0)
            output_ll.move(self.allnodes[j][2], 62, 0)
            output_ll.move(self.allnodes[j][3], 62, 0)
            output_ll.update()
        time.sleep(0.3)
        output_ll.move(self.allnodes[i][0], 0, -80)
        output_ll.move(self.allnodes[i][1], 0, -80)
        output_ll.move(self.allnodes[i][2], 0, -80)
        output_ll.move(self.allnodes[i][3], 0, -80)
        output_ll.update()
        output_ll['scrollregion'] = (sr[0], sr[1], sr[2] + 65, sr[3])

        self.x += 62


back = ttk.Button(master=linkedlistpage,text="← Back",command=lambda:raise_frame(mainpage))
back.pack(anchor="w",padx=40,pady=20)
heading = ttk.Label(master=linkedlistpage, text="Linkedlist",font=('Helvetica',14))
heading.pack(fill=tk.X,padx=40,pady=10)
definition = ttk.Label(master=linkedlistpage,wraplength=width-10,font=('Helvetica', 12),justify='left',
                       text="A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.")
definition.pack(fill=tk.X,padx=40,pady=10)

set_of_operations = tk.Frame(master=linkedlistpage,padx=40,bg="#464646")

nodell = ttk.Entry(master=set_of_operations)
nodell.insert(0,"Enter node value")

atposll = ttk.Entry(master=set_of_operations)
atposll.insert(0,"Enter node position")


ll = linkedlistclass()
output_frame = ttk.Frame(master=linkedlistpage)
output_ll = tk.Canvas(master=output_frame,bg="#464646",bd=1, highlightthickness=1,  highlightbackground="#d8d8d8",relief=tk.FLAT,scrollregion=(0,0,100,100))


size_lb = ttk.Button(master=set_of_operations,text="SIZE",command = lambda:ll.size_lb())
add_lb = ttk.Button(master=set_of_operations,text="ADD",command = lambda:ll.add_lb(output_ll))
append_lb = ttk.Button(master=set_of_operations,text="APPEND",command = lambda:ll.append_lb(output_ll))
insert_lb = ttk.Button(master=set_of_operations,text="INSERT",command = lambda:ll.insert_lb())
remove_lb = ttk.Button(master=set_of_operations,text="REMOVE",command = lambda:ll.remove_lb(output_ll))

nodell.pack(side=tk.LEFT,ipady=4,ipadx=4)
add_lb.pack(side=tk.LEFT,padx=2)
append_lb.pack(side=tk.LEFT,padx=2)
size_lb.pack(side=tk.LEFT,padx=2)
remove_lb.pack(side=tk.LEFT,padx=2)
atposll.pack(side=tk.LEFT,ipady=4,ipadx=4)
insert_lb.pack(side=tk.LEFT,padx=2)

set_of_operations.pack(fill=tk.X)


horscroll = tk.Scrollbar(master=output_frame,orient=tk.HORIZONTAL)
horscroll.configure(command=output_ll.xview)
horscroll.pack(side=tk.BOTTOM,fill=tk.X)

output_ll.configure(xscrollcommand=horscroll.set)

output_ll.pack(fill=tk.BOTH,expand=1)
output_frame.pack(pady=20,padx=40,fill=tk.BOTH,expand=1)

#linkedlistpageends



#stack
class stackclass(object):
    def __init__(self):
        self.stacklist = []
        self.stack_lr = []
        self.stack_lrt = []
        self.x = 20
        self.y = 40

    def push(self,output):
        input = node.get()
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input",message="Please enter input")
            return
        self.stacklist.append(input)
        curr_rect = output.create_rectangle(self.x,self.y,self.x+40,self.y+40)
        self.stack_lr.append(curr_rect)

        curr_text = output.create_text(self.x + 20, self.y + 20,text=self.stacklist[-1],fill="#d8d8d8")
        self.stack_lrt.append(curr_text)
        self.x += 40

        sr = list(map(int, output.cget('scrollregion').split()))
        output['scrollregion'] = (sr[0], sr[1], sr[2] + 40, sr[3])
        output.xview_moveto((self.x+40)/(sr[2]+40))
        output.update()
        window.update()

    def pop(self,output):
        if len(self.stacklist)==0:
            msg.showwarning(title="Empty stack",message="Stack is empty")
            return
        todelr = self.stack_lr.pop()
        todelrt = self.stack_lrt.pop()
        output.move(todelr,40,self.y + 20)
        output.move(todelrt,40, self.y + 20)
        arrow = output.create_line(self.x-40,self.y+20, output.coords(todelr)[0],output.coords(todelr)[1], arrow=tk.LAST, capstyle=tk.BUTT, fill='black')
        output.update()

        time.sleep(0.28)

        output.delete(arrow)
        output.delete(todelr)
        output.delete(todelrt)
        self.stacklist.pop()

        self.x -= 40



    def top(self):
        if len(self.stacklist) == 0:
            msg.showwarning(title="Empty List", message="List is empty")
            return
        top = "Top element is " + str(self.stacklist[-1])
        msg.showinfo(title="Top", message=top)

    def size_(self):
        length = "Length is {}".format(len(self.stacklist))
        msg.showinfo(title="Length", message=length)



back = ttk.Button(master=stackpage,text="← Back",command=lambda:raise_frame(mainpage))
back.pack(anchor="w",padx=40,pady=20)
heading = ttk.Label(master=stackpage, text="Stack",font=('Helvetica',14))
heading.pack(fill=tk.X,padx=40,pady=10)

definition = ttk.Label(master=stackpage,wraplength=width-10,font=('Helvetica', 12),justify='left',text="A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.")
definition.pack(fill=tk.X,padx=40,pady=10)

set_of_operations = tk.Frame(master=stackpage,padx=40,bg="#464646")

node= ttk.Entry(master=set_of_operations)
node.insert(0,"Enter node value")

stackl = stackclass()

output_frame = ttk.Frame(master=stackpage)

output = tk.Canvas(master=output_frame,bg="#464646",bd=1, highlightthickness=1,  highlightbackground="#d8d8d8",relief=tk.FLAT,scrollregion=(0,0,100,100))

push_b = ttk.Button(master=set_of_operations,text="PUSH",command = lambda:stackl.push(output))
pop_b = ttk.Button(master=set_of_operations,text="POP",command = lambda:stackl.pop(output))

top_b = ttk.Button(master=set_of_operations,text="PEEK",command = lambda:stackl.top())
size_b = ttk.Button(master=set_of_operations,text="SIZE",command = lambda:stackl.size_())

node.pack(side=tk.LEFT,ipady=4,ipadx=4)
push_b.pack(side=tk.LEFT,padx=2)
pop_b.pack(side=tk.LEFT,padx=2)
top_b.pack(side=tk.LEFT,padx=2)
size_b.pack(side=tk.LEFT,padx=2)


set_of_operations.pack(fill=tk.X)


horscroll = tk.Scrollbar(master=output_frame,orient=tk.HORIZONTAL)
horscroll.configure(command=output.xview)
horscroll.pack(side=tk.BOTTOM,fill=tk.X)

output.configure(xscrollcommand=horscroll.set)

output.pack(fill=tk.BOTH,expand=1)
output_frame.pack(pady=20,padx=40,fill=tk.BOTH,expand=1)

#stackpage ends












#logo
logo = PhotoImage(file="D:/python projects/logos/png/logoc.png")
window.iconphoto(False,logo)


#heading
heading = ttk.Frame(master=mainpage)

canvas = tk.Canvas(master=heading,width=100,height=100,bg="#464646")
mainimg = PhotoImage(file="D:/python projects/logos/png/mimg4.png")
canvas.create_image(50,50,image=mainimg)

canvas.config(highlightthickness=0)
canvas.pack(side=tk.LEFT,anchor=tk.CENTER)
title = ttk.Label(master=heading,text="vALGO",font=('Helvetica', 14))


title.pack(side=tk.LEFT,anchor=tk.CENTER)
heading.pack()

#mainpage
main = ttk.Frame(master=mainpage)

algo = settings.algos(main)
algoimg = "D:/python projects/logos/png/stack2.png"
buttonstack = algo.addalgo("stack",width,height,algoimg,0,0,stackpage)

algo = settings.algos(main)
algoimg = "D:/python projects/logos/png/ll.png"
buttontree = algo.addalgo("Linkedlist",width,height,algoimg,0,1,linkedlistpage)

algo = settings.algos(main)
algoimg = "D:/python projects/logos/png/ptree.png"
buttonbtree = algo.addalgo("Queue",width,height,algoimg,0,2,queuepage)





main.pack()

window.mainloop()