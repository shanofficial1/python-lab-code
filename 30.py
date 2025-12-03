from tkinter import *

def save_resume():
    name = name_var.get()
    age = age_var.get()
    dob = dob_var.get()
    gender = gender_var.get()
    qualification = qual_text.get("1.0", END)
    address = addr_text.get("1.0", END)

    f = open("resume.doc", "w")
    f.write("RESUME\n")
    f.write("Name : " + name + "\n")
    f.write("Age : " + age + "\n")
    f.write("DOB : " + dob + "\n")
    f.write("Gender : " + gender + "\n")
    f.write("Qualification :\n" + qualification)
    f.write("Address :\n" + address)
    f.close()

    status_var.set("Resume saved")

window = Tk()
window.title("Resume")

name_var = StringVar()
age_var = StringVar()
dob_var = StringVar()
gender_var = StringVar()
status_var = StringVar()

Label(window, text="Name").grid(row=0, column=0)
Entry(window, textvariable=name_var).grid(row=0, column=1)

Label(window, text="Age").grid(row=1, column=0)
Entry(window, textvariable=age_var).grid(row=1, column=1)

Label(window, text="DOB").grid(row=2, column=0)
Entry(window, textvariable=dob_var).grid(row=2, column=1)

Label(window, text="Gender").grid(row=3, column=0)
Radiobutton(window, text="Male", variable=gender_var, value="Male").grid(row=3, column=1)
Radiobutton(window, text="Female", variable=gender_var, value="Female").grid(row=3, column=2)

Label(window, text="Qualification").grid(row=4, column=0)
qual_text = Text(window, height=3, width=20)
qual_text.grid(row=4, column=1)

Label(window, text="Address").grid(row=5, column=0)
addr_text = Text(window, height=3, width=20)
addr_text.grid(row=5, column=1)

Button(window, text="Save", command=save_resume).grid(row=6, column=1)

Label(window, textvariable=status_var).grid(row=7, column=1)

window.mainloop()
