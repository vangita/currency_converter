import tkinter as tk
from dbm import error
from tkinter import ttk

root = tk.Tk()

root.title("Valute Exchange")
root.configure(background='light blue')
root.geometry("800x600+400+150")

currencies= ["USD","GEL","RUPEE"]

first_currency = tk.Label(root, text="From:")
first_currency.grid(row=0,column=0)

lst = ttk.Combobox(root, values=currencies, state="readonly")
lst.grid(row=0,column=1)

second_currency= tk.Label(root, text="To:")
second_currency.grid(row=1,column=0)

lst1 = ttk.Combobox(root, values=["USD","GEL","RUPEE"], state="readonly")
lst1.grid(row=1,column=1)

amount_text1= tk.Label(root, text="Amount")
amount_text1.grid(row=2,column=0)

amount_text2= tk.Label(root, text="Converted Amount")
amount_text2.grid(row=3,column=0)

amount1= tk.Entry(root)
amount1.grid(row=2,column=1)

amount2= tk.Entry(root)
amount2.grid(row=3,column=1)

def converter():
    amount2.delete(0,tk.END)
    value1 = lst.get()
    value2 = lst1.get()
    dct= {"USD/GEL":2.69,"GEL/USD":0.37,"GEL/RUPEE":31.21,"RUPEE/GEL":0.032,"USD/RUPEE":83.96,"RUPEE/USD":0.012}
    x=value1+"/"+value2
    if x not in dct:
        raise error
    amount2.insert(0, dct[x]*float(amount1.get()))
    return


def clear():
    amount1.delete(0, tk.END)
    amount2.delete(0, tk.END)
    lst.set('')
    lst1.set('')
button = tk.Button(root, text="Convert",command=converter)
button.grid(row=4,column=0)

clear_button = tk.Button(root, text="Clear",command=clear)
clear_button.grid(row=4,column=1)




root.mainloop()