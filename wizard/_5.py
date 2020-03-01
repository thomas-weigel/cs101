#!/usr/bin/env python3

LOCATION = "tower"
SKILL = 0
GOLD = 0
LIBRARY = 1

def main():
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
    global LOCATION
    global SKILL
    global GOLD
    global LIBRARY

    if request == LOCATION:
        print(f"You are already in the {request}, silly wizard!")
    elif request == "tower":
        print("You travel to your modest one-story wizard tower.")
        LOCATION = "tower"
    elif LOCATION == "tower" and request == "study":
        print("You study in your library.")
        wiz_max = LIBRARY**2
        if SKILL >= wiz_max:
            print("Alas, you've read these books too many times already. You need new books!")
        else:
            SKILL += 1
            print(f"Your magical skill is now {SKILL}.")
    elif request == "village":
        print("You go down to the village, roughly a 100 yards from your tower.")
        print(f"The cost of new books is currently {LIBRARY * 5} gold.")
        LOCATION = "village"
    elif LOCATION == "village" and request == "provide":
        print("You provide magical services to the villagers. They even pay you!")
        GOLD += SKILL
        print(f"You earn {SKILL} gold and now have {GOLD} gold total.")
    elif LOCATION == "village" and request == "shop":
        price = LIBRARY * 5
        if GOLD < price:
            print(f"You don't have enough money for books! You need {price - GOLD} more gold.")
        else:
            print(f"You spend {price} gold on new books! Books, books, books, hahahahaha!")
            GOLD -= price
            LIBRARY += 1
    elif request == "forest":
        print("You head out into the wood behind your tower.")
        LOCATION = "forest"
    elif request == "help":
        print("Metagame: help, quit")
        print("You can go to these locations: tower, village, forest.")
        print("While in the tower, you can study.")
        print("While in the village, you can provide, shop.")
    else:
        print(f"I don't understand {request}")


if __name__=="__main__":
    main()
