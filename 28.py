from tkinter import *

# Create window
window = Tk()
window.title("Arithmetic Operations")
window.geometry("350x300")

# Functions
def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    if float(num2.get()) != 0:
        result.set(float(num1.get()) / float(num2.get()))
    else:
        result.set("Error")

# Labels
Label(window, text="Enter First Number").pack()
num1 = StringVar()
Entry(window, textvariable=num1).pack()

Label(window, text="Enter Second Number").pack()
num2 = StringVar()
Entry(window, textvariable=num2).pack()

# Buttons
Button(window, text="Sum", command=add).pack(pady=5)
Button(window, text="Difference", command=subtract).pack(pady=5)
Button(window, text="Product", command=multiply).pack(pady=5)
Button(window, text="Quotient", command=divide).pack(pady=5)

# Result
Label(window, text="Result").pack()
result = StringVar()
Entry(window, textvariable=result).pack()

# Run window
window.mainloop()
