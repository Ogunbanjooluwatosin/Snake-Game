import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(height=750, width=1200)
screen.bgcolor("black")
screen.title("Tosin's Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.go_right, key="Right")
screen.onkey(fun=snake.go_left, key="Left")

#

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    #   Collision with food
    if snake.snake_list[0].distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    #  Collision with wall
    if snake.snake_list[0].xcor() > 570 or snake.snake_list[0].xcor() < -570 or snake.snake_list[0].ycor() > 355 or \
            snake.snake_list[0].ycor() < -355:
        scoreboard.update()
        snake.reset()


# Collision with tail
    for segments in snake.snake_list[1:]:
        if snake.snake_list[0].distance(segments) < 15:
            scoreboard.update()
            snake.reset()

screen.exitonclick()
