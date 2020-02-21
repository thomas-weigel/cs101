#!/usr/bin/env python3

import readline


WIZ_LOCATION = "tower"
WIZ_SKILL = 0
WIZ_GOLD = 0
WIZ_LIBRARY = 1

def main():
    readline.set_auto_history(True)
    readline.set_completer(completion)

    while True:
        try:
            request = input("> ")
            if request == "quit":
                print("Goodbye!")
                break
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        task(request)


def task(request):
    global WIZ_LOCATION
    global WIZ_SKILL
    global WIZ_GOLD
    global WIZ_LIBRARY

    if request == WIZ_LOCATION:
        print(f"You are already in the {request}, silly wizard!")
    elif request == "tower":
        print("You travel to your modest one-story wizard tower.")
        WIZ_LOCATION = "tower"
    elif WIZ_LOCATION == "tower" and request == "study":
        print("You study in your library.")
        wiz_max = WIZ_LIBRARY**2
        if WIZ_SKILL >= wiz_max:
            print("Alas, you've read these books too many times already. You need new books!")
        else:
            WIZ_SKILL += 1
            print(f"Your magical skill is now {WIZ_SKILL}.")
    elif request == "village":
        print("You go down to the village, roughly a 100 yards from your tower.")
        print(f"The cost of new books is currently {WIZ_LIBRARY * 5} gold.")
        WIZ_LOCATION = "village"
    elif WIZ_LOCATION == "village" and request == "work":
        print("You work magical services to the villagers. They even pay you!")
        WIZ_GOLD += WIZ_SKILL
        print(f"You earn {WIZ_SKILL} gold and now have {WIZ_GOLD} gold total.")
    elif WIZ_LOCATION == "village" and request == "shop":
        price = WIZ_LIBRARY * 5
        if WIZ_GOLD < price:
            print(f"You don't have enough money for books! You need {price - WIZ_GOLD} more gold.")
        else:
            print(f"You spend {price} gold on new books! Books, books, books, hahahahaha!")
            WIZ_GOLD -= price
            WIZ_LIBRARY += 1
    elif request == "forest":
        print("You head out into the wood behind your tower.")
        WIZ_LOCATION = "forest"
    elif request == "help":
        print("Metagame: help, quit")
        print("You can go to these locations: tower, village, forest.")
        print("While in the tower, you can study.")
        print("While in the village, you can work, shop.")
    else:
        print(f"I don't understand {request}")


def completion(text, state):
    options = [
        'tower',
        'village',
        'forest',
        'study',
        'work',
        'shop',
        'help',
        'quit',
        ]

    matching_options = []
    for opt in options:
        if opt.startswith(text):
            matching_options.append(opt)

    if state >= len(matching_options):
        return None

    return matching_options[state]


if __name__=="__main__":
    main()
