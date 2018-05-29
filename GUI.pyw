import tkinter as tk
import ffxiv_lottery as ff
from tkinter.messagebox import *

#ff.ffxiv_lottery(map)
root = tk.Tk()
root.wm_title("FFXIV lottery calculator")
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
    all_sel = []
    for row in GUI_map:
        for x in row:
            x["background"]="white"
    for i in range(3):
        for j in range(3):
            tmp= GUI_map[i][j].get()
            if tmp == '':
                pass
            elif int(tmp) >= 1 and int(tmp) <= 9:
                if int(tmp) not in all_sel:
                    map[i][j] = int(tmp)
                    all_sel.append(int(tmp))
                    counter += 1
                else:
                    showinfo(title="error", message="input not correct!")
                    return
    if counter == 4:
        plan = ff.ffxiv_lottery(map)
        max_key = list(plan.keys())[0]
        max_expecatation = plan[max_key]
        text=""
        for key in plan.keys():
            if(plan[key] > max_expecatation):
                max_expecatation = plan[key]
                max_key = key
            text += key
            text += ":%.2f"%plan[key]
            text += "\n"
        l1["text"] = text
        if max_key == "row1":
            GUI_map[0][0]["background"] = "yellow"
            GUI_map[0][1]["background"] = "yellow"
            GUI_map[0][2]["background"] = "yellow"
        elif max_key == "row2":
            GUI_map[1][0]["background"] = "yellow"
            GUI_map[1][1]["background"] = "yellow"
            GUI_map[1][2]["background"] = "yellow"
        elif max_key == "row3":
            GUI_map[2][0]["background"] = "yellow"
            GUI_map[2][1]["background"] = "yellow"
            GUI_map[2][2]["background"] = "yellow"
        elif max_key == "col1":
            GUI_map[0][0]["background"] = "yellow"
            GUI_map[1][0]["background"] = "yellow"
            GUI_map[2][0]["background"] = "yellow"
        elif max_key == "col2":
            GUI_map[0][1]["background"] = "yellow"
            GUI_map[1][1]["background"] = "yellow"
            GUI_map[2][1]["background"] = "yellow"
        elif max_key == "col3":
            GUI_map[0][2]["background"] = "yellow"
            GUI_map[1][2]["background"] = "yellow"
            GUI_map[2][2]["background"] = "yellow"
        elif max_key == "diag1":
            GUI_map[0][0]["background"] = "yellow"
            GUI_map[1][1]["background"] = "yellow"
            GUI_map[2][2]["background"] = "yellow"
        elif max_key == "diag2":
            GUI_map[0][2]["background"] = "yellow"
            GUI_map[1][1]["background"] = "yellow"
            GUI_map[2][0]["background"] = "yellow"
    else:
        showinfo(title="error", message="input not correct!")
        return 
b1 = tk.Button(root,text="submit",command=submit)
b1.grid(row=3, column=2)
menu = tk.Menu(root)
submenu = tk.Menu(menu)
def submenu_com():
    showinfo(title="Information", message="2018 by MP.\njust for learning Python and tkinter")
submenu.add_command(label="Information",command=submenu_com)
menu.add_cascade(label='About',menu=submenu)
root['menu'] = menu

root.mainloop()

