"""
Assignment 5 - Game Functions (Project)
File: gamefunctions.py
Description: Module containing game logic functions for purchasing items 
             and generating random monsters, complete with test demonstrations.
"""

import random


# ----------------------------------------------------------------------
# Function Definitions
# ----------------------------------------------------------------------

def purchase_item(itemPrice: int, startingMoney: int, quantityToPurchase: int = 1):
    """
    Calculates how many items can be purchased with the available money
    and returns the quantity purchased along with remaining money.
    """
    # Determine the maximum quantity the player can actually afford
    max_affordable = startingMoney // itemPrice
    
    # Buy only up to the requested amount or what can be afforded
    num_purchased = min(quantityToPurchase, max_affordable)
    
    # Calculate leftover balance
    leftover_money = startingMoney - (num_purchased * itemPrice)
    
    return num_purchased, leftover_money


def new_random_monster():
    """
    Generates and returns a random monster represented as a dictionary
    with stats based on the chosen monster type.
    """
    monster_types = ["Goblin", "Vulture", "Dragon"]
    chosen_type = random.choice(monster_types)

    if chosen_type == "Goblin":
        monster = {
            "name": "A goblin",
            "description": "This is a lone goblin. When it notices you, it rushes at you quickly with a sharp dagger drawn.",
            "health": random.randint(10, 20),
            "power": random.randint(3, 8),
            "money": random.randint(5, 25)
        }
    elif chosen_type == "Vulture":
        monster = {
            "name": "Vulture",
            "description": "You discover a vulture eating the remains of two orcs that appear to have killed each other.",
            "health": random.randint(1, 5),
            "power": random.randint(1, 4),
            "money": random.randint(100, 1500)
        }
    else:  # Dragon
        monster = {
            "name": "Ancient Red Dragon",
            "description": "A gigantic scaled beast sleeping atop a enormous pile of gold and ancient relics.",
            "health": random.randint(150, 250),
            "power": random.randint(40, 70),
            "money": random.randint(2000, 5000)
        }

    return monster


# ----------------------------------------------------------------------
# Function Demonstrations / Main Execution
# ----------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Testing purchase_item() ===")
    
    # Call 1: Standard purchase within budget (using default quantityToPurchase = 1)
    purchased, remaining = purchase_item(341, 2112)
    print(f"Test 1 - Purchased: {purchased}, Leftover: {remaining}")

    # Call 2: Purchasing more than affordable (capped by budget)
    purchased, remaining = purchase_item(123, 201, 3)
    print(f"Test 2 - Purchased: {purchased}, Leftover: {remaining}")

    # Call 3: Completely unaffordable purchase
    purchased, remaining = purchase_item(3141, 2112, 1)
    print(f"Test 3 - Purchased: {purchased}, Leftover: {remaining}\n")

    print("=== Testing new_random_monster() ===")
    
    # Call 1: First random monster
    monster1 = new_random_monster()
    print(f"Monster 1: {monster1['name']} | HP: {monster1['health']} | Power: {monster1['power']} | Money: {monster1['money']}")
    print(f"Description: {monster1['description']}\n")

    # Call 2: Second random monster
    monster2 = new_random_monster()
    print(f"Monster 2: {monster2['name']} | HP: {monster2['health']} | Power: {monster2['power']} | Money: {monster2['money']}")
    print(f"Description: {monster2['description']}\n")

    # Call 3: Third random monster
    monster3 = new_random_monster()
    print(f"Monster 3: {monster3['name']} | HP: {monster3['health']} | Power: {monster3['power']} | Money: {monster3['money']}")
    print(f"Description: {monster3['description']}")
def print_welcome(name, width):
    """
    Prints a welcome message for the supplied name parameter,
    centered within a field of the specified width.
    
    Parameters:
        name (string): The name to include in the welcome message.
        width (int): The total width of the field for centering.
        
    Returns:
        None
    """
    message = f"Hello, {name}!"
    print(f"{message:^ {width}}")

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """
    Prints a formatted shop sign displaying a list of two items and 
    their corresponding prices, left-aligned for names and right-aligned 
    for prices with two decimal places.
    
    Parameters:
        item1Name (string): Name of the first item.
        item1Price (float): Price of the first item.
        item2Name (string): Name of the second item.
        item2Price (float): Price of the second item.
        
    Returns:
        None
    """
    print(r"/----------------------\")
    print(f"| {item1Name:<12} ${item1Price:>7.2f} |")
    print(f"| {item2Name:<12} ${item2Price:>7.2f} |")
    print(r"\----------------------/")

# Three test calls for print_welcome()
print_welcome("Jeff", 20)
print_welcome("Audrey", 30)
print_welcome("Alex", 25)

# Three test calls for print_shop_menu()
print_shop_menu("Apple", 31, "Pear", 1.234)
print_shop_menu("Egg", 0.23, "Bag of Oats", 12.34)
print_shop_menu("Milk", 4.5, "Bread", 2.99)
