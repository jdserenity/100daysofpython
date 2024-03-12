import pandas

data = pandas.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

counts = [0, 0, 0]

for color in data['Primary Fur Color']:
    if color == 'Gray':
        counts[0] += 1
    if color == 'Black':
        counts[1] += 1
    if color == 'Cinnamon':
        counts[2] += 1

data_dict = {'Fur Color': ['Gray', 'Black', 'Cinnamon'], 'Count': counts}
new_data = pandas.DataFrame(data_dict)

new_data.to_csv('./squirrel_count.csv')

