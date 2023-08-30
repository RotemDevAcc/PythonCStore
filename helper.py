from app import Items
import os

def ClearConsole():
    os.system("cls" if os.name == "nt" else "clear")

def print_actions(actions):
    for action in actions:
        print(f"{action.name} - {action.value}")

def print_items():
    print("-" * 43)
    print("Items For Sale")
    print("-" * 43)
    for i,value in enumerate(Items):
        print(f"{i+1}. {value['label']} - ${value['price']}")

    print("-" * 43)

def add_commas(number):
    """
    Format a number with commas as thousands separators.

    Args:
    number (int or float): The number to format.

    Returns:
    str: The formatted number as a string.
    """
    # Check if the input is a valid number
    if not (isinstance(number, int) or isinstance(number, float)):
        return "Invalid input"
    
    # Format the number with commas
    formatted_number = "{:,}".format(number)
    
    return formatted_number

ShoppingBasket = []

def AddItem():

    print_items()
    selection = int(input("Select Item: "))
    found = None
    for i,value in enumerate(Items):
        if i + 1 == selection:
            found = value
            break
    
    if found:
        amount = int(input(f"Amount of {found['label']} To Buy (${add_commas(found['price'])} Each): "))
        total_price = amount * found['price']

        # Check if the item is already in the ShoppingBasket
        item_in_basket = None
        for basket_item in ShoppingBasket:
            if basket_item['name'] == found['name']:
                item_in_basket = basket_item
                break

        if item_in_basket:
            # If the item is already in the basket, update the quantity and total price
            item_in_basket['amount'] += amount
            item_in_basket['total_price'] += total_price
            print(f"Updated {item_in_basket['amount']} {found['label']} in Shopping Basket for a total of ${add_commas(item_in_basket['total_price'])}")
        else:
            # If the item is not in the basket, add it as a new item
            ShoppingBasket.append({"name": found['name'], "label": found['label'], "price": found['price'], "amount": amount, "total_price": total_price})
            print(f"Added {amount} {found['label']} to Shopping Basket for a total of ${add_commas(total_price)}")
    else:
        print("Invalid selection. Please choose a valid item.")

def remove_basket():
    print("-" * 43)
    print("Remove Items from Shopping Basket")
    print("-" * 43)
    
    if not ShoppingBasket:
        print("Your basket is empty.")
    else:
        # Print items in the shopping basket with numbers
        for i, item in enumerate(ShoppingBasket):
            print(f"{i + 1}. {item['label']} - Quantity: {item['amount']} - Total Price: ${item['total_price']}")
        
        # Ask the client to select an item to remove by number
        try:
            selection = int(input("Enter the number of the item you want to remove: "))
            if 1 <= selection <= len(ShoppingBasket):
                removed_item = ShoppingBasket.pop(selection - 1)
                print(f"Removed {removed_item['amount']} {removed_item['label']} from the basket.")
            else:
                print("Invalid selection. Please choose a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
def print_basket():
    print("-" * 43)
    print("Shopping Basket")
    print("-" * 43)
    
    if not ShoppingBasket:
        print("Your basket is empty.")
    else:
        for i, item in enumerate(ShoppingBasket):
            print(f"{i + 1}. {item['label']} - Quantity: {item['amount']} - Total Price: ${item['total_price']}")

def checkout():

    yes = confirm()
    if(not yes):
        print("Checkout Declined")
        return
    payprice = get_totalprice()

    if(payprice == 0):
        print("ERROR: Nothing Was Found in your basket")
        return

    print(f"Bought {len(ShoppingBasket)} Item{'s' if len(ShoppingBasket) != 1 else ''} For ${add_commas(payprice)}")
        

def get_totalprice():
    payprice = 0
    for i, item in enumerate(ShoppingBasket):
        payprice += item['total_price']
    
    return payprice

def confirm():
    print_basket()
    print(f"Total Price: {add_commas(get_totalprice())}")
    selection = input("Are You Sure You Want To Continue? (1 To Continue): ")
    if(selection == "1"):
        return True
    
    return False