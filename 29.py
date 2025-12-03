from tkinter import *

window = Tk()
window.title("Image on Canvas")
window.geometry("500x400")

canvas = Canvas(window, width=400, height=300, bg="white")
canvas.pack()

# ✅ Use raw string r"" OR forward slashes /
photo = PhotoImage(file=r"N:/my works/1000452671.png")

canvas.create_image(200, 150, image=photo)

window.mainloop()
