menu = {
    'espresso': {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18, },
        "cost": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24, },
        "cost": 2.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 24, },
        "cost": 3.00
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
is_on = True
while is_on:
    order = input("what would you like ?(espresso/latte/cappuccino)").lower()
    # TODO 1: print report
    if order == "report":
        print(f"water:{resources['water']}ml\n"
              f"milk:{resources['milk']}ml\n"
              f"coeffee:{resources['coffee']}g\n"
              f"money:{profit}$")
    elif order == 'off':
        print("Thank you!")
        is_on = False
    else:
        drink = menu[order]
        water_required = drink["ingredients"]['water']
        milk_required = drink["ingredients"]['milk']
        coffee_required = drink["ingredients"]['coffee']
        bill = drink["cost"]


        # TODO 2: checking if the resources are sufficient
        def repot(order_ingrediants):
            for item in order_ingrediants:
                if order_ingrediants[item] > resources[item]:
                    print(f'sorry there is no enough {item}.')
                    return False
                else:
                    return True


        # TODO 3: process coins
        def money():
            penny = int(input("How many penny?"))
            quarter = int(input("How many Quarter ?"))
            dime = int(input("How much dime?"))
            nickel = int(input("How much nickel ?"))
            total = penny * 0.01 + quarter * 0.25 + dime * 0.1 + nickel * 0.05
            return total


        # TODO 4: check transaction is sucessful
        if repot(drink['ingredients']):
            transcation = money()
            if transcation >= bill:
                amount = transcation - bill
                print(f"Here is {amount}$ in change.")
                profit += bill
                # TODO 5:make coffee
                print(f"here is your {order} ☕ ,enjoy!")
            else:
                print("sorry not enough money, money is refunded")


        def resource():
            resources['water'] = resources['water'] - drink['ingredients']['water']
            resources['milk'] = resources['milk'] - drink['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - drink['ingredients']['coffee']


        resource()
