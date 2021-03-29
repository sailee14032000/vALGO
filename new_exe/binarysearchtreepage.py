import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import footer

class Node(object):
    def __init__(self,val,canvas,parent=None):
        self.val = val
        self.left = None
        self.right = None
        self.canvas = canvas
        self.parent = parent


class binarysearchtree_contents(object):
    def __init__(self, ancestorpage, parentframe, width, height):

        self.x = width/2
        self.y = 40
        self.root = None


        self.back = ttk.Button(master=parentframe, text="← Back", command=lambda: self.raise_frame(ancestorpage))
        self.back.pack(anchor="w", padx=40, pady=20)

        self.heading = ttk.Label(master=parentframe, text="Binary Search Tree", font=('Helvetica', 14))
        self.heading.pack(fill=tk.X, padx=40, pady=10)

        self.definition = ttk.Label(master=parentframe, wraplength=width - 10, font=('Helvetica', 12), justify='left',
                                    text="""Binary Search Tree is a node-based binary tree data structure which has the following properties:\n1) The left subtree of a node contains only nodes with keys lesser than the node’s key.\n2) The right subtree of a node contains only nodes with keys greater than the node’s key.\n3) The left and right subtree each must also be a binary search tree""")
        self.definition.pack(fill=tk.X, padx=40, pady=10)

        self.set_of_operations = tk.Frame(master=parentframe, padx=40, bg="#464646")

        self.node = ttk.Entry(master=self.set_of_operations)
        self.node.insert(0, "Enter node value")


        self.output_frame = ttk.Frame(master=parentframe)

        self.output = tk.Canvas(master=self.output_frame, bg="#464646", bd=1, highlightthickness=1, highlightbackground="#d8d8d8",
                           relief=tk.FLAT, scrollregion=(0, 0, 100, 100))

        self.insert_b = ttk.Button(master=self.set_of_operations, text="INSERT", command=lambda: self.insert(self.output))
        self.search_b = ttk.Button(master=self.set_of_operations, text="SEARCH", command=lambda: self.search(self.output))
        self.delete_b = ttk.Button(master=self.set_of_operations, text="DELETE", command=lambda: self.delete(self.output))

        self.node.pack(side=tk.LEFT, ipady=4, ipadx=4)
        self.insert_b.pack(side=tk.LEFT, padx=2)
        self.search_b.pack(side=tk.LEFT, padx=2)
        self.delete_b.pack(side=tk.LEFT, padx=2)

        self.set_of_operations.pack(fill=tk.X)

        self.horscroll = tk.Scrollbar(master=self.output_frame,orient=tk.HORIZONTAL)
        self.horscroll.configure(command=self.output.xview)
        self.horscroll.pack(side=tk.BOTTOM,fill=tk.X)

        self.verscroll = tk.Scrollbar(master=self.output_frame, orient=tk.VERTICAL)
        self.verscroll.configure(command=self.output.yview)
        self.verscroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.output.configure(yscrollcommand=self.verscroll.set,xscrollcommand=self.horscroll.set)

        self.output.pack(fill=tk.BOTH, expand=1)
        self.output_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=1)
        self.output['scrollregion'] = (0, 0,width,height)
        self.end = footer.footerlabel(parentframe)

    def raise_frame(self,ancestorpage):
        ancestorpage.tkraise()

    def insert(self,output):

        input = int(self.node.get())
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return
        if not self.root:
            curr_circle = output.create_oval(self.x,self.y,self.x+40,self.y+40,fill="black")
            curr_text = output.create_text(self.x+20,self.y+20,text=input,fill="white")
            canvas = [curr_circle,curr_text,None]
            self.root = Node(input,canvas)
            self.animate(canvas,output)
            return
        temp = self.root
        #Left sub tree from root
        if input<temp.val:

            while temp:
                if input<temp.val:
                    prev = temp
                    self.animate(prev.canvas,output)
                    temp = temp.left

                    if not temp:
                        ancestor = prev.parent

                        if ancestor and ancestor.val <= prev.val:
                            self.move_all_cnodes(prev, 40, output)
                            #output.move(prev.canvas[0], 40, 0)
                            #output.move(prev.canvas[1], 40, 0)
                            #xa, ya, xa1, ya1 = output.coords(ancestor.canvas[0])
                            #xp, yp, xp1, yp1 = output.coords(prev.canvas[0])
                            #output.coords(prev.canvas[2], xa1, ya + 20, xp + 20, yp)
                            #output.update()

                        x, y, x1, y1 = output.coords(prev.canvas[0])
                        arrow = output.create_line(x, y + 20, x - 20, y + 40, arrow=tk.LAST, capstyle=tk.BUTT,
                                                   fill="black")

                        x -= 40
                        y += 40

                        curr_circle = output.create_oval(x, y, x + 40, y + 40, fill="black")
                        curr_text = output.create_text(x + 20, y + 20, text=input, fill="white")
                        canvas = [curr_circle, curr_text, arrow]
                        prev.left = Node(input, canvas, prev)
                        self.animate(canvas, output)

                        sr = list(map(int,output.cget('scrollregion').split()))
                        if x<=sr[0]:
                            output.move(tk.ALL,50,0)
                            output.update()
                            output['scrollregion'] = (sr[0],sr[1],sr[2]+100,sr[3])
                        sr = list(map(int, output.cget('scrollregion').split()))

                        if y + 100>= sr[3]:
                            output['scrollregion'] = (sr[0], sr[1], sr[2], sr[3] + 100)
                            output.update()



                    else:
                        ancestor = prev.parent
                        if ancestor and ancestor.val <= prev.val:
                            self.move_all_cnodes(prev, 40, output)
                            output.update()

                else:
                    prev = temp
                    self.animate(prev.canvas, output)
                    ancestor = prev.parent
                    temp = temp.right

                    if not temp:
                        if ancestor and ancestor.val > prev.val:
                            self.move_all_cnodes(prev, -40, output)
                        x, y, x1, y1 = output.coords(prev.canvas[0])
                        arrow = output.create_line(x1, y + 20, x1 + 20, y + 40, arrow=tk.LAST, capstyle=tk.BUTT,
                                                   fill="black")
                        x += 40
                        y += 40

                        # print(x, y)
                        curr_circle = output.create_oval(x, y, x + 40, y + 40, fill="black")
                        curr_text = output.create_text(x + 20, y + 20, text=input, fill="white")
                        canvas = [curr_circle, curr_text, arrow]
                        prev.right = Node(input, canvas, prev)
                        self.animate(canvas, output)

                        sr = list(map(int, output.cget('scrollregion').split()))
                        if x >= sr[2]*0.75:
                            output.update()
                            output['scrollregion'] = (sr[0], sr[1], sr[2] + 100, sr[3])
                        sr = list(map(int, output.cget('scrollregion').split()))

                        if y +100 >= sr[3]:
                            output['scrollregion'] = (sr[0], sr[1], sr[2], sr[3] + 100)
                            output.update()

                    else:
                        if ancestor and ancestor.val > prev.val:
                            self.move_all_cnodes(prev, -40, output)
                            sr = list(map(int, output.cget('scrollregion').split()))
                            output.move(tk.ALL, 50, 0)
                            output['scrollregion'] = (sr[0], sr[1], sr[2] + 100, sr[3])
                            output.update()


        # Right sub tree from root
        else:
            while temp:
                if input>=temp.val:
                    prev = temp
                    self.animate(prev.canvas, output)

                    temp = temp.right

                    if not temp:
                        ancestor = prev.parent

                        if ancestor and ancestor.val > prev.val:
                            self.move_all_cnodes(prev, -40, output)
                        x, y, x1, y1 = output.coords(prev.canvas[0])
                        arrow = output.create_line(x1, y + 20, x1 + 20, y + 40, arrow=tk.LAST, capstyle=tk.BUTT,
                                                   fill="black")

                        x += 40
                        y += 40

                        curr_circle = output.create_oval(x, y, x + 40, y + 40, fill="black")
                        curr_text = output.create_text(x + 20, y + 20, text=input, fill="white")
                        canvas = [curr_circle, curr_text, arrow]
                        prev.right = Node(input, canvas, prev)
                        self.animate(canvas, output)

                        sr = list(map(int, output.cget('scrollregion').split()))
                        if x >= sr[2]*0.75:
                            output['scrollregion'] = (sr[0], sr[1], sr[2]+100, sr[3])
                            output.update()
                        sr = list(map(int, output.cget('scrollregion').split()))

                        if y + 100 >= sr[3]:
                            output['scrollregion'] = (sr[0], sr[1], sr[2], sr[3] + 100)
                            output.update()


                    else:
                        ancestor = prev.parent
                        if ancestor and ancestor.val > prev.val:
                            self.move_all_cnodes(prev, -40, output)
                            sr = list(map(int, output.cget('scrollregion').split()))
                            output.move(tk.ALL, 50, 0)
                            output['scrollregion'] = (sr[0], sr[1], sr[2] + 100, sr[3])
                            output.update()

                else:
                    prev = temp
                    self.animate(prev.canvas, output)
                    ancestor = prev.parent
                    temp = temp.left

                    if not temp:
                        if ancestor and ancestor.val <= prev.val:
                            self.move_all_cnodes(prev, 40, output)
                        x, y, x1, y1 = output.coords(prev.canvas[0])
                        arrow = output.create_line(x, y + 20, x - 20, y + 40, arrow=tk.LAST, capstyle=tk.BUTT,
                                                   fill="black")
                        x -= 40
                        y += 40

                        curr_circle = output.create_oval(x, y, x + 40, y + 40, fill="black")
                        curr_text = output.create_text(x + 20, y + 20, text=input, fill="white")
                        canvas = [curr_circle, curr_text, arrow]
                        prev.left = Node(input, canvas, prev)
                        self.animate(canvas,output)

                        sr = list(map(int, output.cget('scrollregion').split()))
                        if x < sr[0]:
                            output.move(tk.ALL,50,0)
                            output['scrollregion'] = (sr[0], sr[1], sr[2] + 100, sr[3])
                            output.update()
                        sr = list(map(int, output.cget('scrollregion').split()))

                        if y + 100 >= sr[3]:
                            output['scrollregion'] = (sr[0], sr[1], sr[2], sr[3] + 100)
                            output.update()

                    else:
                        if ancestor and ancestor.val <= prev.val:
                            self.move_all_cnodes(prev, 40, output)

    def search(self, output):
        input = int(self.node.get())
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return
        temp = self.root
        while temp:
            if input<temp.val:
                self.animate(temp.canvas,output)
                temp = temp.left
            elif input>temp.val:
                self.animate(temp.canvas, output)
                temp = temp.right
            else:
                self.animate(temp.canvas, output,'#fb5581')
                return
        else:
            msg.showwarning(title="Not Found",message="{} not present in tree.".format(input))
            return

    def delete(self, output):
        input = int(self.node.get())
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return
        pass


    def move_all_cnodes(self,parent,byx,output):
        q = [parent]
        ancestor = parent.parent
        xa,ya,xa1,ya1 = output.coords(ancestor.canvas[0])


        while len(q):
            prev = q[0]
            output.move(prev.canvas[0],byx,0)
            output.move(prev.canvas[1], byx, 0)
            output.move(prev.canvas[2], byx, 0)

            output.update()
            if prev.left:
                q.append(prev.left)
            if prev.right:
                q.append(prev.right)
            q.pop(0)
        xp, yp, xp1, yp1 = output.coords(parent.canvas[0])
        if byx>0:
            output.coords(parent.canvas[2], xa1, ya + 20, xp+20,yp)
        else:
            output.coords(parent.canvas[2], xa, ya + 20, xp + 20, yp)

    def animate(self,node,output,color='#3be13b'):
        output.itemconfig(node[0], fill=color)
        output.itemconfig(node[1], fill="black")
        output.update()
        time.sleep(0.3)
        output.itemconfig(node[0], fill="black")
        output.itemconfig(node[1], fill="white")
        output.update()







