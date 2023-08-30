from enum import Enum
from helper import *

Items = [
    {"name": "apple", "label": "Apple", "price": 100},
    {"name": "banana", "label": "Banana", "price": 75},
    {"name": "cigarettes", "label": "Cigarettes", "price": 599},
    {"name": "bread", "label": "Bread", "price": 249},
    {"name": "sausage", "label": "Sausage", "price": 499},
    {"name": "burger", "label": "Burger", "price": 399}
]

class Actions(Enum):
    ADD = 1
    REMOVE = 2
    LISTBASKET = 3
    ITEMSFORSALE = 4
    CHECKOUT = 5

def run_actions():
    
    while True:
        print_actions(Actions)
        selection = input("Choose Item To Buy: ")
    

        selection = Actions(int(selection))
        if(selection == Actions.ADD):
            AddItem()
        elif(selection == Actions.REMOVE):
            remove_basket()
        elif(selection == Actions.LISTBASKET):
            print_basket()
        elif(selection == Actions.ITEMSFORSALE):
            print_items()
        elif(selection == Actions.CHECKOUT):
            checkout()


if __name__ == "__main__":
    run_actions()