# US_States Game: Two screens pop up in your window after running this code, one is the blank map of US and the second one is the input widow bar, where you have to guess US states until you exit the input window bar by using "exit" keyword. When you are guessing US states then these states will show in the empty map screen.

import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S_States Game")

img_url = "blank_states_img.gif"
screen.addshape(img_url)
turtle.shape(img_url)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
# print(states_list)


guessed_states = []
while len(guessed_states)<50:
    input_state = screen.textinput(title=f"{len(guessed_states)}/50-U.S states", prompt="Enter any U.S state name")

    if input_state == "exit":
        # remaining_states = []
        # for state in states_list:
        #     if state not in guessed_states:
        #         remaining_states.append(state)
        # using list comprehension
        remaining_states =[state for state in states_list if state not in guessed_states]
        new_file = pandas.DataFrame(remaining_states, columns=["Remaining_States"])
        new_file.to_csv("remainig_states.csv")
        # print(remaining_states)
        break

    if input_state in states_list:
        guessed_states.append(input_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row_data = data[data["state"] == input_state]
        # print(result)
        t.goto(int(state_row_data['x']), int(state_row_data['y']))
        t.write(input_state)


screen.exitonclick()