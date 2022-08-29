import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
right_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(right_dict)

user_word = input('Enter a word: ')
code_word = [right_dict[n.upper()] for n in user_word]
print(code_word)


# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
# Access index and row
# Access row.student or row.score
# pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
