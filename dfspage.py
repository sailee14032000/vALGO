import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import footer

class dfs_contents(object):

    def __init__(self,ancestorpage,parentframe,width,height):
        self.no_of_nodes = 0
        self.graph_nodes = {}

        self.back = ttk.Button(master=parentframe, text="← Back", command=lambda: self.raise_frame(ancestorpage))
        self.back.pack(anchor="w", padx=40, pady=20)

        self.x = 20
        self.y = 0

        self.heading = ttk.Label(master=parentframe, text="DFS", font=('Helvetica', 14))
        self.heading.pack(fill=tk.X, padx=40, pady=10)

        self.definition = ttk.Label(master=parentframe, wraplength=width - 10, font=('Helvetica', 12), justify='left',
                                    text="Depth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.")
        self.definition.pack(fill=tk.X, padx=40, pady=10)

        self.set_of_operations = tk.Frame(master=parentframe, padx=40, bg="#464646")


        self.node = ttk.Entry(master=self.set_of_operations,width=50)
        self.node.insert(0, "Enter starting vertex")
        self.output_frame = ttk.Frame(master=parentframe)

        self.output = tk.Canvas(master=self.output_frame, bg="#464646", bd=1, highlightthickness=1, highlightbackground="#d8d8d8",
                           relief=tk.FLAT, scrollregion=(0, 0, 100, 100))


        self.start = ttk.Button(master=self.set_of_operations, text="START", command=lambda: self.dfs(self.output))
        self.cgraph = ttk.Button(master=self.set_of_operations, text="CREATE GRAPH",
                                      command=lambda:self.creategraph(self.output))

        self.cgraph.pack(side=tk.LEFT, padx=2)
        self.node.pack(side=tk.LEFT, ipady=4, padx=2)
        self.start.pack(side=tk.LEFT, padx=2)
        self.set_of_operations.pack(fill=tk.X)


        self.output.pack(fill=tk.BOTH, expand=1)
        self.output_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=1)
        self.end = footer.footerlabel(parentframe)

    def dfs(self,output):

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
        self.dfs_util(output,input,visited)

    def dfs_util(self,output,input,visited):

        input = int(input)

        output.itemconfig(self.graph_nodes[input][0], fill='#3be13b')
        output.itemconfig(self.graph_nodes[input][1], fill='black')
        output.update()
        time.sleep(1)

        visited[int(input)-1] = True

        for i in self.graph_nodes[input][2]:
            if not visited[i - 1]:
                if i in list(map(lambda x: x[0], self.graph_nodes[input][3])):
                    index_ = list(map(lambda x: x[0], self.graph_nodes[input][3])).index(i)
                    output.itemconfig(self.graph_nodes[input][3][index_][1], fill='#3be13b')
                    output.itemconfig(self.graph_nodes[input][3][index_][1], width=1)
                self.dfs_util(output,i,visited)






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




