# 1-print-input-variables
# 2-primitiveTypes-f-string-if-random-list-loops
# 5-6-loops:for-while sum, max, range, shuffle - functions




import random






# 1-print-input-variables

# print("Hello world!\nHello world!")
# print("Hello, " + "Abdallah")
# print('your age is: ' + input('What is your age? '))

# name = input('What is your name? ')
# print('Your name is: ' + name)
# print('Length of you name is', len(name))
# # print('Family name length is: ', len(input('What is your family name to print its length? ')))
# familyName = input('What is your family name to print its length? ')
# familyNameLength = len(familyName)
# print('Family name length is: ', familyNameLength)






# 2-primitiveTypes-f-string-if-random-list-loops

# # string 
# helloMessage = 'Hello'
# # subscripting
# print(helloMessage[0]) # H
# print(helloMessage[-1]) # o
# print(helloMessage[-2]) # l
# # concatination
# print("123" + "456")

# # Integers
# print(2 + 4)
# print(123_456_789)

# # Float
# print(3.158)

# # bool
# print(True)
# print(False)

# # type
# print(type("Hello")) # <class 'str'>
# print(type(123)) # <class 'int'>
# print(type(5.56)) # <class 'float'>
# print(type(True)) # <class 'bool'>

# # conversion
# print(int(123) + int(432)) # int() float() str() bool()

# # print("Hello " + 1) # TypeError: can only concatenate str (not "int") to str
# print('Hello with number #' + str(123))

# # mathematical operation
# print(123 + 456)
# print(123 - 456)
# print(123 * 456)
# print(20 / 4) # result: 5.0 float (implicit type casting >>> python implicitly converts the result into a float number)
# print(20 // 4) # retuslt 5 (deletes the decimal numbers >>> 5 // 3 = 1 which is wrong (be careful))
# print(2**3) # 8

# # priority of mathematical operations (PEMDAS >>> P: parantheses, E: exponents, M: multiplication, D: division, A: addition, S: subtaction)
# print(3 * 3 + 3 / 3 - 3) # 7

# # number manipulation
# print(round(3.4)) # 3
# print(round(3.9)) # 4
# print(round(3.152, 2)) # round it to 2 decimal places >>> 3.15 >> if 3.1 >>> prints 3.1 not 3.10
# print(int(3.9)) # 3 >>> deletes the decimal part

# # f-strings >>> mix strings with different daata types
# score = 12
# height = 180
# # print('Score is: ' + score) # TypeError: can only concatenate str (not "int") to str
# print('Score is: ' + str(score))
# print(f'Score is: {score}, height is {height}')






# height = int(input('Please, enter you height '))

# if height > 180: # >, <, >=, <=, ==, !=
#     print('Tall')
#     age = int(input('What is your age? '))
#     if age > 20 and age > 21:
#         print('Allowed, old')
#     elif age < 10:
#         print('Kill him')
#     else: 
#         print('Not allowed, young')
# else: 
#     print('Small')

# # modulos operator (remainder of the division)
# if height % 2 == 0:
#     print('Even')
# else: 
#     print('Odd')

# a = 5
# b = 7
 
# if a >= b and a != b:
#     print("A")
# elif not a >= b and a != b:
#     print("B") # right answer
# else:
#     print("C")






# # random
# import random

# print(random.randint(1, 5)) #   a <= N <= b
# print(random.random()) #        floating-point number X such that 0.0 <= X < 1.0
# print(random.random() * 10) #   0 to 9 (float)
# print(random.uniform(5, 9)) #   floating-point number N such that a <= N <= b

# # program to print whether it's a head(0) or tail(1)
# randomHeadTail = random.randint(0, 1)
# if randomHeadTail == 0:
#     print(randomHeadTail, 'Head')
# else :
#     print(randomHeadTail, 'Tail')


# # Lists
# states = ["Hello", "from", "the", "other"]
# print(states[1])
# states.append('Side')
# print(states[-1])
# states.extend(["New", "Array"])
# print(states)
# # lastItem = states.pop()
# # print(lastItem)
# print(states)
# print(states[len(states) - 1])

# # get a random item from a list
# names = ["Abdallah", "Mahmoud", "Wahbah"]
# print(random.choice(names))
# print(names[random.randint(0, len(names) - 1)])






# 5-6-loops:for-while sum, max, range, shuffle - functions
fruits = ["Apple", "Peach", "Banana"]
scores = [1, 54, 8541, 452, 235]
for fruit in fruits:
    print(fruit)
    print(fruit + ' Pie')
print('Done')

# sum
sum_value = 0
for score in scores:
    sum_value += score
print("sum function", sum(scores))
print("sum loop", sum_value)

# max
max_value = 0
for score in scores: 
    if(score > max_value):
        max_value = score
print("max function", max(scores))
print("max loop", max_value)

# range
# for number in range(1, 10, 1): # start, end(excluding), step size(optional)
#     print(number)

# gauss challenge: print the total of the numbers between 1 and 100(including)
total = 0
for i in range(1, 101):
    total += i
print(total)

# suffle: Takes a sequence(array-list) and returns the sequence in a random order
print(scores)
random.shuffle(scores)
print(scores)

# function
def test_function():
    print('Test function')
test_function()

# while loop
num_test = 1
while num_test <= 5: # while ((not)) num_test <= 5
    print(num_test)
    num_test += 1
print('End of while loop with num_test = ', num_test)