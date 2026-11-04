def print_menu():
    print("""
1. Enter battle
2. Sleep
q. Quit
    """)

def enter_battle():
    print("You fought a battle!")

def rest():
    print("You took a nap, you are no longer tired and have healed.")

if __name__ == "__main__":
    while True:
        print_menu()
        menu_choice = input("What is your choice?: ").strip().lower()
        if menu_choice == "1":
            enter_battle()
        elif menu_choice == "2":
            rest()
        elif menu_choice == "q":
            break
        else:
            print("Invalid choice. Try again")
    print("Thanks for playing.")
        
    
