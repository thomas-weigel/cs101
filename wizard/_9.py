#!/usr/bin/env python3

import os.path
import readline


def main():
    readline.set_auto_history(True)
    readline.set_completer(completion)
    wiz = load('wiz.save')

    while True:
        try:
            request = input("> ")
            if request == "quit":
                print("Goodbye!")
                break
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        wiz.task(request)
        save(wiz)


def save(wiz):
    data = {
        'save_file': wiz.save_file,
        'location': wiz.location,
        'skill': wiz.skill,
        'gold': wiz.gold,
        'library': wiz.library,
        }

    with open(wiz.save_file, 'w') as f:
        for key in data:
            f.write(f"{key}:{data[key]}\n")


def load(save_file):
    data = {}
    if os.path.isfile(save_file):
        with open(save_file, 'r') as f:
            for line in f:
                key, value = line.strip().split(':')
                if key in ('skill', 'gold', 'library'):
                    value = int(value)
                data[key] = value

    wiz = WizardState(**data)
    return wiz


class WizardState:
    def __init__(self, save_file='wiz.save', location='tower', skill=0, gold=0, library=1):
        self.save_file = save_file
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

    def task(self, request):
        if request == self.location:
            print(f"You are already in the {request}, silly wizard!")

        elif request == "tower":
            print("You travel to your modest one-story wizard tower.")
            self.location = "tower"
        elif self.location == "tower" and request == "study":
            print("You study in your library.")
            wiz_max = self.library**2
            if self.skill >= wiz_max:
                print("Alas, you've read these books too many times already. You need new books!")
            else:
                self.skill += 1
                print(f"Your magical skill is now {self.skill}.")

        elif request == "village":
            print("You go down to the village, roughly a 100 yards from your tower.")
            print(f"The cost of new books is currently {self.library * 5} gold.")
            self.location = "village"
        elif self.location == "village" and request == "work":
            print("You work magical services to the villagers. They even pay you!")
            self.gold += self.skill
            print(f"You earn {self.skill} gold and now have {self.gold} gold total.")
        elif self.location == "village" and request == "shop":
            price = self.library * 5
            if self.gold < price:
                print(f"You don't have enough money for books! You need {price - self.gold} more gold.")
            else:
                print(f"You spend {price} gold on new books! Books, books, books, hahahahaha!")
                self.gold -= price
                self.library += 1

        elif request == "forest":
            print("You head out into the wood behind your tower.")
            self.location = "forest"

        elif request == "status":
            self.status()
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
