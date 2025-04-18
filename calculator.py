import tkinter as tk
from tkinter import font
def button_click(char):
    current=display.get()
    if char=='c':
        display.delete(0, tk.END)
    elif char=='=':
        try:
            result=eval(current)
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, char)
        
root=tk.Tk()
root.title("Calculator")         
root.resizable(False, False)
display_font=font.Font(size=20)
display=tk.Entry(root, width=16, font=display_font,borderwidth=4, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons=[
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('c',5,0)
]
button_font=font.Font(size=15)
for (text, row, col) in buttons:
    button=tk.Button(root, text=text, font=button_font, command=lambda t=text: button_click(t), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
root.mainloop()
