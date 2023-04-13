from coffeemachine_art import logo

MENU = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


coin_values = {
    "€1": 1,
    "50c": 0.5,
    "20c": 0.2,
    "10c": 0.1,
}

income = 0
restock_resources = resources.copy()


def check_resources(order):
    """returns True if resources are ok, False if not"""
    for ingredient, amount in MENU[order]['ingredients'].items():
        if amount > resources[ingredient]:
            print(f"Not enough {ingredient} available for {order}")
            return False
    return True


def process_coins(order, income):
    """Returns income after coins are processed and deducts resource ingredients """
    coins_entered = {}
    total_coin_value = 0

    # print drink price
    print(f"{order} price: €{MENU[order]['cost']:.2f}\n")

    # prompt for coins and count total inserted
    for denomination, value in coin_values.items():
        count = int(input(f"Enter the number of {denomination} coins: "))
        total_coin_value = total_coin_value + (count * coin_values[denomination])
        print(f"Entered: €{total_coin_value:.2f}")

        # stop prompting if total is sufficient
        if total_coin_value >= MENU[order]['cost']:
            break

    # if not enough coins entered
    if total_coin_value < MENU[order]['cost']:
        print("Not enough money, coins refunded.")
    # make drink, give change and add income
    else:
        change = total_coin_value - MENU[order]['cost']
        income = income + MENU[order]['cost']
        print(f"\nEnjoy your {order} ☕, here's your change: €{change:.2f}")

        # deduct used ingredients from resources
        for ingredient, amount in MENU[order]['ingredients'].items():
            resources[ingredient] = resources[ingredient] - amount

    return income


# function for admin menu
def admin(income):
    """Returns True and Income except for Shutdown which returns False and Income"""
    admin_mode = True

    def print_report():
        print(f"\nWater:  {resources['water']}ml")
        print(f"Milk:   {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money:  €{income:.2f}")

    while admin_mode:
        print("\nAdmin Menu:")
        print("'r' for report")
        print("'s' to restock")
        print("'c' to cash out")
        print("'o' to turn off")
        prompt = input("'e' to exit: ")

        if prompt == 'r':
            print_report()
        elif prompt == 's':
            for ingredient, amount in resources.items():
                resources[ingredient] = restock_resources[ingredient]
            print_report()
        elif prompt == 'c':
            print(f"\n€{income:.2f} debited.")
            income = 0
        elif prompt == 'o':
            print("Shutting down...")
            return False, income
        elif prompt == 'e':
            return True, income
        else:
            print("Invalid input, please try again")


keep_running = True

print(logo)

while keep_running:

    # check resources
    for ingredient, amount in resources.items():
        if amount == 0:
            print(f"\nWARNING! {ingredient} level low.")

    # prompt for user input
    prompt = input("\nEspresso/Latte/Cappuccino? type e, l or c: ")

    # enter admin
    if prompt == 'admin':
        keep_running, income = admin(income)

    # successful order
    elif prompt == 'e' or prompt == 'l' or prompt == 'c':
        if prompt == 'e':
            order = 'Espresso'
        elif prompt == 'l':
            order = 'Latte'
        elif prompt == 'c':
            order = 'Cappuccino'

        if check_resources(order):
            income = process_coins(order, income)

    else:
        print("Invalid input, please try again")




