import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Games ')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.color('black')
pen.penup()

states_data = pandas.read_csv('50_states.csv')
states_name_list = states_data['state'].to_list()
correct_answers = []
states_to_learn = states_data['state'].to_list()

while len(correct_answers) <= 50:
    title_str = f'Guess the State Name - Correct answers: {len(correct_answers)}/50'
    answer_state = screen.textinput(title=title_str, prompt="What's another state's name?")
    print(answer_state)
    answer_title = answer_state.title()
    if answer_title == 'Exit':
        break
    if (answer_title in states_name_list) and (not answer_title in correct_answers):
        print('ok')
        print(states_data[states_data.state == answer_title])
        x_coor = int(states_data[states_data.state == answer_title]['x'])
        y_coor = int(states_data[states_data.state == answer_title]['y'])

        print(type(states_data[states_data.state == answer_title]))
        pen.goto(x_coor, y_coor)
        pen.write(answer_title)
        correct_answers.append(answer_title)
        states_to_learn.remove(answer_title)
    else:
        pass
        print('not ok')

df_states_to_learn = pandas.DataFrame(states_to_learn)
df_states_to_learn.to_csv('states_to_learn.csv')

# with open('states_to_learn.csv', 'a') as to_learn:
#     for state in states_to_learn:
#         # state = f'\n{state}'
#         to_learn.write('\n' + state)

turtle.mainloop()

screen.exitonclick()

## The Way We Got The X and Y Values for the States on the Map
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
