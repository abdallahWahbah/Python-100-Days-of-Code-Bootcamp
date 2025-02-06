# file = open('my_file.txt')
# content = file.read()
# print(content)
# file.close() 

# another way without closing the file(close automatically)
with open('my_file.txt') as file:
    content = file.read()
    print(content)

# write to file
# if file doesn't exist, it will create a file for you
with open('new_file.txt', mode='a') as file: # mode='r': read only(default), w: wrie(override everything), a: append(add to existing)
    file.write('\nNew Line')


# exercise
print('  hello    '.strip()) # removes extra spaces
file = open('my_file.txt')
linesList = file.readlines() # Return all lines in the file, as a list where each line is an item in the list object
print(linesList)

for index, line in enumerate(linesList):
    linesList[index]= line.replace('\n', '')
    
print(linesList)





# conclusion (if you have a file that contains list of lines)
# data = []
# with open('file.txt') as data_file:
#     lines = data_file.readlines()
#     for line in lines:
#         data.append(line.strip())

# print(data)