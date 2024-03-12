from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def check_player_level_with_car(player, car):
    for i in range(-10, 11):
        for j in range(-10, 11):
            if player.ycor() + i == car.ycor() + j:
                return True


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('white')
    screen.title('Turtle Crossing')
    screen.tracer(0)

    score = Scoreboard()
    cars = CarManager()
    player = Player()

    screen.listen()

    screen.onkey(player.up, "Up")

    game_is_on = True
    should_gen_car = False
    gen_car_counter = 0.7
    num_cars_to_gen = 1
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        gen_car_counter += 0.1
        if gen_car_counter >= 0.7:
            should_gen_car = True
            gen_car_counter = 0

        if should_gen_car:
            cars.gen_car(num_cars_to_gen)
            should_gen_car = False

        cars.move_cars()

        # Player wins level
        if player.ycor() + 5 >= 300:
            player.refresh()
            score.update_score()
            cars.increase_move_distance()
            num_cars_to_gen += 0.2
            print(num_cars_to_gen)

        # Player hits a car
        for car in cars.cars:
            if player.distance(car) < 26 and check_player_level_with_car(player, car):
                print(car.color())
                score.game_over()
                game_is_on = False

    screen.exitonclick()


if __name__ == '__main__':
    main()
