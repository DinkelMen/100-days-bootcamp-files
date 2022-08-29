import random
list1 = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# name = 'Dima'
#
# list2 = [n.upper() for n in list1 if len(n) > 4]
# print(list2)

# with open('file1.txt') as file1:
#     file1_list = file1.read().split('\n')
#
# with open('file2.txt') as file2:
#     file2_list = file2.read().split('\n')
#
# result = [int(n) for n in file1_list if n in file2_list and n != '']
# print(result)

# missing_states = [state for state in all_states if state not in guessed_states]

student_scores = {student: random.randint(1, 100) for student in list1}
print(student_scores)
# print(student_scores.keys())
passed_student = {student: student_scores[student] for student in student_scores.keys() if student_scores[student] >= 60}
print(passed_student)
# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
