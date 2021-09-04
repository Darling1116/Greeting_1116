import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x200')  # 窗口的大小

ll = tk.Label(window, bg='yellow', width=30, height=2, text='empty')
ll.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()


def print_selection():
    if(var1.get() == 1) & (var2.get() == 0):
        ll.config(text='I love only Python ')
    elif(var1.get() == 0) & (var2.get() == 1):
        ll.config(text='I love only C++ ')
    elif(var1.get() == 1) & (var2.get() == 1):
        ll.config(text='I love both ')
    else:
        ll.config(text='I do not love either ')


c1 = tk.Checkbutton(window, text='Python', variable=var1,
                    onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable=var2,
                    onvalue=1, offvalue=0, command=print_selection)
c2.pack()


window.mainloop()