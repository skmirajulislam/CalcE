import tkinter as tk
from tkinter import ttk
import numpy as np
from mpmath import factorial


def click(val):
    e = entry.get()
    ans = " "

    try:
        if val == "C":
            e = e[0:len(e) - 1]
            entry.delete(0, "end")
            entry.insert(0, e)
            return
        elif val == "CE":
            entry.delete(0, "end")
        elif val == "=":
            ans = eval(e)
        elif val == "√":
            ans = np.sqrt(eval(e))
        elif val == "π":
            ans = np.pi
        elif val == "cosθ":
            ans = np.cos(np.radians(eval(e)))
        elif val == "sinθ":
            ans = np.sin(np.radians(eval(e)))
        elif val == "tanθ":
            ans = np.tan(np.radians(eval(e)))
        elif val == "2π":
            ans = 2 * np.pi
        elif val == "cosh":
            ans = np.cosh(eval(e))
        elif val == "sinh":
            ans = np.sinh(eval(e))
        elif val == "tanh":
            ans = np.tanh(eval(e))
       # ..
        elif val == chr(8731):
            ans = np.cbrt(eval(e))
       # ...
        elif val == "x\u02b8":
            entry.insert("end", "**")
            return
        elif val == "x\u00B3":
            ans = eval(e) ** 3
        elif val == "x\u00B2":
            ans = eval(e) ** 2
        elif val == "ln":
            ans = np.log(eval(e))
        elif val == "deg":
            ans = np.degrees(eval(e))
        elif val == "rad":
            ans = np.radians(eval(e))
        elif val == "e":
            ans = np.e
        elif val == "log10":
            ans = np.log10(eval(e))
        elif val == "x!":
            ans = factorial(eval(e))
        elif val == chr(247):
            entry.insert("end", "/")
            return
        else:
            entry.insert("end", val)
            return

        entry.delete(0, "end")
        entry.insert(0, ans)

    except (ZeroDivisionError, ValueError, OverflowError, ArithmeticError) as e:
        entry.delete(0, "end")
        entry.insert(0, "Error: " + str(e))
    except (SyntaxError, TypeError):
        entry.delete(0, "end")
        entry.insert(0, "Syntax Error..!")


root = tk.Tk()
root.title("SciCalc")
root.maxsize(790, 390)
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="SK MIRAJ")
tab_control.pack(expand=1, fill="both")

entry = tk.Entry(tab1, font=("Arial", 20, "bold"), bg="#ecf0f1",
                 fg="#2c3e50", bd=3, width=60, relief='sunken')

entry.grid(row=0, column=0, columnspan=8)

button_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ", "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
               "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", "7", "8", "9", chr(247), "ln", "deg",
               "rad", "e", "0", ".", "%", "=", "log10", "(", ")", "x!"]
r = 1
c = 0

for i in button_list:
    button = tk.Button(tab1, width=5, height=2, bd=2, text=i, bg="#ecf0f1", fg="#2c3e50",
                       font=("Arial", 18, "bold"), command=lambda button=i: click(button))
    button.grid(row=r, column=c, pady=1)
    c += 1
    if c > 7:
        r += 1
        c = 0

root.mainloop()
