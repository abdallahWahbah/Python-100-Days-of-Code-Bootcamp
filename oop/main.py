# Day 16
# predefined classes (Turtle, Screen)
# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color('carol')
# timmy.forward(100)
# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()




# PrettyTable: third party library >>>>   https://github.com/prettytable/prettytable
# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column('Type', ['Electric', 'Water', 'Fire'])
# print(table)
# table.align = 'l'
# print(table)



# old program (coffee maker) in oop (you can ignore it if you want)
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()

isOn = True

while isOn:
    options = menu.get_items()
    choice = input(f'What would you like? ({options}):')
    if choice == "off":
        isOn = False
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)