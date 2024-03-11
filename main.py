from turtle import Screen
import time
from food import Food
from  scoreboard import  ScoreBoard
from snake_behaviour import Snake


screen = Screen()

screen.setup(600, 500)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


screen.listen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

snake.making_snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gaming = True
while gaming:
    screen.update()
    time.sleep(0.1)

    snake.moving_snake()

    if snake.head.distance(food) < 15:
       food.refresh()
       snake.extend_snake()
       scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 240 or snake.head.ycor() < -240 :
        gaming = False
        scoreboard.game_over()

    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            scoreboard.game_over()
            gaming = False


screen.exitonclick()
