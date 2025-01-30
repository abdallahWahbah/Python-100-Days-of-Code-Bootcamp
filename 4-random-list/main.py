# random
import random

print(random.randint(1, 5)) #   a <= N <= b
print(random.random()) #        floating-point number X such that 0.0 <= X < 1.0
print(random.random() * 10) #   0 to 9 (float)
print(random.uniform(5, 9)) #   floating-point number N such that a <= N <= b

# program to print whether it's a head(0) or tail(1)
randomHeadTail = random.randint(0, 1)
if randomHeadTail == 0:
    print(randomHeadTail, 'Head')
else :
    print(randomHeadTail, 'Tail')


# Lists
states = ["Hello", "from", "the", "other"]
print(states[1])
states.append('Side')
print(states[-1])
states.extend(["New", "Array"])
print(states)
# lastItem = states.pop()
# print(lastItem)
print(states)
print(states[len(states) - 1])

# get a random item from a list
names = ["Abdallah", "Mahmoud", "Wahbah"]
print(random.choice(names))
print(names[random.randint(0, len(names) - 1)])