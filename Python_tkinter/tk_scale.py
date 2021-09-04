import tkinter as tk


window = tk.Tk()
window.title('my window')
window.geometry('300x200')  # 窗口的大小

ll = tk.Label(window, bg='yellow', width=20, text='empty')
ll.pack()


def print_selection(v):
    ll.config(text='you have selected ' + v)


#定义尺度的相关属性:tickinterval--尺度，resolution--精确度
s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=1, tickinterval=3, resolution=0.01, command=print_selection)
s.pack()


window.mainloop()