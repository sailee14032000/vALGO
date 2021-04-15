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
for k in range(len(l)):
    j = set(associationrule[i]).difference(set(l[k]))
    o = list(associationtable)

    if ((new_apriori2['subcount'][i] / associationtable_['subcount'][o.index(sorted(list(l[k])))]) * 100) > 70:
        print("association rule for")
        print(l[k], "=>", j)
        print("support")
        print((new_apriori2['subcount'][i] / associationtable_['subcount'][o.index(sorted(list(l[k])))]))

        print("confidence")
        print(((new_apriori2['subcount'][i] / associationtable_['subcount'][o.index(sorted(list(l[k])))])) * 100)
