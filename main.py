from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time
# Setup of the screen
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.title("SNAKE GAME")
screen.setup(width=600, height=600)

# creating objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# starting of the game
game_on = True

# using arrow keys to move the sake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # increasing the snake size
    if snake.head.distance(food) < 20:
        food.random_position()
        snake.extend()
        scoreboard.increase_score()

    # detecting collision with the walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detecting collision with the snake itself
    for each_segment in snake.segments[1:]:
        if snake.head.distance(each_segment) < 10:
            time.sleep(1)
            scoreboard.reset()
            snake.reset()

screen.exitonclick()