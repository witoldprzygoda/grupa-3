import tkinter as tk
from tkinter import StringVar, Button, Entry
import tkinter.font as font

okno = tk.Tk()
okno.title("Calculator")

myFont = font.Font(family='Arial', size=20, weight='bold')

ans_entry =  Entry(okno, bd=5, width=20, font=myFont, bg="gray", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)


# przykładowy pierwszy Button 
btn_1 = Button(okno, text="1", padx=20, pady=10)
btn_1['font'] = myFont
btn_1.grid(row=1, column=0)



# proponuje dopisywac do slownika trzy elementy:
# num_1, num_2, oper wraz z wartościami
equation = {} 


def mouse_button_release(event):
    widg = event.widget
    text = widg.cget("text")

    if text in "0123456789":
        ans_entry.insert(len(ans_entry.get()), text)

    if text in "+-*/":
        pass

    if text == "C":
        pass

    if text == "=":
        # jakieś obliczenia
        pass

        

# sposób na reakcję 
okno.bind("<ButtonRelease-1>", mouse_button_release)

okno.mainloop()
