# Add one to all numbers in list
# old way for loop
numbers1 = [1, 2, 3]
new_numbers1 = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)


# List comprehension
NEW_LIST = [NEW_ITEM for ITEM in LIST]

numbers2 = [1, 2, 3]
new_numbers2 = [n + 1 for n in numbers]
[2, 3, 4]

name = "Angela"
name_letter_list = [letter for letter in name]
['A', 'n', 'g', 'e', 'l', 'a']

# new way + test
NEW_LIST = [NEW_ITEM for ITEM in LIST if TEST]

names = ["Alex", "Beth", "Carloine", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
['Alex', 'Beth', 'Dave']

upper_names = [name.upper() for name in names if len(name) > 5]
['CARLOINE', 'ELEANOR', 'FREDDIE']


# Dictionary Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random

NEW_DICTIONARY = {NEW_KEY: KEY_VALUE for ITEM in LIST}

student_scores = {student: random.randint(1, 100) for student in names}
{'Alex': 44, 'Beth': 31, 'Caroline': 98, 'Dave': 89, 'Eleanor': 76, 'Freddie': 89}

passed_students = {NEW_KEY: KEY_VALUE for (KEY, VALUE) in DICTIONARY.items() if TEST}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}


# Iterate over a Panda DataFrame
student_dic = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas
student_data_frame = pandas.DataFrame(student_dic)
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

NEW_DICTIONARY = {NEW_KEY: KEY_VALUE for (index, row) in DATAFRAME.items()}

