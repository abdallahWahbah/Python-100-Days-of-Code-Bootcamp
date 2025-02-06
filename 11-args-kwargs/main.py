# args
def add(*args): # the same as rest in js
    print(args) # tuple not array >>> (1, 2, 3, 4)
    sum = 0
    for num in args:
        sum += num
    print(sum)

add(1, 2, 3, 4)


# kwargs(with functions): key word arguments
def calculate(sum, **kwargs):
    print(kwargs) # dictionary >>> {'add': 3, 'multiply': 5}
    print(kwargs['add'], kwargs['multiply'])
    # sum += kwargs['add']
    # sum += kwargs['multiply']
    for key, item in kwargs.items():
        print(key, item)
        sum += item
    print('sum', sum)
calculate(0, add=3, multiply=5)


# kwargs(with class)
class Car:
    def __init__(self, **kw):
        self.sum = 0
        self.sum += kw['firstNum']
        self.sum += kw.get('secondNum') # the same as the line above, but it won't give error if it doesn't exist, 
        # but we here are making math calc, so we must pass it >>>> useful when assigning it to a variable

car1 = Car(firstNum=2, secondNum=5)
print(car1.sum)





# # Question 5:
# def all_aboard(a, *args, **kw): 
#     print(a, args, kw) # 4 (7, 3, 0) {'x':10, 'y':64}
 
# all_aboard(4, 7, 3, 0, x=10, y=64)
