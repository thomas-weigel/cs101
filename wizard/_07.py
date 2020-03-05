#!/usr/bin/env python3

import readline


def main():
    readline.set_auto_history(True)
    readline.set_completer(completion)
    readline.parse_and_bind("tab: complete")
    wiz = Wizard()

    while True:
        try:
            request = input("> ")
            if request == "quit":
                print("Goodbye!")
                break
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        task(wiz, request)


class Wizard:
    def __init__(self, location='tower', skill=0, gold=0, library=1):
        self.location = location
        self.skill = skill
        self.gold = gold
        self.library = library

    def status(self):
        print(
            f"You are at {self.location}. "
            f"Your library is rating {self.library} and skill is rating {self.skill}. "
            f"You have {self.gold} gold coins."
            )


def task(wiz, request):
    if request == wiz.location:
        print(f"You are already in the {request}, silly wizard!")

    elif request == "tower":
        print("You travel to your modest one-story wizard tower.")
        wiz.location = "tower"
    elif wiz.location == "tower" and request == "study":
        print("You study in your library.")
        wiz_max = wiz.library**2
        if wiz.skill >= wiz_max:
            print("Alas, you've read these books too many times already. You need new books!")
        else:
            wiz.skill += 1
            print(f"Your magical skill is now {wiz.skill}.")

    elif request == "village":
        print("You go down to the village, roughly a 100 yards from your tower.")
        print(f"The cost of new books is currently {wiz.library * 5} gold.")
        wiz.location = "village"
    elif wiz.location == "village" and request == "provide":
        print("You provide magical services to the villagers. They even pay you!")
        wiz.gold += wiz.skill
        print(f"You earn {wiz.skill} gold and now have {wiz.gold} gold total.")
    elif wiz.location == "village" and request == "shop":
        price = wiz.library * 5
        if wiz.gold < price:
            print(f"You don't have enough money for books! You need {price - wiz.gold} more gold.")
        else:
            print(f"You spend {price} gold on new books! Books, books, books, hahahahaha!")
            wiz.gold -= price
            wiz.library += 1

    elif request == "forest":
        print("You head out into the wood behind your tower.")
        wiz.location = "forest"

    elif request == "status":
        wiz.status()
    elif request == "help":
        print("Metagame: help, quit")
        print("You can go to these locations: tower, village, forest.")
        print("While in the tower, you can study.")
        print("While in the village, you can provide, shop.")
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
        'status',
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
