#15-exercise coffee machine
isOn = True
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino":{
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 14
        },
        "cost": 3.0
    },
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100 
}

def isResourceSufficient(ingredients):
    for itemKey in ingredients:
        if ingredients[itemKey] >= resources[itemKey]:
            print(f'Sorry there is not enough {itemKey}.')
            return False
    return True

def isTransactionSuccessful(moneyReceived, drinkCost):
    if moneyReceived > drinkCost:
        change = round(moneyReceived - drinkCost, 2) # 2: number of decimal places
        print(f'Here is {change} in change')
        global profit
        profit += drinkCost
        return True
    else:
        print('Sorry that\'s not enough money. Money refunded.​')
        return False

def processCoins():
    print('Please insert coins')
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .1
    total += int(input("How many nickles?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total

def makeCoffee(drinkName, ingredients):
    for itemKey in ingredients:
        resources[itemKey] -= ingredients[itemKey]
    print('Here is your drink😊')

while isOn:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choice == 'off':
        isOn = False
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choice]
        if isResourceSufficient(drink["ingredients"]):
            payment = processCoins()
            if isTransactionSuccessful(payment, drink['cost']):
                makeCoffee(choice, drink['ingredients'])