# 1-print-input-variables
# 2-primitiveTypes-f-string-if-random-list-loops
# 5-6-loops:for-while sum, max, range, shuffle - functions
# 7-expercise: hanngman: construct array from a string and visa verse
# 8-10-functions with keyword arguments and return, .title
# 9-12-dictionary-scope


######## Notes
# to declare a constant >> the convension is to make all letters uppercase
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






# # 5-6-loops:for-while sum, max, range, shuffle - functions
# fruits = ["Apple", "Peach", "Banana"]
# scores = [1, 54, 8541, 452, 235]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + ' Pie')
# print('Done')

# # sum
# sum_value = 0
# for score in scores:
#     sum_value += score
# print("sum function", sum(scores))
# print("sum loop", sum_value)

# # max
# max_value = 0
# for score in scores: 
#     if(score > max_value):
#         max_value = score
# print("max function", max(scores))
# print("max loop", max_value)

# # range
# # for number in range(1, 10, 1): # start, end(excluding), step size(optional)
# #     print(number)

# # gauss challenge: print the total of the numbers between 1 and 100(including)
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

# # suffle: Takes a sequence(array-list) and returns the sequence in a random order
# print(scores)
# random.shuffle(scores)
# print(scores)

# # function
# def test_function():
#     print('Test function')
# test_function()

# # while loop
# num_test = 1
# while num_test <= 5: # while ((not)) num_test <= 5
#     print(num_test)
#     num_test += 1
# print('End of while loop with num_test = ', num_test)






# # 7-expercise: hanngman: construct array from a string and visa verse
# wordList = ["Hello", "Green", "Engineer"]
# word = random.choice(wordList).lower()
# wordToPrint = ['-' for _ in word] # ['-', '-', '-', '-', '-']
# lifes = 6

# print('Word', word)
# print("Word to print", ''.join(wordToPrint)) # '-----'

# while lifes > 0 and '-' in wordToPrint:
#     inputLetter = input('Guess a letter that could be in the word: ').lower()
#     if(inputLetter in word):
#         for index, letter in enumerate(word):
#             if inputLetter == letter:
#                 wordToPrint[index] = inputLetter
#     else: 
#         lifes -= 1

#     print("Word to print: ", ''.join(wordToPrint))
#     print(f'remaining lives {lifes}')

#     if '-' not in wordToPrint:
#         print("Congratulations! You've guessed the word.")
#         break

# if '-' in wordToPrint:
#     print("Game Over! The word was:", word)






# 8-10-functions with keyword arguments and return
# def greet(name, location):
#     print(f'hello {name}, what is the weather like in {location}')

# greet('Abdallah', 'egypt')
# greet(location = 'cairo', name = 'wahbah') # keyword arguments (you can change the order of the parameters)

# # caeser cipher
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# restart = True

# def caeser(inputText, shiftAmount, encodeOrDecode):
#     output = ""
#     if encodeOrDecode == "decode":
#         shiftAmount *= -1

#     for letter in inputText:
#         if letter not in alphabet:
#             output += letter
#         else: 
#             # if(encodeOrDecode == "encode"):
#             #     shiftedPosition = alphabet.index(letter) + shiftAmount
#             # else:
#             #     shiftedPosition = alphabet.index(letter) - shiftAmount
            
#             shiftedPosition = alphabet.index(letter) + shiftAmount
#             shiftedPosition = shiftedPosition % len(alphabet) # to handle letter that will be out of index 
#             # (more than 26) or (less than 0 >> if -2 for example >> that will be the item before the end)
#             output += alphabet[shiftedPosition]
#     print(f"Here is the {encodeOrDecode}d word: {output}") # jgnnq >> hello


# while restart:
#     direction = input('type "encode" to encrypt, type "decode" to decrypt ').lower()
#     text = input('Type the message ').lower()
#     shift = int(input('Type shift number '))
#     caeser(text, shift, direction)
#     shouldRestart = input('Type "Yes" to restart ').lower()
#     if shouldRestart != 'yes' :
#         restart = False
# print('abdallah mahmoud abdelbary'.title()) # make first letter of each word a camel case
# def formatName(firstName, lastName):
#     if firstName == "" or lastName == "":
#         return "Empty Name"
#     return f'{firstName.title()} {lastName.title()}'
# formattedName = formatName('Abdallah', "Wahbah")
# print(formattedName)





# # 9-12-dictionary-scope
# programmingDicitonary = {
#     "Bug": "An error can occure",
#     "Function": "We need to write a new function",
#     "Egypt": ["Cairo", "Alex", "Giza", "Luxor"],
#     "Employee": {
#         "id": 1,
#         "name": "Abdallah",
#         "age": '27'
#     }
# }
# print(programmingDicitonary["Bug"])
# print(programmingDicitonary["Egypt"][2], programmingDicitonary["Employee"]["name"])
# programmingDicitonary["Loop"] = "Loop is done using for or while"
# programmingDicitonary["Bug"] = "Modifying a bug"
# print(programmingDicitonary)

# # looping through a dicionary
# for key in programmingDicitonary: 
#     print(key + ": ", programmingDicitonary[key])

# nestedList = ["A", "B", ["C", "D"]]
# print(nestedList[2][1])

# # Secret Auction exercise
# name = ""
# bid = ""
# anotherBid = True
# bids = {}
# sum = 0
# maxBid = 0

# def newBid():
#     name = input('What\'s your name? ')
#     bid = int(input('What\'s your bid? $'))
#     bids[name] = {
#         "name": name,
#         "bid": bid,
#     }

# while anotherBid:
#     newBid()
#     anotherBid = input('Is there another bid? type "Yes" or "No" ').lower() == 'yes'

# for key in bids:
#     sum += bids[key]["bid"]
#     if maxBid < bids[key]["bid"]:
#         maxBid = bids[key]["bid"]
# print('Sum', sum, maxBid)

####### Notes about scope
# if we have a varibal in a global scope and the same name of the variable in a local scope, when prinitin in global >> value of global ---- when printing in local >> value in local
# no block scope in python, if a varibale declared in if-statement, i can print it outside of it >>> but be careful, if the if-statement is in a function scope, you can't access the variable outside the function
# if you created a variable within a function, it will be available only in this function 
# if you created a variable within a block (if-while-for)(anything that has indentation of column :), you are not creating a separate local scope

# enemies = 1
# def increaseEnemies():
#     # if you want to modify the global variable in a local scope you need to declare it first (not preferred)(use return way from a function instead)
#     # global enemies
#     # enemies += 1
#     enemies = 2
#     print("inner", enemies)

# increaseEnemies()
# print("outer", enemies)

# try: # try/catch
#     age = int(input("What's your age? "))
# except ValueError:
#     print("Please write in numbers not string")
#     age = int(input("what's your age? "))
# print(age)






# # small exercise
# gameDictionary = {
#     1: {
#         "question": "Who is better: Cristiano or Messi? ",
#         "answer": "Cristiano"
#     },
#     2: {
#         "question": "What is the capital of France? ",
#         "answer": "Paris"
#     },
#     3: {
#         "question": "What is the largest planet in the Solar System? ",
#         "answer": "Jupiter"
#     },
#     4: {
#         "question": "Who painted the Mona Lisa? ",
#         "answer": "DaVinci"
#     },
#     5: {
#         "question": "What is the fastest land animal? ",
#         "answer": "Cheetah"
#     },
#     6: {
#         "question": "What is the chemical symbol for gold? ",
#         "answer": "Au"
#     },
#     7: {
#         "question": "Which ocean is the largest? ",
#         "answer": "Pacific"
#     },
#     8: {
#         "question": "What is the square root of 64? ",
#         "answer": "Eight"
#     },
#     9: {
#         "question": "Who developed the theory of relativity? ",
#         "answer": "Einstein"
#     },
#     10: {
#         "question": "Which sport is known as the 'king of sports'? ",
#         "answer": "Football"
#     },
# }

# for index, key in enumerate(gameDictionary):
#     item = gameDictionary[key]
#     answerInput = input(item["question"]).lower()
#     if(answerInput != item["answer"].lower()):
#         print(f'Wrong, the correct answer is {item["answer"]}')
#         print(f'you passed {index} questions')
#         break
#     else:
#         print('Correct answer')