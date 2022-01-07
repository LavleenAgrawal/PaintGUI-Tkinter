from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab


class Paint:
    def __init__(self):
        self.root = root
        self.root.title("Paint")
        self.root.geometry("900x620")
        self.root.configure(background='white')
        self.root.resizable(0, 0)
        self.tool, self.obj = None, None

        self.color_frame = LabelFrame(self.root,
                                      text='Text Colors',
                                      font=('times new roman', 12),
                                      bd=5,
                                      bg='white',
                                      relief=GROOVE)
        self.color_frame.place(x=3, y=0, width=100, height=200)

        colors = ['black', 'purple', 'dark green', 'brown', 'orange', 'magenta', 'azure',
                  'grey', 'dark blue', 'green', 'red', 'gold', 'hot pink', 'white',
                  'silver', 'blue', 'light green', 'salmon', 'yellow', 'pink', 'snow']
        i = 0
        j = 0
        for color in colors:
            Button(self.color_frame,
                   bg=color,
                   bd=1,
                   width=3,
                   anchor=CENTER,
                   relief=RAISED,
                   command=lambda col=color: self.select_color(col)).grid(row=i, column=j)
            i += 1
            if i == 7:
                i = 0
                j += 1

        self.penColor = 'black'
        self.eraser_color = 'white'

        self.eraserButton = Button(self.root,
                                   text='ERASER',
                                   bd=6,
                                   anchor=CENTER,
                                   width='8',
                                   relief=GROOVE,
                                   command=self.eraser)
        self.eraserButton.place(x=112, y=6)

        self.canvasColor_button = Button(self.root,
                                         text='CANVAS',
                                         bd=6,
                                         anchor=CENTER,
                                         width='8',
                                         relief=GROOVE,
                                         command=self.canvas_color)
        self.canvasColor_button.place(x=192, y=6)

        self.extra_frame = LabelFrame(self.root,
                                      text='Extra Widget',
                                      font=('Times new roman', 12),
                                      bd=5,
                                      bg='white',
                                      relief=GROOVE)
        self.extra_frame.place(x=3, y=208,
                               width=100, height=195)

        self.lineButton = Button(self.root,
                                 text='LINE',
                                 bd=6,
                                 anchor=CENTER,
                                 width='8',
                                 relief=GROOVE,
                                 command=self.line)
        self.lineButton.place(x=16, y=233)

        self.circleButton = Button(self.root,
                                   text='CIRCLE',
                                   bd=6,
                                   anchor=CENTER,
                                   width='8',
                                   relief=GROOVE,
                                   command=self.cir)
        self.circleButton.place(x=16, y=273)

        self.triButton = Button(self.root,
                                text='TRIANGLE',
                                bd=6,
                                anchor=CENTER,
                                width='8',
                                relief=GROOVE,
                                command=self.tri)
        self.triButton.place(x=16, y=313)

        self.sqButton = Button(self.root,
                               text='SQUARE',
                               bd=6,
                               anchor=CENTER,
                               width='8',
                               relief=GROOVE,
                               command=self.rect)
        self.sqButton.place(x=16, y=353)

        self.clearButton = Button(self.root,
                                  text='CLEAR',
                                  bd=6,
                                  anchor=CENTER,
                                  width='8',
                                  relief=GROOVE,
                                  command=lambda: self.canvas.delete("all"))
        self.clearButton.place(x=732, y=6)

        self.saveButton = Button(self.root,
                                 text='SAVE',
                                 bd=6,
                                 anchor=CENTER,
                                 width='8',
                                 relief=GROOVE,
                                 command=self.save_paint)
        self.saveButton.place(x=812, y=6)

        self.penSize_frame = LabelFrame(self.root,
                                        text='Change Size',
                                        font=('Times new roman', 12),
                                        bd=5,
                                        bg='white',
                                        relief=GROOVE)
        self.penSize_frame.place(x=3, y=414,
                                 width=100, height=195)
        self.penSize = Scale(self.penSize_frame, orient=VERTICAL, from_=50, to=0, length=165)
        self.penSize.set(1)
        self.penSize.grid(row=0, column=1, padx=30)

        self.canvas = Canvas(self.root,
                             bg='white',
                             bd=5,
                             relief=GROOVE,
                             height=550, width=765)
        self.canvas.place(x=110, y=45)

        self.canvas.bind('<B1-Motion>', self.paint)

        # self.canvas.bind('<Button-1>', self.line)

    def line(self):
        self.canvas.create_line(100, 200, 400, 200, fill=self.penColor)

    def cir(self):
        self.canvas.create_oval(100, 200, 200, 100, fill=self.penColor)

    def tri(self):
        self.canvas.create_line(50, 100, 150, 100, fill=self.penColor)
        self.canvas.create_line(50, 100, 100, 50, fill=self.penColor)
        self.canvas.create_line(100, 50, 150, 100, fill=self.penColor)

    def rect(self):
        self.canvas.create_rectangle(150, 350, 350, 150, fill=self.penColor)

    def paint(self, event):
        x1, y1 = (event.x-2), (event.y-2)
        x2, y2 = (event.x+2), (event.y+2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.penColor, outline=self.penColor, width=self.penSize.get())

    def select_color(self, col):
        self.penColor = col

    def canvas_color(self):
        color = colorchooser.askcolor()
        self.canvas.configure(background=color[1])
        self.eraser_color = color[1]

    def eraser(self):
        self.penColor = self.eraser_color

    def save_paint(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=',jpg')
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
            messagebox.showinfo('paint says ', 'image is saved as ' + str(filename))
        except:
            messagebox.showerror('not saved')


if __name__ == '__main__':
    root = Tk()
    p = Paint()
    root.mainloop()
