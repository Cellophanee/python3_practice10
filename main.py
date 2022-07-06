from tkinter import *
from tkinter import colorchooser
import tkinter.font as tkFont
text_color = 'blue'
def Triangle():
    Clear()
    frame.canvas.itemconfig(t, fill='#00d0ff', outline='black')
    frame.canvas.coords(t, (50, 200, 340, 200, 110, 60))
    text.insert(1.0, 'Зображення трикутника')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', 16), foreground=text_color, justify=CENTER)
def Rectangle():
    Clear()
    frame.canvas.itemconfig(r, fill='blue', outline='black')
    frame.canvas.coords(r, (80, 50, 320, 200))
    text.insert(1.0, 'Зображення прямокутника')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', 16), foreground=text_color, justify=CENTER)
def Circle():
    Clear()
    frame.canvas.itemconfig(c, fill='#ff29f4', outline='black')
    frame.canvas.coords(c,(125, 125, 250, 250))
    text.insert(1.0, 'Зображення кола')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', 16), foreground=text_color, justify=CENTER)
def Square():
    Clear()
    frame.canvas.itemconfig(s, fill='#07db00', outline='black')
    frame.canvas.coords(s, (125, 125, 250, 250))
    text.insert(1.0, 'Зображення квадрата')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', 16), foreground=text_color, justify=CENTER)
def Clear():
    frame.canvas.coords(t, (0, 0, 0, 0, 0, 0) )
    frame.canvas.coords(c, (0, 0, 0, 0))
    frame.canvas.coords(r, (0, 0, 0, 0))
    frame.canvas.coords(s, (0, 0, 0, 0))
    text.delete(1.0, END)
def increase_font():
    fontsize = fontStyle['size']
    text.tag_config('title', font=('Times', fontsize+1), foreground=text_color, justify=CENTER)
    fontStyle.configure(size=fontsize-2)
def decrease_font():
    fontsize = fontStyle['size']
    text.tag_config('title', font=('Times', fontsize-1), foreground=text_color, justify=CENTER)
    fontStyle.configure(size=fontsize-2)
class Color(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.color_btn = pictureMenu.add_command(label='Колір фігури', command=self.ChooseColor)
        self.color_btn = pictureMenu.add_command(label='Колір фону', command=self.ChooseBgColor)
        self.size_btn = pictureMenu.add_command(label='Розмір фігури', command=self.ChooseSize)
        self.font_btn = settingsMenu.add_command(label='Налаштування тексту', command=self.TextStyle)
        self.canvas = Canvas(width=400, height=400, bg='#fff')
    def ChooseColor(self):
        (rgb, hx) = colorchooser.askcolor()
        self.canvas.itemconfig(t, fill=hx, outline='black')
        self.canvas.itemconfig(c, fill=hx, outline='black')
        self.canvas.itemconfig(r, fill=hx, outline='black')
        self.canvas.itemconfig(s, fill=hx, outline='black')
    def ChooseBgColor(self):
        (rgb, hx) = colorchooser.askcolor()
        self.canvas.config(bg=hx)
    def ChooseSize(self):
        (rgb, hx) = colorchooser.askcolor()
    def TextStyle(self):
        Window().mainloop()
class Window(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.initUI()
    def initUI(self):
        color = Button(self, text="Color", width=30,
        command=self.ChooseColor)
        increase = Button(self, text="Increase", width=30,
        command=increase_font)
        decrease = Button(self, text="Decrease", width=30,
        command=decrease_font)
        increase.pack(side=LEFT)
        decrease.pack(side=RIGHT)
        color.pack(side=BOTTOM)
    def ChooseColor(self):
        (rgb, hx) = colorchooser.askcolor()
        text_color = hx
        text.tag_config('title', foreground=text_color)
win = Tk()
win.title('Модифікований приклад 3')
mainMenu = Menu(win)
win.config(menu=mainMenu)
settingsMenu = Menu(mainMenu, tearoff=0)
pictureMenu = Menu(settingsMenu, tearoff=0)
mainMenu.add_cascade(label="Налаштування", menu=settingsMenu)
settingsMenu.add_cascade(label="Налаштування зображень", menu=pictureMenu)
fontStyle = tkFont.Font(family="LucidaGrande", size=16)
print(fontStyle['size'])
frame = Color(win)
b_triangle = Button(text="Трикутник", width=20, command=Triangle)
b_rectangle = Button(text="Прямокутник", width=20, command=Rectangle)
b_circle = Button(text="Коло", width=20, command=Circle)
b_square = Button(text="Квадрат", width=20, command=Square)
b_clear = Button(text="Очистити", width=20, command=Clear)
text = Text(width=55, height=5, bg='#fff', wrap=WORD)
t = frame.canvas.create_polygon(0, 0, 0, 0, 0, 0)
c = frame.canvas.create_oval(0, 0, 0, 0)
r = frame.canvas.create_rectangle(0, 0, 0, 0)
s = frame.canvas.create_rectangle(0, 0, 0, 0)
b_triangle.grid(row=0, column=0, ipady=5, padx=45)
b_rectangle.grid(row=1, column=0, ipady=5, padx=45)
b_circle.grid(row=2, column=0, ipady=5, padx=45)
b_square.grid(row=3, column=0, ipady=5, padx=45)
b_clear.grid(row=4, column=0, ipady=5, padx=45)
frame.canvas.grid(row=0, column=1, rowspan=10)
text.grid(row=11, column=1, rowspan=2)
win.mainloop()