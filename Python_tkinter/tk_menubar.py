import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x200')  # 窗口的大小

ll = tk.Label(window, bg='yellow', width=30, height=2, text='')
ll.pack()

counter = 0
def do_job():
    global counter
    ll.config(text='do' + str(counter))
    counter += 1


menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()  # 添加分离行
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label='Submenul', command=do_job)

#config为改变参数的函数
window.config(menu=menubar)  # 把menu显示到窗口上



window.mainloop()