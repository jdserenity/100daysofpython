from create_game import create_game; from game_loop import game_loop; # noqa E701


def main():
    objects = create_game()

    game_loop(objects)

    objects['window'].mainloop()


if __name__ == '__main__':
    main()
