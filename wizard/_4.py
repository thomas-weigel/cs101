#!/usr/bin/env python3

LOCATION = "tower"
SKILL = 0


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


def request(task):
    global LOCATION
    global SKILL
    if task == LOCATION:
        print(f"You are already in the {task}, silly wizard!")
    elif task == "tower":
        print("You travel to your modest one-story wizard tower.")
        LOCATION = "tower"
    elif LOCATION == "tower" and task == "study":
        print("You study Ye Olde Magykal Primer.")
        SKILL += 1
        print(f"Your magical skill is now {SKILL}.")
    elif task == "village":
        print("You go down to the village, roughly a 100 yards from your tower.")
        LOCATION = "village"
    elif task == "forest":
        print("You head out into the wood behind your tower.")
        LOCATION = "forest"
    elif task == "help":
        print("You can go to these locations:")
        print("  help")
        print("  quit")
        print("  tower")
        print("  village")
        print("  forest")
        print("While in the tower, you can study.")
    else:
        print(f"I don't understand {task}")


if __name__=="__main__":
    main()
