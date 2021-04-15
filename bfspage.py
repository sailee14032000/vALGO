import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import footer

class bfs_contents(object):

    def __init__(self,ancestorpage,parentframe,width,height):
        self.no_of_nodes = 0
        self.graph_nodes = {}

        self.back = ttk.Button(master=parentframe, text="← Back", command=lambda: self.raise_frame(ancestorpage))
        self.back.pack(anchor="w", padx=40, pady=20)

        self.x = 20
        self.y = 0

        self.heading = ttk.Label(master=parentframe, text="BFS", font=('Helvetica', 14))
        self.heading.pack(fill=tk.X, padx=40, pady=10)

        self.definition = ttk.Label(master=parentframe, wraplength=width - 10, font=('Helvetica', 12), justify='left',
                                    text="Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.")
        self.definition.pack(fill=tk.X, padx=40, pady=10)

        self.set_of_operations = tk.Frame(master=parentframe, padx=40, bg="#464646")


        self.node = ttk.Entry(master=self.set_of_operations,width=50)
        self.node.insert(0, "Enter starting vertex")
        self.output_frame = ttk.Frame(master=parentframe)

        self.output = tk.Canvas(master=self.output_frame, bg="#464646", bd=1, highlightthickness=1, highlightbackground="#d8d8d8",
                           relief=tk.FLAT, scrollregion=(0, 0, 100, 100))


        self.start = ttk.Button(master=self.set_of_operations, text="START", command=lambda: self.bfs(self.output))
        self.cgraph = ttk.Button(master=self.set_of_operations, text="CREATE GRAPH",
                                      command=lambda:self.creategraph(self.output))

        self.cgraph.pack(side=tk.LEFT, padx=2)
        self.node.pack(side=tk.LEFT, ipady=4, padx=2)
        self.start.pack(side=tk.LEFT, padx=2)
        self.set_of_operations.pack(fill=tk.X)


        self.output.pack(fill=tk.BOTH, expand=1)
        self.output_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=1)
        self.end = footer.footerlabel(parentframe)

    def bfs(self,output):

        output.configure(bg='#464646')
        output.unbind('<ButtonPress-1>')
        output.unbind('<B1-Motion>')
        output.unbind('<ButtonRelease-1>')

        if len(list(output.find_all()))==0:
            msg.showinfo(title="Creating a graph", message="Click inside the canvas section to create graph nodes and then click start")

        input = self.node.get()
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return

        visited = [False]*self.no_of_nodes
        bfs_queue = []
        bfs_queue.append(int(input))
        visited[int(input)-1] = True

        while bfs_queue:

            current = bfs_queue.pop(0)
            output.itemconfig(self.graph_nodes[current][0],fill='#3be13b')
            output.itemconfig(self.graph_nodes[current][1], fill='black')
            #output.itemconfig(self.graph_nodes[current][3][i], fill='#3be13b')
            #output.itemconfig(self.graph_nodes[current][3][i],width=1)
            output.update()
            time.sleep(1)

            for i in self.graph_nodes[current][2]:
                if not visited[i-1]:
                    bfs_queue.append(i)
                    if i in list(map(lambda x: x[0],self.graph_nodes[current][3])):
                        index_ = list(map(lambda x: x[0],self.graph_nodes[current][3])).index(i)
                        output.itemconfig(self.graph_nodes[current][3][index_][1], fill='#3be13b')
                        output.itemconfig(self.graph_nodes[current][3][index_][1], width=1)
                    visited[i-1] = True



    def creategraph(self,output):

        output.configure(bg='#d8d8d8')
        output.delete(tk.ALL)
        msg.showinfo(title="Creating a graph",
                     message="Click inside the canvas section to create graph nodes and then click start")

        self.no_of_nodes = 0
        self.graph_nodes.clear()


        #creating nodes and edges
        def create_new_node(event):

            x,y = event.x, event.y

            for i in range(1,self.no_of_nodes+1):

                x1, y1, x2, y2 = output.coords(self.graph_nodes[i][0])

                if x1 <= x <= x2 and y1 <= y <= y2:
                    line = output.create_line(x,y,x,y,arrow=tk.LAST,capstyle=tk.BUTT,fill="black")
                    #self.graph_nodes[i].insert(2,line)
                    self.draggable_line = [self.graph_nodes[i],line]
                    return

            else:
                self.no_of_nodes += 1

                node = output.create_oval(x - 20, y - 20, x + 20, y + 20, fill="black")
                text = output.create_text(x, y, text=str(self.no_of_nodes), fill="white")

                self.graph_nodes[self.no_of_nodes] = [node,text,[],[]]
                self.draggable_line = None


        def dragline(event):

            if self.draggable_line:
                x,y,x1,y1 = output.coords(self.draggable_line[1])
                output.coords(self.draggable_line[1],x,y,event.x,event.y)

        def stopline(event):

            if self.draggable_line:

                x,y = event.x,event.y
                from_node = output.itemcget(self.draggable_line[0][1],"text")
                possible_nodes = list(self.graph_nodes.keys())
                possible_nodes.remove(int(from_node))

                for i in possible_nodes:

                    x1,y1,x2,y2 = output.coords(self.graph_nodes[i][0])
                    #print(self.draggable_line[0][2],i,x1,x,x2,y1<=y<=y2)
                    if x1<=x<=x2 and y1<=y<=y2 and (i not in self.draggable_line[0][2]):

                        output.tag_lower(self.draggable_line[1])
                        self.draggable_line[0][2].append(i)
                        self.draggable_line[0][3].append([i,self.draggable_line[1]])
                        return

                else:
                    output.delete(self.draggable_line[1])



        output.bind('<ButtonPress-1>',create_new_node)
        output.bind('<B1-Motion>',dragline)
        output.bind('<ButtonRelease-1>',stopline)



    def raise_frame(self,ancestorpage):
        ancestorpage.tkraise()




