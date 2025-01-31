
with open("./file1.txt", "r") as file1:
    file1_list = [int(line.strip()) for line in file1.readlines()]

with open("./file2.txt", "r") as file2:
    file2_list = [int(line.strip()) for line in file2.readlines()]

result = [common for common in file1_list if common in file2_list]

print(result)

# ######

import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(1, 100) for student in names}
for v in students_scores.values():
    print(f"{v} \n")
passed_students = {k:v for k,v in students_scores.items() if v > 50}
for v in passed_students.keys():
    print(v)

# #####

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_list = sentence.split()
result = {word:len(word) for word in words_list}
for v in result.values():
    print(v)

# #####

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp_c * 9/5) + 32 for day,temp_c in weather_c.items()}
print(weather_f)
# ####

import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_dataframe = pd.DataFrame(student_dict)
print(student_dataframe)

for (index, row) in student_dataframe.iterrows():
    print(row)

df = pd.read_csv("./unilever_users_with_workspaces.csv")

