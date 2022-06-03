from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

sort = 0
try:
    words = pd.read_csv("data/words_to_learn.csv")
    english_words = words["English"].to_list()
    french_words = words["French"].to_list()
except FileNotFoundError:
    words = pd.read_csv("./data/french_words.csv")
    english_words = words["English"].to_list()
    french_words = words["French"].to_list()    

words_to_learn = {
    "English": [],
    "French": [],
}


def get_new_words_wrong():
    global sort 
    sort = random.randint(0, len(english_words) - 1)

    french_word = french_words[sort]

    canvas.itemconfig(card_bg, image= front_card_image)
    canvas.itemconfig(language_text, text= "French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")

    window.after(3000, swap_words)


def get_new_words_right():
    global sort
    

    english_words.remove(english_words[sort])
    french_words.remove(french_words[sort])

    words_to_learn["English"] = english_words
    words_to_learn["French"] = french_words

    words_to_learn_dataframe = pd.DataFrame(words_to_learn)

    words_to_learn_dataframe.to_csv("data/words_to_learn.csv", index= False)
    

    

    sort = random.randint(0, len(english_words))

    french_word = french_words[sort]

    canvas.itemconfig(card_bg, image= front_card_image)
    canvas.itemconfig(language_text, text= "French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")

    window.after(3000, swap_words)

def swap_words():
    english_word = english_words[sort]

    canvas.itemconfig(card_bg, image=back_card_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text= english_word, fill= "white")



#Window setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)




#Canvas setup
canvas = Canvas(width=800, height=526)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front_card_image)
language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font= ("Ariel", 60, "bold"))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

french_word = french_words[sort]

canvas.itemconfig(card_bg, image= front_card_image)
canvas.itemconfig(language_text, text= "French", fill="black")
canvas.itemconfig(word_text, text=french_word, fill="black")

window.after(3000, swap_words)

#Wrong button setup
wrong_image = PhotoImage(file= "./images/wrong.png")
wrong_button = Button(image= wrong_image, highlightthickness=0, command=get_new_words_wrong)
wrong_button.grid(row=1, column=0)


#Right button setup
right_image = PhotoImage(file= "./images/right.png")
right_button = Button(image= right_image, highlightthickness=0, command=get_new_words_right)
right_button.grid(row=1, column=1)




window.mainloop()


