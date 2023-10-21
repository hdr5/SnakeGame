from tkinter import *
# the de facto way in Python to create Graphical User interfaces (GUIs)
import random


GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50  #size of every square in the board
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = 'black'


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")




def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y)) # at index 0

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill= SNAKE_COLOR)

    snake.squares.insert(0, square)

    window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    pass

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

window.eval('tk::PlaceWindow . center')

window.bind('<Left>', lambda  event: change_direction('left'))
window.bind('<Right>', lambda event: print('right'))
window.bind('<Up>', lambda event: print('up'))
window.bind('<Down>', lambda event: print('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()


