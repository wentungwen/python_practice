from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    pyperclip.paste()


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(message="No empty string!")
    else:
        is_save_ok = messagebox.askokcancel(title=website,
                                            message=f"Details: \nEmail:{email}\nPassword: {password}\nIs it ok to save?")
        if is_save_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password generator")
window.config(padx=20, pady=20, bg="white")

# logo
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0, )

# text
website_text = Label(text="website: ", font=(FONT_NAME, 12), fg="black", bg="white")
website_text.grid(column=0, row=1)
password_text = Label(text="password: ", font=(FONT_NAME, 12), fg="black", bg="white")
password_text.grid(column=0, row=3)
email_text = Label(text="email/username: ", font=(FONT_NAME, 12), fg="black", bg="white")
email_text.grid(column=0, row=2)

# entry
email_entry = Entry(width=35, fg="black", bg="white", highlightthickness=1)
email_entry.grid(column=1, row=2, columnspan=2, pady=10)
email_entry.insert(0, "wentung@gmail.com")
password_entry = Entry(width=21, fg="black", bg="white", highlightthickness=1)
password_entry.grid(column=1, row=3)
website_entry = Entry(width=35, fg="black", bg="white", highlightthickness=1)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# button
generate_btn = Button(text="Generate!", highlightthickness=0, command=generate_password)
generate_btn.grid(column=2, row=3)
add_btn = Button(text="Add to notebook", width=35, highlightthickness=0, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
