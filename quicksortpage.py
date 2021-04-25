import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import footer
class quicksort_contents(object):
    def __init__(self,ancestorpage,parentframe,width,height):
        self.back = ttk.Button(master=parentframe, text="← Back", command=lambda: self.raise_frame(ancestorpage))
        self.back.pack(anchor="w", padx=40, pady=20)

        self.x = 20
        self.y = 0

        self.heading = ttk.Label(master=parentframe, text="Quick Sort", font=('Helvetica', 14))
        self.heading.pack(fill=tk.X, padx=40, pady=10)

        self.definition = ttk.Label(master=parentframe, wraplength=width - 10, font=('Helvetica', 12), justify='left',
                                    text="Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. In our case we will select last element as pivot.")
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
        numbers = list(map(int, input.strip().split(',')))
        total_numbers = (len(numbers)*40+40)

        output['scrollregion'] = (0, 0, (len(numbers) * 40)+160, 80)
        output.update()
        self.x = (output.winfo_width() - total_numbers)//2


        self.y = 40
        for i in numbers:
            rect = output.create_rectangle(self.x, self.y, self.x + 40, self.y+40)
            text = output.create_text(self.x + 20, self.y + 20, text=str(i),fill="white")
            self.x += 40
            self.rectangles.append([rect, text])



        self.start(self.rectangles,numbers,output,0,len(numbers)-1)

    def start(self,rectangles,numbers,output,low,high):
        if len(numbers)==1:
            return numbers
        if low<high:
            pi = self.partition(rectangles,numbers,low,high,output)

            self.start(rectangles,numbers,output,low,pi-1)
            self.start(rectangles, numbers, output,pi + 1,high)



    def partition(self,rectangles,numbers,low,high,output):
        i = low-1
        pivot = numbers[high]
        output.itemconfig(rectangles[high][1],fill="black")
        output.itemconfig(rectangles[high][0], fill="#3be13b")

        x,y,x1,y1 = output.coords(rectangles[high][0])
        pivot_text = output.create_text((x1+x)//2,y1+20,text="pivot",fill="white")

        output.update()
        time.sleep(0.3)



        for j in range(low,high):
            if numbers[j]<=pivot:
                i+=1
                if i!=j:
                    self.animate(rectangles[i],rectangles[j],output)
                numbers[i],numbers[j] = numbers[j],numbers[i]

                output.itemconfig(rectangles[i][1], text=numbers[i])
                output.itemconfig(rectangles[j][1], text=numbers[j])
                output.update()
                time.sleep(0.6)

        numbers[i+1],numbers[high] = numbers[high],numbers[i+1]
        output.itemconfig(rectangles[i+1][1], text=numbers[i+1])
        output.itemconfig(rectangles[high][1], text=numbers[high])
        output.itemconfig(rectangles[i+1][0], fill="#3be13b")
        output.itemconfig(rectangles[i + 1][1], fill="black")

        output.itemconfig(rectangles[high][0], fill="")
        output.delete(pivot_text)
        x,y,x1,y1 = output.coords(rectangles[i+1][0])
        pivot_text = output.create_text((x1+x)//2,y1+20,text="pivot",fill="white")



        output.update()
        time.sleep(0.6)

        output.delete(pivot_text)
        output.itemconfig(rectangles[high][1], fill="white")
        output.itemconfig(rectangles[i + 1][0], fill="")
        output.itemconfig(rectangles[i + 1][1], fill="white")

        return i+1

    def animate(self,obj1,obj2,output,color='#fb5581',color1='#f18b74'):
            output.itemconfig(obj1[0], fill=color)
            output.itemconfig(obj2[0], fill=color1)
            output.itemconfig(obj1[1], fill="black")
            output.itemconfig(obj2[1], fill="black")

            output.update()
            time.sleep(0.3)
            output.itemconfig(obj1[0], fill="")
            output.itemconfig(obj2[0], fill="")
            output.itemconfig(obj1[1], fill="white")
            output.itemconfig(obj2[1], fill="white")

            output.update()
            time.sleep(0.3)




    def raise_frame(self,ancestorpage):
        ancestorpage.tkraise()




