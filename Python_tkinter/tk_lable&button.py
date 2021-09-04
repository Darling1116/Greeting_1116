import tkinter as tk


window = tk.Tk()
window.title('my window')
window.geometry('300x200')  # 窗口的大小

#添加标签
#ll = tk.Label(window, text='OMG! this is tk! ', bg='green', font=('Arial', 12), width=20, height=2)
var = tk.StringVar()
ll = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=18, height=2)
ll.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

#添加按钮，并定义按钮相关动作
b = tk.Button(window, text='hit me', width=12, height=1, command=hit_me)
b.pack()

window.mainloop()  # window不断地循环


