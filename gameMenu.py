character_damage = 5
character_health = 30
gold = 10
monster1_health = 15
monster1_damage = 3

print("You are in town.")
print("Current HP:", character_health, "Current Gold:", gold)
print("What would you like to do?")
print()

def print_menu():
    print("""
1. Enter battle
2. Sleep
q. Quit
    """)

def enter_battle():
    global character_health, monster1_health, gold
    # Reset monster health each time you enter battle so it starts fresh
    monster1_health = 15
    
    print("Your first foe lies in the cave")
    print("Would you like to enter the cave?")
    battle_choice_1 = input("Yes or No: ").strip()
    
    if battle_choice_1 == "Yes": 
        print("The cave looks empty from the outside but internally the cave is lined with torches.")
        print("You see a large figure kneeling down in the center")
        print("As you approach you can start to see what is in the center. It's an Undead Zealot!")
        
        while character_health > 0 and monster1_health > 0:
            print(f"\nYour HP: {character_health} | Zealot HP: {monster1_health}")
            print("1. Attack")
            print("2. Run away")
            user_action = input("Choose your action (1 or 2): ").strip()
            
            if user_action == "1":
                monster1_health -= character_damage
                print(f"You strike the Zealot for {character_damage} damage!")
                if monster1_health > 0:
                    character_health -= monster1_damage
                    print(f"The Zealot strikes back for {monster1_damage} damage!")
            elif user_action == "2":
                print("You ran away safely back to town.")
                break # exits the while loop
            else:
                print("Unrecognized command")
                
        # Handle the outcomes after the loop ends
        if character_health <= 0:
            print("Your character passed out from your injuries!")
        elif monster1_health <= 0:
            print("You defeated the Undead Zealot!")
            gold += 3
            print("You gained 3 gold! Current Gold:", gold)
            
    elif battle_choice_1 == "No":
        print("Are you sure? This is a level 1 opponent.")

def rest():
    global character_health
    print("You took a nap, you are no longer tired and have healed.")
    character_health = 30  # Restore health fully on rest
    print("Current HP restored to:", character_health)

if __name__ == "__main__":
    while True:
        print("\n--------------------------------")
        print("Current HP:", character_health, "| Current Gold:", gold)
        print_menu()
        menu_choice = input("What is your choice?: ").strip().lower()
        if menu_choice == "1":
            enter_battle()
        elif menu_choice == "2":
            rest()
        elif menu_choice == "q":
            print("Thanks for playing.")
            break
        else:
            print("Invalid choice. Try again")
