# Maintainers commands: "off" and "report"

turn_off_machine = False


drinks_info = [
    {
        "name": "espresso",
        "water": 50,
        "coffee": 18,
        "price": 1.50,
    },
    {
        "name": "latte",
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price": 2.50,
    },
    {
        "name": "cappuccino",
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 3.00,
    }
]


water = 300
milk = 200
coffee = 100
money = 0
products_list = [water, milk, coffee, money]


def requsted_products(water, milk, coffee, money):
    if user_selection == "espresso":
        water = drinks_info[0]["water"]
        coffee = drinks_info[0]["coffee"]
        milk = 0
        money = drinks_info[0]["price"]
    elif user_selection == "latte":
        water = drinks_info[1]["water"]
        coffee = drinks_info[1]["coffee"]
        milk = drinks_info[1]["milk"]
        money = drinks_info[1]["price"]
    elif user_selection == "cappuccino":
        water = drinks_info[2]["water"]
        coffee = drinks_info[2]["coffee"]
        milk = drinks_info[2]["milk"]
        money = drinks_info[2]["price"]
    return water, milk, coffee, money


def products_update(products_list, updated_list):
    products_list[0] -= updated_list[0]
    products_list[1] -= updated_list[1]
    products_list[2] -= updated_list[2]
    products_list[3] += updated_list[3]
    for item in products_list:
        if item < 0:
            products_list[0] += updated_list[0]
            products_list[1] += updated_list[1]
            products_list[2] += updated_list[2]
            products_list[3] -= updated_list[3]
            print("Sorry there is not enough water")
            break


def total_calculation():
    print("Please insert coins")
    quarters_qty = int(input("How many quarters?: "))
    dimes_qty = int(input("How many dimes?: "))
    nickles_qty = int(input("How many nickles?: "))
    pennies_qty = int(input("How many pennies?: "))
    total = (0.25 * quarters_qty) + (0.1 * dimes_qty) + (0.05 * nickles_qty) + (0.01 * pennies_qty)
    return total


while not turn_off_machine:
    user_selection = input("What would you like? (espresso/latte/cappuccino) ")
    if user_selection == "report":
        print(f"Water: {products_list[0]}\nMilk: {products_list[1]}\nCoffee: {products_list[2]}\nMoney: {products_list[3]}")
    elif user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino":
        updated_list = list(requsted_products(water, milk, coffee, money))
        products_update(products_list, updated_list)
        if products_list[0] > 0:
            total = total_calculation()
            if total < updated_list[3]:
                products_list[0] += updated_list[0]
                products_list[1] += updated_list[1]
                products_list[2] += updated_list[2]
                products_list[3] -= updated_list[3]
                print("Sorry, that's not enough money. Money refunded.")
            else:
                for k in drinks_info:
                    if k["name"] == user_selection:
                        price = k["price"]
                        change = round((total - price), 2)
                        print(f"Here is {change} in change\nHere is your {user_selection}. Enjoy!")
    elif user_selection == "off":
        turn_off_machine = True