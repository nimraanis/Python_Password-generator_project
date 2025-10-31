# Importing Libraries
from tkinter import *
import random, string, pyperclip
import os

# Initialize window
root = Tk()
root.geometry("550x550")
root.resizable(0, 0)
root.title("MIMMI - PASSWORD GENERATOR")

# Try loading background image safely
image_path = r"C:\Users\NIMRA ANIS\Downloads\one.png"
if os.path.exists(image_path):
    img = PhotoImage(file=image_path)
    label = Label(root, image=img)
    label.place(x=0, y=0)
else:
    print("⚠️ Image not found, continuing without background.")

# Heading
Label(root, text='PASSWORD GENERATOR', font=('Times', 24, 'bold')).pack()
Label(root, text='BY MIMMI', font=('Times', 18, 'bold')).pack()
Label(root, text='M I M M I', font=('Times', 22)).pack(side=BOTTOM)

# Password length selection
Label(root, text='PASSWORD LENGTH', font=('Times', 14)).pack()
pass_len = IntVar(value=8)
Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

# Password variable
pass_str = StringVar()

# Password generator function
def Generator():
    length = pass_len.get()
    if length < 4:
        pass_str.set("Min length 4")
        return
    password = (
        random.choice(string.ascii_uppercase)
        + random.choice(string.ascii_lowercase)
        + random.choice(string.digits)
        + random.choice(string.punctuation)
    )
    password += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation)
                        for _ in range(length - 4))
    pass_str.set(password)

# Buttons
Button(root, text="GENERATE PASSWORD", command=Generator, font=('Times', 12)).pack(pady=19)
Entry(root, textvariable=pass_str, width=35).pack()

# Copy function
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text='COPY TO CLIPBOARD', command=Copy_password, font=('Times', 12)).pack(pady=19)

# Run the main loop
root.mainloop()
