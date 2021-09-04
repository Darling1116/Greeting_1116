import tkinter as tk


window = tk.Tk()
window.title('my window')
window.geometry('300x200')  # 窗口的大小

var1 = tk.StringVar()
ll = tk.Label(window, bg='yellow', width=4, textvariable=var1)
ll.pack()


def print_selection():
    value = lb.get(lb.curselection())  # 选择光标选中的内容
    var1.set(value)


b1 = tk.Button(window, text='print selection', width=12, height=1, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lb = tk.Listbox(window, listvariable=var2)

list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()