import turtle
import pandas

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game.")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

score = 0
correctAnswers = []
missing_states = data["state"].to_list()

while score < 50:
    answer = screen.textinput(title=f" {score}/50 Guess the State", prompt="What's another state name?")

    if answer.title() == "Exit":
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states to learn.csv")
        break

    if len(data[data["state"] == answer.title()]) == 1:
        score += 1
        correctAnswers.append(answer)
        print("tem")
        print(correctAnswers)
        x = data[data["state"] == answer.title()]["x"].item()
        y = data[data["state"] == answer.title()]["y"].item()

        pen.goto(x, y)
        pen.write(answer.title())

        missing_states.remove(answer.title())
        print(missing_states)


