'''
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

coords = {"x":0,"y":0,"x2":0,"y2":0}
# keep a reference to all lines by keeping them in a list
lines = []

def click(e):
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y

    # create a line on this point and store it in the list
    lines.append(canvas.create_line(coords["x"],coords["y"],coords["x"],coords["y"]))

def drag(e):
    # update the coordinates from the event
    coords["x2"] = e.x
    coords["y2"] = e.y

    # Change the coordinates of the last created line to the new coordinates
    canvas.coords(lines[-1], coords["x"],coords["y"],coords["x2"],coords["y2"])

canvas.bind("<ButtonPress-1>", click)
canvas.bind("<B1-Motion>", drag)

root.mainloop()
'''
'''
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("inserting 22 to left")

engine.runAndWait()
'''
'''
        if temp.left is None and temp.right is None:
            if dir1=="root":
                self.root = None
            if dir2 == "l":
                prev.left = None
            elif dir2=="r":
                prev.right = None
            canvas = temp.canvas
            output.delete(canvas[0], canvas[1], canvas[2])
            for i in range(len(deletion_to_be_made)):
                self.move_all_cnodes(deletion_to_be_made[i][0], deletion_to_be_made[i][1], deletion_to_be_made[i][2],
                                     True)
            return
        if temp.right:
            temp_n = temp.right
            prev_n = temp_n
            if temp_n.left:
                while temp_n:
                    prev_n = temp_n
                    temp_n = temp_n.left
                output.itemconfig(temp.canvas[1], text=prev_n.val)
                output.itemconfig(prev_n.canvas[1], text=temp.val)
                output.update()
                time.sleep(1)
                self.delete(output, [prev_n, temp,deletion_to_be_made])

            else:
                self.move_all_cnodes(temp.right, -40, output,True, -40)
                prev.right = temp.right
                temp.right.parent = prev
                canvas = temp.canvas
                output.delete(canvas[0],canvas[1],canvas[2])
                xa, ya, xa1, ya1 = output.coords(prev.canvas[0])
                xp, yp, xp1, yp1 = output.coords(prev.right.canvas[0])
                output.coords(temp.right.canvas[2], xa1, ya + 20, xp + 20, yp)





        else:
            temp_n = temp.left
            prev_n = temp_n
            if temp_n.right:
                while temp_n:
                    prev_n = temp_n
                    temp_n = temp_n.right

                output.itemconfig(temp.canvas[1],text=prev_n.val)
                output.itemconfig(prev_n.canvas[1], text=temp.val)
                output.update()
                time.sleep(1)
                print(prev_n.val)
                self.delete(output,[prev_n,temp,deletion_to_be_made])

            else:
                self.move_all_cnodes(temp.left, 40, output,True, -40)
                prev.left = temp.left
                temp.left.parent = prev
                canvas = temp.canvas
                output.delete(canvas[0],canvas[1],canvas[2])
                xa, ya, xa1, ya1 = output.coords(prev.canvas[0])
                xp, yp, xp1, yp1 = output.coords(prev.left.canvas[0])
                output.coords(temp.left.canvas[2], xa, ya + 20, xp + 20, yp)

'''
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
        self.bfspage = ttk.Frame(master=self.window)
        self.dfspage = ttk.Frame(master=self.window)
        self.bubblesortpage = ttk.Frame(master=self.window)
        self.insertionsortpage = ttk.Frame(master=self.window)
        self.selectionsortpage = ttk.Frame(master=self.window)
        self.dashboardpage = ttk.Frame(master=self.window)

        self.pages = [self.selectionsortpage,self.insertionsortpage,self.bubblesortpage,self.dfspage,self.bfspage,self.binarysearchtreepage,self.queuepage,self.stackpage,self.linkedlistpage,self.dashboardpage]
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

        #graph
        bfs = bfspage.bfs_contents(self.dashboardpage, self.bfspage, self.width,self.height)
        dfs = dfspage.dfs_contents(self.dashboardpage, self.dfspage, self.width,self.height)


    def dashboard_page(self,parentframe):

        def on_configure(event):
            dashboard_canvas.configure(scrollregion=dashboard_canvas.bbox(tk.ALL))

        dashboard_canvas = tk.Canvas(parentframe, highlightthickness=0)
        dashboard_frame = ttk.Frame(dashboard_canvas)

        yscrollbar = tk.Scrollbar(parentframe, command=dashboard_canvas.yview)
        dashboard_canvas.config(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        dashboard_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        dashboard_canvas.create_window((0,0), window=dashboard_frame, anchor="center")
        dashboard_frame.bind('<Configure>', on_configure)


        heading = ttk.Frame(master=dashboard_frame)

        canvas = tk.Canvas(master=heading, width=100, height=100, bg="#464646")
        self.mainimg = PhotoImage(file="D:/python projects/logos/png/mimg4.png")
        canvas.create_image(50, 50, image=self.mainimg)

        canvas.config(highlightthickness=0)
        canvas.pack(side=tk.LEFT, anchor=tk.CENTER)

        title = ttk.Label(master=heading, text="vALGO", font=('Helvetica', 16))
        title.pack(side=tk.LEFT, anchor=tk.CENTER)

        heading.pack()


        contents = ttk.Frame(master=dashboard_frame)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/stack2.png"
        algo.addalgo("stack",self.width, self.height, algoimg, 0, 0, self.stackpage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/ll.png"
        algo.addalgo("Linkedlist", self.width, self.height, algoimg, 0, 1, self.linkedlistpage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/queue.png"
        algo.addalgo("Queue", self.width, self.height, algoimg, 0, 2, self.queuepage)


        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/selectionsort.png"
        algo.addalgo("Selection sort", self.width, self.height, algoimg, 1, 0,
                                  self.selectionsortpage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/bubblesort.png"

        algo.addalgo("Bubble sort", self.width, self.height, algoimg, 2,1,
                                  self.bubblesortpage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/insertionsort.png"
        algo.addalgo("Insertion sort", self.width, self.height, algoimg, 1, 2,
                                        self.insertionsortpage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/binarytree.png"
        algo.addalgo("Binary Search Tree", self.width, self.height, algoimg, 2, 0, self.binarysearchtreepage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/bfs.png"
        algo.addalgo("BFS", self.width, self.height, algoimg, 1, 1, self.bfspage)

        algo = settings.algos(contents)
        algoimg = "D:/python projects/logos/png/dfs.png"
        algo.addalgo("DFS", self.width, self.height, algoimg, 2, 2, self.dfspage)


        contents.pack()
        self.end = footer.footerlabel(dashboard_frame)

    def start(self):
        self.window.mainloop()
if __name__=="__main__":
    valgo = vALGO()
    valgo.dashboard_page(valgo.dashboardpage)
    valgo.start()

    '''
            self.y +=80
            self.draw(left_sub_array,right_sub_array,self.y,output)
            self.start_sort(rectangles,left_sub_array,output)
            self.start_sort(rectangles,right_sub_array,output)
    def draw(self,left,right,y,output):
        self.x = 40
        j = 0
        for i in left:
            rect = output.create_rectangle(self.x, y, self.x + 40, y+40)
            text = output.create_text(self.x + 20, y + 20, text=str(i),fill="white")
            self.x += 40
            j+=1
        self.x += 40*j

        output.update()
        for i in right:
            rect = output.create_rectangle(self.x, y, self.x + 40, y + 40)
            text = output.create_text(self.x + 20, y + 20, text=str(i), fill="white")
            self.x += 40

        time.sleep(0.3)
        '''
