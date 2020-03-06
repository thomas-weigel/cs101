#!/usr/bin/env python3

from configparser import ConfigParser
import os.path
import readline


def main():
    set_readline()
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

        print(wiz.task(request))
        save(wiz)


def set_readline():
    import readline

    readline.set_auto_history(True)
    readline.set_completer(completion)

    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
        print("OS X")
    else:
        readline.parse_and_bind("tab: complete")
        print("wut")


def save(wiz):
    data = ConfigParser()
    data['wizard'] = {
        'save_file': wiz.save_file,
        'location': wiz.location,
        'skill': wiz.skill,
        'gold': wiz.gold,
        'library': wiz.library,
        }

    with open(wiz.save_file, 'w') as f:
        data.write(f)


def load(save_file):
    data = ConfigParser()
    if os.path.isfile(save_file):
        data.read(save_file)
    else:
        data['wizard'] = {}

    wiz = Wizard(**data['wizard'])
    return wiz


class Wizard:
    def __init__(self, save_file='wiz.save', location='tower', skill=0, gold=0, library=1):
        self.save_file = save_file
        self.location = location
        self.skill = int(skill)
        self.gold = int(gold)
        self.library = int(library)

        self.area = {
            'tower': 'You travel to your modest one-story wizard tower.',
            'village': 'You go down to the village, roughly a 100 yards from your tower.',
            'forest': 'You head out into the wood behind your tower.',
            }

    def status(self):
        return \
            f"You are at {self.location}. " \
            f"Your library is rating {self.library} and skill is rating {self.skill}. " \
            f"You have {self.gold} gold coins. " \
            f"The price of new books is {self.library * 5}. "

    def move(self, location):
        if location == self.location:
            msg = f"You are already in the {location}, silly wizard!"
        else:
            self.location = location
            msg = self.area[location]
        return msg

    def study(self):
        if self.location == "tower":
            wiz_max = self.library**2
            msg = "You study in your library.\n"
            if self.skill >= wiz_max:
                msg += "Alas, you've read these books too many times already. You need new books!"
            else:
                self.skill += 1
                msg += f"Your magical skill is now {self.skill}."
        else:
            msg = f"You cannot study in the {self.location}."
        return msg

    def work(self):
        if self.location == "village":
            self.gold += self.skill
            msg = "You work magical services to the villagers. They even pay you!\n" + \
                  f"You earn {self.skill} gold and now have {self.gold} gold total."
        else:
            msg = f"You cannot work in the {self.location}."
        return msg

    def shop(self):
        if self.location == "village":
            price = self.library * 5
            if self.gold < price:
                msg = f"You don't have enough money for books! You need {price - self.gold} more gold."
            else:
                self.gold -= price
                self.library += 1
                msg = f"You spend {price} gold on new books! Books, books, books, hahahahaha!"
        else:
            msg = f"You cannot shop in the {self.location}."
        return msg

    def task(self, request):
        if request in self.area:
            return self.move(request)
        elif request == "study":
            return self.study()
        elif request == "work":
            return self.work()
        elif request == "shop":
            return self.shop()
        elif request == "status":
            return self.status()
        elif request == "help":
            return \
                "Metagame: help, quit\n" \
                + "You can go to these locations: tower, village, forest.\n" \
                + "While in the tower, you can study.\n" \
                + "While in the village, you can work, shop."
        else:
            return f"I don't understand {request}"


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
