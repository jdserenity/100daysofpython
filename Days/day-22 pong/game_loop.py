from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball


def someone_scores(ball, paddle_left, paddle_right):
    ball.refresh()
    paddle_left.refresh()
    paddle_right.refresh()


def game_loop():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title('Pong')
    screen.tracer(0)

    score = Scoreboard()

    paddle_left = Paddle('left')
    paddle_right = Paddle('right')

    ball = Ball()

    screen.listen()

    screen.onkey(paddle_left.up, "w")
    screen.onkey(paddle_left.down, "s")

    screen.onkey(paddle_right.up, "i")
    screen.onkey(paddle_right.down, "k")

    game_is_on = True
    while game_is_on:
        screen.update()

        ball.move()

        # Detect collision with paddles
        if ((ball.distance(paddle_left) <= 50 and ball.xcor() <= -344) or
                (ball.distance(paddle_right) <= 50 and ball.xcor() >= 336)):
            ball.bounce_paddle()
            # ball.increase_speed()

        # Detect someone scoring
        if ball.xcor() <= -400:
            score.update_right_score()
            someone_scores(ball, paddle_left, paddle_right)
        elif ball.xcor() >= 400:
            score.update_left_score()
            someone_scores(ball, paddle_left, paddle_right)

    screen.exitonclick()
