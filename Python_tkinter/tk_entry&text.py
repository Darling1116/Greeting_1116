import tkinter as tk


window = tk.Tk()
window.title('my window')
window.geometry('300x200')  # 窗口的大小

e = tk.Entry(window, show=None)
#若为输入密码，则：e = tk.Entry(window, show=’*‘)
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert('end', var)


b1 = tk.Button(window, text='insert point', width=12, height=1, command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', width=12, height=1, command=insert_end)
b2.pack()

t = tk.Text(window, width=20, height=6)  # 显示文本框
t.pack()

window.mainloop()  # window不断地循环