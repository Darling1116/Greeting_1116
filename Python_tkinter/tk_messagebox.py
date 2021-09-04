import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('300x200')  # 窗口的大小


def hit_me():
    #tk.messagebox.showinfo(title='Hi', message='hahahhahha')
    #tk.messagebox.showwarning(title='Hi', message='nonononono')
    #tk.messagebox.showerror(title='Hi', message='No!!!never!!!')

    print(tk.messagebox.askquestion(title='Hi', message='hahahahaha'))  # return 'yes' or 'no'
    #print(tk.messagebox.askyesno(title='Hi', message='nonononono'))  # return True or False
    #print(tk.messagebox.asktrycancel(title='Hi', message='nonononono'))  # return True or False
    #print(tk.messagebox.askokcancel(title='Hi', message='nonononono'))  # return True or False


tk.Button(window, text='hit me!', command=hit_me).pack()


window.mainloop()