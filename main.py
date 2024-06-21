from tkinter import *
import random


GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 80
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


def check_collisions(snake):

    x, y = snake.coordinates[0]
    # checking for collision with the borders
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    # checking for a collision with the snake itself
    for body_part in snake.coordinates[1:]:
        if body_part[0] == x and body_part[1] == y:
            return True


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

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score+=1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
        return
    window.after(SPEED, next_turn, snake, food)

def game_over():

    global highScore
    if score > highScore:
        highScore = score

    canvas.delete(ALL)

    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/4, fill='white', text='High Score:{}'.format(highScore), tag='highscore', font=('consolas', 25))
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, fill='yellow', text='GAME OVER', tag='gameover', font=('consolas', 70))

    global btn
    btn = Button(window, text='Try again', width=10,
                 height=2,padx=5, font=('consolas',15), bd='4', command=new_game)
    btn.place( relx=0.5, rely=0.7, anchor=CENTER)

def change_direction(new_direction):

    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    if new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def new_game():

    canvas.delete(ALL)
    btn.destroy()

    snake = Snake()
    food = Food()

    global direction
    direction = 'right'

    global score
    score = 0

    label.config(text="Score:{}".format(score))

    next_turn(snake, food)


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

highScore = 0
score = 0
direction = 'right'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

window.eval('tk::PlaceWindow . center')

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()

