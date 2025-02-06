# # old way of reading files
# data = []
# with open('weather_data.csv') as data_file:
#     lines = data_file.readlines()
#     for line in lines:
#         data.append(line.strip())
# print(data)


# # Using csv module & open method (better but not the best )
# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row) # ['Monday', '12', 'Sunny']
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


###### using pandas
# import pandas
# data = pandas.read_csv('weather_data.csv')
# # print(data['temp'])
# data_dict = data.to_dict() # dictionary
# print(data_dict)
# data_list = data['temp'].to_list()
# print(data_list) # [12, 14, 15, 14, 21, 22, 24]






# video #191

# ###### Get data in column 
# # you can access column using key or attribute >>> data['temp] or data.temp

# ###### series functions: https://pandas.pydata.org/docs/reference/series.html

# # to get average (mean), max 
# # traditional way
# average = sum(data_list) / len(data_list)
# print("traditional", average)
# # using pandas
# print("pandas average", data['temp'].mean())
# print("pandas max", data['temp'].max())

# ###### Get data in row
# mondayData = data[data.day == 'Monday']
# print("mondayData: ")
# print(mondayData)
# print('CONDITION: ', mondayData.condition)
# print(data[data.temp == data.temp.max()])  # get the row where temp is at its max

# ###### how to differentiate between accessing column and row 
# # if you passed a condition, you are accessing row
# # if you passed a key, you are accessing a coumn


# # challenge: get temp on Monday from weather_data.csv
# mondayTemp = data[data.day == 'Monday'].temp[0] # [0]: cause there can be more than an item called Monday
# print(mondayTemp)


# ###### Create a dataframe (such as table in csv file) using the following dictionary and store in a csv file
# dataDictionary = {
#     'students': ['Amy', 'Nahla', 'Walaa'],
#     'scores': [50, 845, 20]
# }
# print(pandas.DataFrame(dataDictionary))
# dataframe = pandas.DataFrame(dataDictionary) # table
# dataframe.to_csv('new_file.csv')  # save it as csv file



# 192: exercise on using pandas in data analysis
# using data in squirrel_data, extract count of Gray, Cinnamon, Black items from 'Primary Fur Color' column 
# and store the result in a new csv file
import pandas

data = pandas.read_csv('squirrel_data.csv')
gray_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_squirrel_count, red_squirrel_count, black_squirrel_count)

data_dictionary = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

dataframe = pandas.DataFrame(data_dictionary)
dataframe.to_csv('squirrel_count.csv')