import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import footer

class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedlist_contents(object):
    def __init__(self,ancestorpage,parentframe,width,height):

        self.head = None
        self.x = 20
        self.y = 40
        self.allnodes = []

        self.back = ttk.Button(master=parentframe, text="← Back", command=lambda: self.raise_frame(ancestorpage))
        self.back.pack(anchor="w", padx=40, pady=20)
        self.heading = ttk.Label(master=parentframe, text="Linkedlist", font=('Helvetica', 14))
        self.heading.pack(fill=tk.X, padx=40, pady=10)
        self.definition = ttk.Label(master=parentframe, wraplength=width - 10, font=('Helvetica', 12), justify='left',
                               text="A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.")
        self.definition.pack(fill=tk.X, padx=40, pady=10)

        self.set_of_operations = tk.Frame(master=parentframe, padx=40, bg="#464646")

        self.node = ttk.Entry(master=self.set_of_operations)
        self.node.insert(0, "Enter node value")

        self.atpos = ttk.Entry(master=self.set_of_operations)
        self.atpos.insert(0, "Enter node position")

        self.output_frame = ttk.Frame(master=parentframe)
        self.output = tk.Canvas(master=self.output_frame, bg="#464646", bd=1, highlightthickness=1,
                              highlightbackground="#d8d8d8", relief=tk.FLAT, scrollregion=(0, 0, 100, 100))

        self.size_b = ttk.Button(master=self.set_of_operations, text="SIZE", command=lambda: self.size_lb(self.output))
        self.add_b = ttk.Button(master=self.set_of_operations, text="ADD", command=lambda: self.add_lb(self.output))
        self.append_b = ttk.Button(master=self.set_of_operations, text="APPEND", command=lambda: self.append_lb(self.output))
        self.insert_b = ttk.Button(master=self.set_of_operations, text="INSERT", command=lambda: self.insert_lb(self.output))
        self.remove_b = ttk.Button(master=self.set_of_operations, text="REMOVE", command=lambda: self.remove_lb(self.output))

        self.node.pack(side=tk.LEFT, ipady=4, ipadx=4)
        self.add_b.pack(side=tk.LEFT, padx=2)
        self.append_b.pack(side=tk.LEFT, padx=2)
        self.size_b.pack(side=tk.LEFT, padx=2)
        self.remove_b.pack(side=tk.LEFT, padx=2)
        self.atpos.pack(side=tk.LEFT, ipady=4, ipadx=4)
        self.insert_b.pack(side=tk.LEFT, padx=2)

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
        
    def add_lb(self,output):
        input = self.node.get()
        new_node = Node(input)
        new_node.next = self.head
        self.head = new_node

        #canvas part
        output.move(tk.ALL,62,0)
        ll_rect = output.create_rectangle(20,40,60,80,fill='#3779D2')
        ll_rectnext  = output.create_rectangle(60,40,65,80)
        ll_text = output.create_text(40, 60,text=input,fill="#d8d8d8")
        arrow = output.create_line(62.5,60,80.5,60,
                                   arrow=tk.LAST, capstyle=tk.BUTT, fill='black')
        sr = list(map(int,output['scrollregion'].split()))
        output['scrollregion'] = (sr[0], sr[1], sr[2] + 65, sr[3])
        #output.xview_moveto((self.x + 45) / (sr[2] + 45))
        output.xview_moveto(0)
        output.update()
        time.sleep(0.28)
        output.itemconfig(ll_rect,fill="")

        output.update()
        self.x += 62
        self.allnodes.insert(0,[ll_rect,ll_rectnext,ll_text,arrow])

    def append_lb(self,output):
        input = self.node.get()
        temp = self.head
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return

        if not self.head:
            return self.add_lb(output)
        else:
            while temp:
                prev = temp
                temp = temp.next
            new_node = Node(input)
            prev.next = new_node

        #canvas
        ll_rect = output.create_rectangle(self.x, self.y, self.x + 40, self.y + 40,fill='#3779D2')

        ll_text = output.create_text(self.x + 20, self.y + 20, text=input, fill="#d8d8d8")
        ll_rectnext = output.create_rectangle(self.x+40, 40, self.x + 45, 80)

        arrow = output.create_line(self.x+42.5,self.y+20,self.x+60.5,self.y+20,
                                      arrow=tk.LAST, capstyle=tk.BUTT, fill='black')
        sr = list(map(int, output['scrollregion'].split()))
        output['scrollregion'] = (sr[0], sr[1], sr[2] + 65, sr[3])
        output.xview_moveto((self.x + 45) / (sr[2] + 45))

        output.update()
        time.sleep(0.28)
        output.itemconfig(ll_rect, fill="")
        output.update()

        self.allnodes.append([ll_rect, ll_rectnext, ll_text, arrow])
        self.x += 62


    def remove_lb(self,output):
        input = self.node.get()
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
            x,y,x1,y1 = output.coords(self.allnodes[i][0])
            sr = list(map(int, output['scrollregion'].split()))
            output.xview_moveto((x - 45) / (sr[2] + 45))

            for j in range(4):
                output.move(self.allnodes[i][j],0,60)
            output.itemconfig(self.allnodes[i][0], fill="#DC143C")
            output.update()

            time.sleep(0.09)
            output.itemconfig(self.allnodes[i][0], fill="#800000")
            output.update()

            time.sleep(0.1)
            output.itemconfig(self.allnodes[i][0], fill="#DC143C")
            output.update()

            time.sleep(0.09)
            output.update()
            output.delete(self.allnodes[i][1],self.allnodes[i][0],self.allnodes[i][3],self.allnodes[i][2])
            for j in range(i+1,len(self.allnodes)):
                output.move(self.allnodes[j][0], -62,0)
                output.move(self.allnodes[j][1], -62,0)
                output.move(self.allnodes[j][2], -62,0)
                output.move(self.allnodes[j][3], -62,0)
                output.update()
            self.x -= 62

            self.allnodes.pop(i)

    def size_lb(self,output):
        msg.showinfo(title="Size of linkedlist",message="Size of linkedlist is %d"%(len(self.allnodes)))
        return
    def insert_lb(self,output):
        input = self.node.get()
        atpos = int(self.atpos.get())

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
            x, y, x1, y1 = output.coords(self.allnodes[i][0])
            y += 40
            y1 += 40

        sr = list(map(int, output['scrollregion'].split()))
        output.xview_moveto((x-45) / (sr[2] + 45))

        ll_rect = output.create_rectangle(x, y + 40, x1, y1 + 40,fill='#3779D2')
        ll_rectnext = output.create_rectangle(x + 40, y + 40, x + 45, y1 + 40)
        ll_text = output.create_text(x + 20, y + 60, text=input, fill="#d8d8d8")
        arrow = output.create_line(x + 42.5, y + 60, x + 60, y + 60,
                                      arrow=tk.LAST, capstyle=tk.BUTT, fill='black')
        self.allnodes.insert(atpos, [ll_rect, ll_rectnext, ll_text, arrow])
        output.update()



        for j in range(i + 1, len(self.allnodes)):
            output.move(self.allnodes[j][0], 62, 0)
            output.move(self.allnodes[j][1], 62, 0)
            output.move(self.allnodes[j][2], 62, 0)
            output.move(self.allnodes[j][3], 62, 0)
            output.update()
        time.sleep(0.28)
        output.itemconfig(self.allnodes[i][0], fill="")
        output.update()

        output.move(self.allnodes[i][0], 0, -80)
        output.move(self.allnodes[i][1], 0, -80)
        output.move(self.allnodes[i][2], 0, -80)
        output.move(self.allnodes[i][3], 0, -80)
        output.update()
        output['scrollregion'] = (sr[0], sr[1], sr[2] + 65, sr[3])

        self.x += 62
