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

        wiz.task(request)


class Wizard:
    def __init__(self, location='tower', skill=0, gold=0, library=1):
        self.location = location
        self.skill = skill
        self.gold = gold
        self.library = library

        self.area = {
            'tower': 'You travel to your modest one-story wizard tower.',
            'village': 'You go down to the village, roughly a 100 yards from your tower.',
            'forest': 'You head out into the wood behind your tower.',
            }

    def status(self):
        print(
            f"You are at {self.location}. "
            f"Your library is rating {self.library} and skill is rating {self.skill}. "
            f"You have {self.gold} gold coins. "
            f"The price of new books is {self.library * 5}."
            )

    def move(self, location):
        if location == self.location:
            print(f"You are already in the {location}, silly wizard!")
        else:
            print(self.area[location])
            self.location = location

    def study(self):
        if self.location == "tower":
            print("You study in your library.")
            wiz_max = self.library**2
            if self.skill >= wiz_max:
                print("Alas, you've read these books too many times already. You need new books!")
            else:
                self.skill += 1
                print(f"Your magical skill is now {self.skill}.")
        else:
            print(f"You cannot study in the {self.location}.")

    def work(self):
        if self.location == "village":
            print("You work magical services to the villagers. They even pay you!")
            self.gold += self.skill
            print(f"You earn {self.skill} gold and now have {self.gold} gold total.")
        else:
            print(f"You cannot work in the {self.location}.")

    def shop(self):
        if self.location == "village":
            price = self.library * 5
            if self.gold < price:
                print(f"You don't have enough money for books! You need {price - self.gold} more gold.")
            else:
                print(f"You spend {price} gold on new books! Books, books, books, hahahahaha!")
                self.gold -= price
                self.library += 1
        else:
            print(f"You cannot shop in the {self.location}.")

    def task(self, request):
        if request in self.area:
            self.move(request)
            self.status()
        elif request == "study":
            self.study()
        elif request == "work":
            self.work()
        elif request == "shop":
            self.shop()
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
