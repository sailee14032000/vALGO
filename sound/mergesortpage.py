import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import footer
import voice_assistance
class mergesort_contents(object):
    def __init__(self,ancestorpage,parentframe,width,height):
        self.back = ttk.Button(master=parentframe, text="← Back", command=lambda: self.raise_frame(ancestorpage))
        self.back.pack(anchor="w", padx=40, pady=20)

        self.x = 20
        self.y = 0

        self.heading = ttk.Label(master=parentframe, text="Merge Sort", font=('Helvetica', 14))
        self.heading.pack(fill=tk.X, padx=40, pady=10)

        self.definition = ttk.Label(master=parentframe, wraplength=width - 10, font=('Helvetica', 12), justify='left',
                                    text="Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.")
        self.definition.pack(fill=tk.X, padx=40, pady=10)

        self.set_of_operations = tk.Frame(master=parentframe, padx=40, bg="#464646")

        self.node = ttk.Entry(master=self.set_of_operations,width=50)
        self.node.insert(0, "29,4,150,34,90,12,36,87,45")
        self.node.bind('<Button-1>', self.deletetext)

        self.output_frame = ttk.Frame(master=parentframe)

        self.output = tk.Canvas(master=self.output_frame, bg="#464646", bd=1, highlightthickness=1, highlightbackground="#d8d8d8",
                           relief=tk.FLAT, scrollregion=(0, 0, 100, 100))


        self.sort = ttk.Button(master=self.set_of_operations, text="SORT", command=lambda: self.sort_(self.output))

        self.instructor = voice_assistance.voice_assistant()
        self.allow_speaking = False
        self.voice_b = ttk.Button(master=self.set_of_operations, text="🔊 Guide",
                                  command=lambda: self.guide(self.output))

        self.node.pack(side=tk.LEFT, ipady=4, ipadx=4)
        self.sort.pack(side=tk.LEFT, padx=2)
        self.voice_b.pack(side=tk.LEFT, padx=2)
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



        x = (output.winfo_width()//2)-((len(numbers)*40)//2)
        x1 = x+((len(numbers)*40)//2)
        y = self.y +60

        self.start(self.rectangles,numbers,output,y,x,x1)

    def start(self,rectangles,numbers,output,y,x,x1):

        if len(numbers)>1:
            mid = len(numbers)//2
            left = numbers[:mid]
            right = numbers[mid:]

            sr = list(map(int, output.cget('scrollregion').split()))

            output['scrollregion'] = (sr[0],sr[1],sr[2],y+80)
            output.update()

            x2,x3,trl=self.draw(left, output,x-60, y)
            x4, x5, trr = self.draw(right, output, x1 + 60, y)

            self.start(trl,left,output, y + 60,x2,x3)


            self.start(trr,right, output,y+60, x4,x5)

            y+=60

            for v in range(len(left)+len(right)):
                output.itemconfig(rectangles[v][1],text="")
            output.update()


            i = 0
            j = 0
            k = 0

            while i<len(left) and j<len(right):
                self.animate(trl[i],trr[j],output)

                if left[i]<right[j]:
                    self.explain("{0} is less than {1}".format(left[i],right[j]))

                    numbers[k] = left[i]
                    output.itemconfig(rectangles[k][1],text=numbers[k])
                    output.update()
                    time.sleep(0.3)

                    i+=1
                    k+=1
                else:
                    self.explain("{0} is less than {1}".format(right[j],left[i]))


                    numbers[k] = right[j]
                    output.itemconfig(rectangles[k][1], text=numbers[k])
                    output.update()
                    time.sleep(0.3)

                    j += 1
                    k += 1
            if i<len(left):
                self.explain("Filling the array with remaining elements of left sub array")


            while i<len(left):
                self.animate(trl[i],None,output)

                numbers[k] = left[i]

                output.itemconfig(rectangles[k][1], text=numbers[k])
                output.update()
                time.sleep(0.3)

                k+=1
                i+=1
            if j < len(right):
                self.explain("Filling the array with remaining elements of right sub array")

            while j < len(right):
                self.animate(None,trr[j], output)

                numbers[k] = right[j]

                output.itemconfig(rectangles[k][1], text=numbers[k])
                output.update()
                time.sleep(0.3)

                k += 1
                j += 1

            for u in trl:
                output.delete(u[0])
                output.delete(u[1])
            for u in trr:
                output.delete(u[0])
                output.delete(u[1])
            output.update()
            time.sleep(0.3)

    def draw(self,arr,output,x,y):

        l = 0
        temp_rect =[]

        start_x = x
        for i in arr:
            rect = output.create_rectangle(x, y, x + 40, y + 40)
            text = output.create_text(x + 20, y + 20, text=str(i), fill="white")
            temp_rect.append([rect,text])
            x += 40
            l+=1
        l = l//2

        output.update()
        time.sleep(0.3)

        return start_x,start_x+(l*40),temp_rect


    def animate(self,obj1,obj2,output,color='#fb5581'):
        if obj1 is None and obj2 is not None:
            output.itemconfig(obj2[0], fill=color)
            output.itemconfig(obj2[1], fill="black")

            output.update()
            time.sleep(0.3)
            output.itemconfig(obj2[0], fill="")
            output.itemconfig(obj2[1], fill="white")
            output.update()
            time.sleep(0.3)

        elif obj2 is None and obj1 is not None:
            output.itemconfig(obj1[0],fill=color)
            output.itemconfig(obj1[1], fill="black")

            output.update()
            time.sleep(0.3)
            output.itemconfig(obj1[0], fill="")
            output.itemconfig(obj1[1], fill="white")
            output.update()
            time.sleep(0.3)
        else:
            output.itemconfig(obj1[0], fill=color)
            output.itemconfig(obj2[0], fill=color)
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

    def deletetext(self,event):
        event.widget.delete(0,"end")
        return None

    def explain(self,sentence):
        if self.allow_speaking:
            self.instructor.speak(sentence)

    def guide(self,output):
        v = self.allow_speaking
        self.allow_speaking = (not v)
        if self.allow_speaking:
            self.voice_b.config(text="🔊 On")

        else:
            self.voice_b.config(text="🔊 Off")





