from tkinter import *
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from tkinter import filedialog

window = Tk()
filename = filedialog.askopenfilename()
if 'xlsx' in filename:
    dff = pd.read_excel(filename,sheet_name='score')
elif 'csv' in filename:
    dff = pd.read_csv(filename)

def do():


    fig, axes = plt.subplots(16,1, figsize=(20, 20), sharex=True,sharey=True)

    checked_items = []
    for i, var in enumerate(check_vars):
        if var.get():  # If the checkbutton is selected (True)
            checked_items.append(items[i])  # Add the corresponding item to the list

    for i,j in enumerate(checked_items):
        sb.lineplot(ax = axes[i], x=dff[selected_option.get()], y= dff[j])
    plt.tight_layout()

    plt.yticks(rotation=45)
    plt.show()

items = [i for i in dff.columns]
selected_option = StringVar()
options = [i for i in dff.columns]
o = OptionMenu(window, selected_option, *options)
o.pack()
check_vars = []
for i in dff.columns:
    var = IntVar()
    check_vars.append(var)
    y = Checkbutton(window, text=i,variable=var, onvalue=1, offvalue=0)
    y.pack(anchor=W)
Button(window,text='CLICK',command=do,bg='RED').pack(fill='x')
window.mainloop()