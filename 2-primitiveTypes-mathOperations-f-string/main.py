# string 
helloMessage = 'Hello'
# subscripting
print(helloMessage[0]) # H
print(helloMessage[-1]) # o
print(helloMessage[-2]) # l
# concatination
print("123" + "456")

# Integers
print(2 + 4)
print(123_456_789)

# Float
print(3.158)

# bool
print(True)
print(False)

# type
print(type("Hello")) # <class 'str'>
print(type(123)) # <class 'int'>
print(type(5.56)) # <class 'float'>
print(type(True)) # <class 'bool'>

# conversion
print(int(123) + int(432)) # int() float() str() bool()

# print("Hello " + 1) # TypeError: can only concatenate str (not "int") to str
print('Hello with number #' + str(123))

# mathematical operation
print(123 + 456)
print(123 - 456)
print(123 * 456)
print(20 / 4) # result: 5.0 float (implicit type casting >>> python implicitly converts the result into a float number)
print(20 // 4) # retuslt 5 (deletes the decimal numbers >>> 5 // 3 = 1 which is wrong (be careful))
print(2**3) # 8

# priority of mathematical operations (PEMDAS >>> P: parantheses, E: exponents, M: multiplication, D: division, A: addition, S: subtaction)
print(3 * 3 + 3 / 3 - 3) # 7

# number manipulation
print(round(3.4)) # 3
print(round(3.9)) # 4
print(round(3.152, 2)) # round it to 2 decimal places >>> 3.15 >> if 3.1 >>> prints 3.1 not 3.10
print(int(3.9)) # 3 >>> deletes the decimal part

# f-strings >>> mix strings with different daata types
score = 12
height = 180
# print('Score is: ' + score) # TypeError: can only concatenate str (not "int") to str
print('Score is: ' + str(score))
print(f'Score is: {score}, height is {height}')