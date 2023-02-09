MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


def update_resource(ingredients, resources):
    """return the new resources"""
    for value in ingredients:
        resources[value] = (resources[value] - ingredients[value])
    return resources


def transaction(cost, order):
    """return true if transaction success, false if money is not enough"""
    customer_paid = round(((int(input("Penny: \n"))) * 0.01 + (int(input("dime: \n"))) * 0.01 +
                           (int(input("Nickel: \n"))) * 0.05 + (int(input("Quarter: \n"))) * 0.25), 2)
    if customer_paid > cost:
        print(f"You pay {customer_paid}. The change is: {round((customer_paid - cost), 2)}. "
              f"We are preparing your {order}.")
        return True
    else:
        print("The money is not enough!")
        return False


def make_coffee():
    turn_off_machine = False
    profit = 0
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    while not turn_off_machine:
        order = input("What would you like? (espresso/latte/cappuccino):")
        order_menu = MENU[order]
        ingredients = order_menu["ingredients"]
        cost = order_menu["cost"]
        has_coffee = True

        if order == 'report':
            for n in resources:
                print(f"{n}:{resources[n]}ml")
        elif order == 'off':
            turn_off_machine = True

        for value in ingredients:
            if resources[value] - ingredients[value] < 0:
                has_coffee = False

        if has_coffee:
            print(f"Please enter the money: \n")
            if transaction(cost, order):
                resources = update_resource(ingredients, resources)
                profit += cost
                print(profit)
        else:
            print(f"Not enough ingredient!")


make_coffee()
