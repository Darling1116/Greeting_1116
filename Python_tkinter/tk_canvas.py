import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x450')  # 窗口的大小

canvas = tk.Canvas(window, bg='blue', height=400, width=330)
image_file = tk.PhotoImage(file='D:/Workspaces/save/1.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)

x0, y0, x1, y1 = 200, 200, 260, 260
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  # 添加圆形
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180, fill='yellow')  # 添加扇形
rect = canvas.create_rectangle(160, 160, 260, 260, fill='gray')  # 添加矩形
canvas.pack()


def moveit():
    canvas.move(rect, 0, 8)

b = tk.Button(window, text='move gray rectangle', command=moveit).pack()



window.mainloop()