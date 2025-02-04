# Day 17
class User:
    # constructor: first thing getting executed when creating a new object (instance) on the class 
    def __init__(self, user_id, username): # self: the actual object that is being created or initialized
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Abdallah")
user_2 = User("002", "Mahmoud")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following) 
