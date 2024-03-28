from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data\\words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data\\french_words.csv")

data_dict = data.to_dict(orient="records")
current_card = {}


def know_card():
    data_dict.remove(current_card)
    data_to_learn = pd.DataFrame(data_dict)
    data_to_learn.to_csv("data\\words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    timer = window.after(3000, flip_card)


def flip_card():
    global timer
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images\\card_front.png")
card_back_image = PhotoImage(file="images\\card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
right_image = PhotoImage(file="images\\right.png")
known_button = Button(image=right_image, highlightthickness=0, command=know_card)
known_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images\\wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)


window.mainloop()


