from tkinter import *
import pandas
import random
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
current_card = {}

try:
    data = pandas.read_csv("data/need_practice.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/dutch_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- Create Flash Cards ------------------------------- #
def show_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(card_title, text="Dutch", fill="black")
    canvas.itemconfig(card_word, text=current_card["Dutch"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/need_practice.csv", index=False)
    show_next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("flash card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(3000, flip_card)

# card
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# label
card_title = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=(FONT, 50, "bold"), fill="black")

# button
right_btn_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, border=0, command=is_known)
right_btn.grid(column=0, row=2)
wrong_btn_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, border=0, command=show_next_card)
wrong_btn.grid(column=1, row=2)

show_next_card()

window.mainloop()
