import tkinter as tk
import ffxiv_lottery as ff
from tkinter.messagebox import *

#ff.ffxiv_lottery(map)
root = tk.Tk()
root.wm_title("FFXIV lottery calculator by MP")
root.wm_iconbitmap("ffxiv.ico")
#root.geometry('200x300')
GUI_map = []
for i in range(3):
    GUI_row=[]
    for j in range(3):
        GUI_row.append(tk.Entry(root))
        GUI_row[j].grid(row=i, column=j)
    GUI_map.append(GUI_row)
l1 = tk.Label(root,text='')
l1.grid(row=5, columnspan=8)
def submit():
    map=[[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
    counter = 0
    for i in range(3):
        for j in range(3):
            tmp= GUI_map[i][j].get()
            if tmp == '':
                pass
            elif int(tmp) >= 1 and int(tmp) <= 9:
                map[i][j] = int(tmp)
                counter += 1
    if counter == 4:
        l1["text"] = ff.ffxiv_lottery(map)
    else:
        showinfo(title="error",message="input numbers not correct!")    
b1 = tk.Button(root,text="submit",command=submit)
b1.grid(row=3, column=2)
menu = tk.Menu(root)
submenu = tk.Menu(menu)
submenu.add_command(label="test")
menu.add_cascade(label='about',menu=submenu)
root['menu'] = menu

root.mainloop()

