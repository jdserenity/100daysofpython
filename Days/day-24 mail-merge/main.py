# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open('./Input/Names/invited_names.txt', mode='r') as names_file:
    names = names_file.readlines()

for name in names:
    with open('./Input/Letters/starting_letter.txt', mode='r') as starting_letter:
        lines = starting_letter.readlines()

    if name[-1] == '\n':
        name = name[:-1]

    lines[0] = lines[0].replace('[name]', name)

    with open(f'./Output/ReadyToSend/{name}_invite.txt', mode='w') as new_file:
        new_file.write(''.join(lines))
