# NAME: khadega algafri
# DATE: February 21, 2026
#I certify that this work is my own: 
# SIGNATURE: khadegaalgafri

def create_rooms():
    rooms = {
        "library": {
            "description": "A dusty library with ancient books.",
            "exits": {"north": "hallway"},
            "details": {
                "desk": "an old oak desk. You find a **rusty key** in the drawer!",
                "bookshelf": "Shelves of books. One looks like a secret lever."
            },
            "items": ["rusty key"],
            "visited": False
        }, 
        "hallway": {
            "description": "A narrow hallway",
            "exits": {"south": "library", "west": "garden"},
            "details": {
                "painting": "You see a painting",
            },
            "visited": False
        },
        "garden": {
            "description": "An overgrown garden with crumbling fountain",
            "exits": {"east": "hallway"},
            "details": {
                "fountain": "You spot a silver shard in the shimmering water",
                "statue": "It looks to be a Knight pointing North."
            },
            "items": ["silver shard"],
            "visited": False
        }
    }
    return rooms


def create_npcs():
    """
    non-player character (computer controlled - character)

    NPC's to have the following characteristics
    - locations
    - be able to talk (text dialogue)
    - item: they may be able to offer users an item 
    - TALKED? have we spoken to them before

    """
    npcs = {
        "librarian": {
            "location": "library",
            "dialogue": "The safe code is hidden in the oldest book on the third shelf. ",
            "item": "ancient book",
            "talked": False,
        },
        "ghost": {
            "location": "hallway",
            "dialogue": "I once guarded this mansion. The master key is in three pieces.",
            "item": "ghost token",
            "talked": False
        },
        "gardener": {
            "location": "garden",
            "dialogue": "The fountain holds secrets. Look closely at the inscription.",
            "item": None,
            "talked": False
        }
    }
    return npcs

def talk_to_npc(npc_name, npcs, current_room, inventory):
    """
    have a simple conversation with an npc 
    one exchange with each npc
    """
    npc_name = npc_name.lower()

    if npc_name not in npcs:
        available = ", ".join(npcs.keys())
        print(f"\nNo NPCS named '{npc_name}. Try {available}")
        return False
    
    npc = npcs[npc_name]
    
    if npc["location"] != current_room: 
        print(f"\n{npc_name.title()} is not in this room.")
        return False
    # npc is available and in the room.. we can have a dialogue
    # show the dialogue

    print(f"\n{npc_name.title()}: \"{npc['dialogue']}\"")

    # give an item
    if npc["item"] and not npc["talked"]:
        print(f"\n{npc_name.title()} gives you: {npc['item']}")
        inventory.append(npc['item'])
        npc["talked"] = True
    elif npc["talked"]:
        print(f"\n{npc_name.title()}: I've already spoken with you and told you what i know")
    return True    

def list_npcs_in_room(current_room, npcs):
    """show which NPCs are in the room"""
    # list comprehension - technique in python for generating a list by providing rules for the # members of the list.
    npcs_here = [name for name, data in npcs.items() if data["location"] == current_room ]

    if npcs_here:
        print("\nPeople are here")
        for npc in npcs_here:
            print(f" - {npc.title()}")
        return True
    return False


def display_inventory(inventory):
    """
    Display the user's current inventory.
    """ 
    if not inventory:
        print("\nYour inventory is empty. ")
    else:
        print("\nYour inventory:")
        for i, item in enumerate(inventory, 1):
            print(f"  {i}. {item}")
def examine_object(obj_name, current_room_data ,inventory):
    """
    Examine an object and maybe add it to our inventory. 
    Return True if item added. otherwise it will return False
    """
    obj_name = obj_name.lower()

    if obj_name in current_room_data['details']:
        print(f"\n{current_room_data['details'][obj_name]}")
        if "items" in current_room_data and len(current_room_data["items"]) > 0:
            item = current_room_data["items"].pop(0)
            print(f"Added {item} to inventory")
            inventory.append(item)

    else:
        print(f"You don't see any {obj_name} here.")

    # if obj_name == "desk":
    #     print("You seach the desk drawers...")
    #     if "rusty key" not in inventory:
    #         print("You found a rusty key!")
    #         inventory.append("rusty key")
    #         return True
    #     else:
    #         print("The desk is empty now")
    #         return False
    # elif obj_name == "bookshelf":
    #     print("\nYou examine the bookshelf...")
    #     if "mysterious book" not in inventory:
    #         print("One book seems different. You take it.")
    #         inventory.append("mysterious book")
    #         return True
    #     else:
    #         print("Just dusty old books.")
    #         return False
    
    # else:
    #     print(f"\nYou can't examine '{obj_name}'. Try 'desk' or 'bookshelf'.")
    #     return False

def describe_room(room_name, rooms, npcs):
    """
    describe the current room to the player
    """
    room = rooms[room_name]

    print("\n" + "="*50)
    print(f"LOCATION: {room_name.upper()}")
    print("\n" + "="*50)
    print(room["description"])

    # show all objects in the room
    if room.get("details"):
        print("\nYou see:")
        for obj in room["details"]:
            print(f"  - {obj}")
    list_npcs_in_room(room_name, npcs)

    # have we visited this room before
    if not room.get("visited"):
        print("\n (First time here)")
        room["visited"] = True

 # SECTION 1 & 2: Database and List Comprehensions 
def create_item_database():# this is a new function to create a database of items in the game
    """
    Create a dictionary describing all items in the game.
    """
    items = {
        "rusty key": {
            "description": "An old brass key covered in rust. It looks fragile but might still unlock something important.",
            "value": 50,
            "category": "key"
        },
        "mysterious book": {
            "description": "A dark leather-bound book with strange symbols on the cover. The pages whisper when opened.",
            "value": 120,
            "category": "book"
        },
        "ancient book": {
            "description": "A dusty tome filled with forgotten knowledge from a lost civilization.",
            "value": 150,
            "category": "book"
        },
        "ghost token": {
            "description": "A glowing token that feels icy in your palm. It seems linked to the spirit world.",
            "value": 200,
            "category": "artifact"
        },
        "golden amulet": {
            "description": "A beautifully crafted amulet that radiates a faint magical warmth.",
            "value": 300,
            "category": "treasure"
        },
        "silver shard": {
            "description": "A sharp silver fragment shimmering with strange energy, pulled from the fountain water.",
            "value": 75,
            "category": "relic"
        }
    }
    return items 

def get_valuable_items(inventory, items_db):# inventory is a list of item names, items_db is the dictionary we just created
    """
    Return list of items in inventory worth more than 40 points.
    Uses list comprehension.
    """
    valuable = [item for item in inventory if items_db[item]["value"] > 40]
    return valuable
def get_untalked_npcs(npcs):# untalked npcs are npcs where "talked" is False
    """
    SECTION 2: Return list of NPC names the player hasn't talked to yet.
    Uses list comprehension.
    """
    untalked = [name.title() for name, data in npcs.items() if not data["talked"]]
    return untalked
 # SECTION 4: New Functionality
def examine_inventory_item(inventory, items_db):# this function allows the player to examine an item in their inventory and see its details from the items database
    """
    Let player examine an item in their inventory for details.
    """
    item_name = input("\nWhich item do you want to examine? ").lower()

    if item_name not in inventory:
        print(f"\nYou don't have '{item_name}' in your inventory.")
        return False

    if item_name not in items_db:
        print(f"\nNo information available about '{item_name}'.")
        return False

# Display Details
    data = items_db[item_name]
    print("\n" + item_name.title())
    print(f"Description: {data['description']}")
    print(f"Value: {data['value']} points")
    print(f"Category: {data['category']}")
# Bonus Logic: Check if it's "Valuable"
    if item_name in get_valuable_items([item_name], items_db):
        print("★ This is a valuable item! ★")

    return True
def main(): # main function to run the game loop
    """
    Welcome to our Escape Room. 
    The challenge is for users to use the tools to "escape" 
    """
    npcs = create_npcs()
    rooms = create_rooms()
    item_db = create_item_database() #update our main function to create the item database and pass it to the examine inventory function
    
    current_room = "library" # every time we start the game in the library

    # game variables

    player_name = input("what's your name, challenger? ")
    print(f"\nWelcome, {player_name}.   \nLet's get started on your adventure... ") 

    # initializing variables
    game_over = False
    # escaped = False 
    moves = 0
    inventory = [] #empty list?

    while not game_over:
        print("\n" + "="*50)
        print("What do you want to do?")
        print("1. Look around the room")
        print("2. Move to another room")
        print("3. Check your inventory")
        print("4. Examine an object")
        print("5. Talk to someone")
        print("6. Examine an item in your inventory")
        print("7. Try to escape")
        print("8. Quit game")
    
        choice = input("Enter your choice (1-8): ")
        # print(f"DEBUG you chose number {choice}")
        moves += 1

        if choice == "1":
            # WE STILL HAD SOME OF THE OLD HARD-CODED CHOICES HERE
            # NOW WE CAN JUST USE THE FUNCTION WE BUILT!
            describe_room(current_room, rooms, npcs)
        elif choice == "2":
            direction = input("\nWhich direction? (north/south/east/west): ").lower()
            
            room = rooms[current_room]
            if direction in room["exits"]:
                current_room = room["exits"][direction]
                print(f"\nYou move {direction}...")
                describe_room(current_room, rooms, npcs)
            else:
                print(f"\nYou can't go {direction} from here.")
                moves -= 1 
        elif choice == "3":
            untalked = get_untalked_npcs(npcs) # new function to get list of untalked npcs
            if untalked:
                print(f"\nYou still need to speak with: {', '.join(untalked)}")
            display_inventory(inventory)
        elif choice == "4":
            obj = input("\nWhat do you want to examine? ")
            examine_object(obj, rooms[current_room], inventory)
        elif choice == "5":
            who = input("\nTalk to whom? ")
            talk_to_npc(who, npcs, current_room, inventory)
        elif choice == "6": # new choice to examine inventory items
            examine_inventory_item(inventory, item_db)
            moves -= 1 # don't count examining inventory as a move
            continue
        elif choice == "7":
            print("\nYou try the door...")
            if "rusty key" in inventory:
                print("The rusty key works! The door creaks open...")
                print(f"\nCongratulations, {player_name}! You escaped in {moves} moves!")
                # escaped = True
                game_over = True
            else:
                print("The door is locked. You need to find a key!")
        elif choice == "8":
            print(f"\nThanks for playing, {player_name}! You made {moves} moves.")
            game_over = True

        else: 
            print("\nInvalid choice. Try again ")
            moves -= 1

    print("\nGame Over!")

if __name__ == "__main__":
    main()  

    
    