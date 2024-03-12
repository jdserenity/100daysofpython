from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def game_over(scoreboard, snake):
    if scoreboard.score > scoreboard.high_score:
        scoreboard.set_high_score(screen)

        screen.listen()

    scoreboard.reset()
    snake.reset()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(lambda: snake.direction('up'), "Up")
screen.onkey(lambda: snake.direction('down'), "Down")
screen.onkey(lambda: snake.direction('left'), "Left")
screen.onkey(lambda: snake.direction('right'), "Right")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()

    if snake.head.distance(food) < 17:
        score.update_score()
        snake.grow_length()
        food.regen()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        screen.update()
        game_over(score, snake)

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over(score, snake)

screen.exitonclick()
