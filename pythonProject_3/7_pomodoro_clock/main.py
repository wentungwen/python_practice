from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    # reset time
    canvas.itemconfig(timer_text, text=f"0:00")
    # reset title label
    title.config(text="Timer")
    # reset check_marks
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)
        reps = 0
    elif reps % 2 == 0:
        title.config(text="Break", fg=GREEN)
        count_down(short_break_sec)
    else:
        title.config(text="work", fg=PINK)
        count_down(work_sec)
    print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1, count_down, count - 1)
    else:
        start_timer()
        mark_text = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark_text += "∆"
        check_marks.config(text=mark_text)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Promodoro")
window.config(pady=100, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# TEXT
start_btn = Button(text="start", command=start_timer, highlightthickness=0)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="reset", command=reset, highlightthickness=0)
reset_btn.grid(column=2, row=2)

# label
title = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)

check_marks = Label(font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=2)

window.mainloop()
