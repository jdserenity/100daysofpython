import pandas

data = pandas.read_csv('./50_states.csv')
states_list = data['state'].to_list()


def check_input(user_input):
    return True if user_input.title() in states_list else False


def get_x_and_y(user_input):
    x = data[data.state == user_input.title()]['x'].to_list()[0]
    y = data[data.state == user_input.title()]['y'].to_list()[0]
    return x, y
