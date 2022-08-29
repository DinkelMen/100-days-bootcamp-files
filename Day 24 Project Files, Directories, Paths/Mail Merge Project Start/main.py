# '''TODO: Create a letter using starting_letter.txt'''
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


with open('Input/Names/invited_names.txt') as name:
    names = name.read()
    names_list = names.split('\n')

with open('Input/Letters/starting_letter.txt') as mock_up:
    start = mock_up.read()
    for name in names_list:
        with open(f'Output/ReadyToSend/Welcome {name} letter.', 'w') as new_file:
            new_file.write(start.replace('[name]', name))
