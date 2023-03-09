import tkinter as tk
FONT = ("Times New Roman", 20)

window = tk.Tk()
window.title("It is a GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)



def button_clicked():
    km_output["text"] = 0
    num = float(mile_input.get())
    num *= 1.60934
    km_output["text"] = round(num, 2)

# button
button = tk.Button(text="calculate", command=button_clicked)
button.grid(column=2, row=3)

# label
lb_mile = tk.Label(text="mile", font=FONT)
lb_mile.grid(column=4, row=1)
lb_km = tk.Label(text="km", font=FONT)
lb_km.grid(column=4, row=2)
lb_equal = tk.Label(text="is equal to", font=FONT)
lb_equal.grid(column=1, row=2)

# input and output
mile_input = tk.Entry(width=10)
mile_input.grid(column=2, row=1)
km_output = tk.Label(text="", font=FONT)
km_output.grid(column=2, row=2)

window.mainloop()


