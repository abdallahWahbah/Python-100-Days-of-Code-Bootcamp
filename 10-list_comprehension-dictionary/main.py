# list comprehension, dictionary comprehension


# # list comprehension
# arrNum = [1, 2, 3, 4] # increase each one by 1
# newArrNum = [n + 1 for n in arrNum]
# print(newArrNum)

# name = 'ABDALLAH'
# newNameArr = [letter.lower() for letter in name]
# print(newNameArr)

# # conditional list comprehensive
# namessss = ["Mah", "Mahmoud", "Wahbah"]
# newNameArrUpperCase = [name.upper() for name in namessss if len(name) > 5]
# print(newNameArrUpperCase)

# # double only the even number in arrNum
# evenNumArrDoubled = [n * 2 for n in arrNum if n % 2 == 0]
# print(evenNumArrDoubled)



# dictionary comprehension
import random
import pandas
names = ['Abdo', 'Mahmoud', 'Abdelbary', 'Abdallah', 'Wahbah']
# we want to print something like the following (not exatly the same result)
# direction_comprehensive = {
#     "Abdallah": 67, # random
#     "Mahmoud": 55
# }

# looping through a list
studentsDegrees = {student: random.randint(1, 100) for student in names if len(student) > 4} 
print(studentsDegrees) # {'Mahmoud': 3, 'Abdelbary': 2, 'Abdallah': 1, 'Wahbah': 1}
# looping through a dictionary and using dictionary comprehension
passedStudents = {studentName: studentDegree for (studentName, studentDegree) in studentsDegrees.items() if studentDegree > 50}
print(passedStudents) # {'Mahmoud': 55, 'Abdelbary': 64}

# looping through a dictionary
student_dict = {
    'names': ['wael', 'samy', 'ebrahim'],
    'ages': [54, 32, 96]
}

df = pandas.DataFrame(student_dict)
# # you can loop through a data frame (dataframe) using the same way (bad way)
# for (key, value) in df.items():
#     print(value)


# use this formula to loop through a data frame 
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

for(index, row) in df.iterrows():
    if row.names == 'samy':
        print(row.ages)