import random
import time

def clear_screen():
    print("\n" * 100)

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    clear_screen()
    slow_print("You find yourself at the entrance of an old, decrepit mansion.")
    slow_print("A chilling wind blows through the trees, and the front door creaks open.")
    slow_print("Do you dare to enter? (yes/no)")
    
def get_choice(prompt, options):
    choice = input(prompt).lower().strip()
    while choice not in options:
        print("Invalid choice. Please try again.")
        choice = input(prompt).lower().strip()
    return choice

def enter_mansion():
    clear_screen()
    slow_print("You step inside the mansion. The air is thick with dust and the smell of mildew.")
    slow_print("There are three doors in front of you, each leading to a different room:")
    slow_print("1. The Library")
    slow_print("2. The Dining Hall")
    slow_print("3. The Cellar")
    
def library():
    clear_screen()
    slow_print("You enter the Library. It's dimly lit and filled with towering bookshelves.")
    slow_print("A single book lies open on a desk. It seems to be beckoning you.")
    slow_print("Do you read the book or search the shelves? (read/search)")

    choice = get_choice("> ", ['read', 'search'])
    if choice == 'read':
        slow_print("The book contains dark spells and incantations.")
        slow_print("As you read, you hear whispering voices around you. The lights flicker.")
        slow_print("Suddenly, a ghostly figure appears! You must run!")
        return False
    else:
        slow_print("You search the shelves and find a hidden compartment.")
        slow_print("Inside, you find a rusty key. This might be useful.")
        return True

def dining_hall():
    clear_screen()
    slow_print("You enter the Dining Hall. A long, dust-covered table is set with broken china.")
    slow_print("You notice a strange shadow moving across the wall.")
    slow_print("Do you investigate the shadow or check under the table? (investigate/check)")

    choice = get_choice("> ", ['investigate', 'check'])
    if choice == 'investigate':
        slow_print("The shadow leads you to a wall with a hidden passage.")
        slow_print("You find a dusty old journal with notes about the mansion's dark past.")
        slow_print("The passage seems to lead to the basement.")
        return True
    else:
        slow_print("You check under the table and find a hidden trapdoor.")
        slow_print("You open it and find an old, rusty knife. It might be useful for defense.")
        return True

def cellar():
    clear_screen()
    slow_print("You enter the Cellar. The air is cold and damp.")
    slow_print("You see a large crate and a flickering lantern on a wooden shelf.")
    slow_print("Do you open the crate or inspect the lantern? (open/inspect)")

    choice = get_choice("> ", ['open', 'inspect'])
    if choice == 'open':
        slow_print("You open the crate and find it full of old wine bottles.")
        slow_print("Suddenly, a cold breeze sweeps through the room, and you hear footsteps behind you.")
        slow_print("A dark figure emerges from the shadows. You must escape!")
        return False
    else:
        slow_print("You inspect the lantern and find a hidden compartment with a map of the mansion.")
        slow_print("The map shows secret passages and hidden rooms.")
        return True

def final_room(key_found, journal_found, map_found):
    clear_screen()
    slow_print("You find yourself in a dimly lit final room with a locked door.")
    if key_found:
        slow_print("You use the rusty key to unlock the door.")
        slow_print("The door creaks open, and you step into a hidden chamber.")
        slow_print("In the chamber, you find a way to escape the mansion.")
        slow_print("Congratulations, you've escaped the haunted mansion!")
    else:
        slow_print("You don't have the key to open the door.")
        slow_print("Without the key, you must find another way out.")
        if journal_found:
            slow_print("You use the journal to find a secret passage behind a bookshelf.")
            slow_print("The passage leads to an escape route.")
            slow_print("Congratulations, you've escaped the haunted mansion!")
        elif map_found:
            slow_print("You use the map to find a hidden exit.")
            slow_print("The exit leads to safety.")
            slow_print("Congratulations, you've escaped the haunted mansion!")
        else:
            slow_print("Without any special items, you are trapped.")
            slow_print("The mansion's ghosts close in, and you have no choice but to remain inside.")
            slow_print("Game Over.")

def play_game():
    intro()
    choice = get_choice("> ", ['yes', 'no'])
    if choice == 'no':
        slow_print("You decide not to enter the mansion. Maybe another time.")
        return
    
    enter_mansion()
    key_found = False
    journal_found = False
    map_found = False
    
    while True:
        room = get_choice("Which room do you want to enter? (library/dining/cellar) ", ['library', 'dining', 'cellar'])
        if room == 'library':
            key_found = library()
        elif room == 'dining':
            journal_found = dining_hall()
        elif room == 'cellar':
            map_found = cellar()
        
        if not (key_found or journal_found or map_found):
            slow_print("You are lost and unable to find a way out.")
            slow_print("Game Over.")
            return
        
        if key_found and (journal_found or map_found):
            break
    
    final_room(key_found, journal_found, map_found)

if __name__ == "__main__":
    play_game()
