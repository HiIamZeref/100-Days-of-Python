from flask import Flask
from random import randint
app = Flask(__name__)

sort = randint(0,9)


@app.route("/")
def game_start():
    string = '<h1>Guess a number between 0 and 9</h1> <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
    return string 
            




@app.route("/<number>")
def result(number):
    global sort
    integer = int(number)
    if integer == sort:
        return '<h1 style="color: green;">You found me! Congrats!</h1> <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"</img>'
    elif integer < sort:
        return '<h1 style="color: red;">Too low! Try again!</h1> <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"</img>'
    elif integer > sort:
        return '<h1 style="color: purple;">Too high! Try again!</h1> <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"</img>'
    


if __name__ == "__main__":
    app.run(debug= True)

