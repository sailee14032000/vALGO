import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import time
import footer
import voice_assistance

class insertionsort_contents(object):

    def __init__(self,ancestorpage,parentframe,width,height):
        self.back = ttk.Button(master=parentframe, text="← Back", command=lambda: self.raise_frame(ancestorpage))
        self.back.pack(anchor="w", padx=40, pady=20)

        self.x = 20
        self.y = 0

        self.heading = ttk.Label(master=parentframe, text="Insertion Sort", font=('Helvetica', 14))
        self.heading.pack(fill=tk.X, padx=40, pady=10)

        self.definition = ttk.Label(master=parentframe, wraplength=width - 10, font=('Helvetica', 12), justify='left',
                                    text="Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.")
        self.definition.pack(fill=tk.X, padx=40, pady=10)

        self.set_of_operations = tk.Frame(master=parentframe, padx=40, bg="#464646")

        self.node = ttk.Entry(master=self.set_of_operations,width=50)
        self.node.insert(0, "29,4,150,34,90,12,36,87,45")
        self.output_frame = ttk.Frame(master=parentframe)

        self.output = tk.Canvas(master=self.output_frame, bg="#464646", bd=1, highlightthickness=1, highlightbackground="#d8d8d8",
                           relief=tk.FLAT, scrollregion=(0, 0, 100, 100))

        self.sort = ttk.Button(master=self.set_of_operations, text="SORT", command=lambda: self.sort_(self.output))

        self.instructor = voice_assistance.voice_assistant()
        self.allow_speaking = False
        self.voice_b = ttk.Button(master=self.set_of_operations, text="🔊 Guide",
                                  command=lambda: self.guide(self.output))
        self.allow_execution = True


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
        output['scrollregion'] = (0,0,0,0)

        input = self.node.get()
        if input == "" or input == "Enter node value":
            msg.showwarning(title="No Input", message="Please enter input")
            return
        numbers = list(map(int, input.strip().split(',')))
        max_ = max(numbers)
        self.y = max_ + 40
        for i in numbers:
            rect = output.create_rectangle(self.x, self.y, self.x + 40, self.y - i)
            text = output.create_text(self.x + 20, self.y + 10, text=str(i),fill="white")
            self.x += 50
            self.rectangles.append([rect, text])
        time.sleep(0.3)
        n = len(numbers)

        sr = list(map(int, output.cget('scrollregion').split()))
        if max_+120>int(output['height']):
            sr[3] = max_ + 120
        output['scrollregion'] = (sr[0],sr[1],sr[0]+ n*(50)+50,sr[3])
        output.yview_moveto(1)
        output.update()
        sr = list(map(int, output.cget('scrollregion').split()))

        output.itemconfig(self.rectangles[0][0], fill="#3be13b")

        for i in range(1,n):
            current = numbers[i]
            current_rect = self.rectangles[i]
            j = i-1

            x,y,x1,y1 = output.coords(current_rect[0])
            output.coords(current_rect[0],x,self.y+20,x+40,self.y+60)
            output.move(current_rect[0],0,0)
            output.itemconfig(current_rect[0], fill="#fb5581")
            output.itemconfig(current_rect[1], fill="black")

            tx, ty = output.coords(current_rect[1])
            output.coords(current_rect[1], tx,ty+30)

            output.update()
            time.sleep(0.3)

            while j>=0 and current<numbers[j]:
                self.explain("{0} is less than {1} Hence swapping ".format(current,numbers[j]))
                output.move(current_rect[1],-50,0)
                output.move(current_rect[0], -50, 0)

                output.move(self.rectangles[j][1], 50, 0)
                output.move(self.rectangles[j][0], 50, 0)
                output.update()
                time.sleep(0.4)

                self.rectangles[j + 1] = self.rectangles[j]
                numbers[j+1] = numbers[j]
                j-=1

            x2, y2, x4, y4 = output.coords(current_rect[0])

            output.coords(current_rect[0],x2,y,x4,y1)
            tx1, ty1 = output.coords(current_rect[1])

            output.coords(current_rect[1], tx1,ty)

            output.itemconfig(current_rect[0],fill="#3be13b")
            output.itemconfig(current_rect[1],fill="white")


            output.update()

            self.rectangles[j+1] = current_rect
            numbers[j+1] = current
            time.sleep(0.3)


    def raise_frame(self,ancestorpage):
        ancestorpage.tkraise()

    def deletetext(self, event):
        event.widget.delete(0, "end")
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

