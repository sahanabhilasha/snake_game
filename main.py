from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from score_board import score_board

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()
score_board = score_board()

screen.listen()

screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    #tail collied
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            score_board.game_over()

screen.exitonclick()
