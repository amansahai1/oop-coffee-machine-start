from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_status = True
new_menu = Menu()
new_coffee_maker = CoffeeMaker()
new_money_machine = MoneyMachine()
# new_menu_item = MenuItem()
while coffee_machine_status:
    user_selection = input(f"What would you like? {new_menu.get_items()} ").lower()

    if user_selection == "off":
        coffee_machine_status = False
    elif user_selection == "report":
        new_coffee_maker.report()
    else:
        new_menu_item = new_menu.find_drink(user_selection)
        if new_coffee_maker.is_resource_sufficient(new_menu_item):
            cost_of_Drink = new_menu_item.cost
            money_enough = new_money_machine.make_payment(cost_of_Drink)
            if money_enough:
                print("Money is enough")
                new_coffee_maker.make_coffee(new_menu_item)





