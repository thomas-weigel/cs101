#!/usr/bin/env python3


WIZ_LOCATION = "tower"


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
    global WIZ_LOCATION
    if task == WIZ_LOCATION:
        print(f"You are already in the {task}, silly wizard!")
    elif task == "tower":
        print("You travel to your modest one-story wizard tower.")
        WIZ_LOCATION = "tower"
    elif task == "village":
        print("You go down to the village, roughly a 100 yards from your tower.")
    elif task == "forest":
        print("You head out into the wood behind your tower.")
    elif task == "help":
        print("You can do any of the following:\n")
        print("  help")
        print("  quit")
        print("  tower")
        print("  village")
        print("  forest")
    else:
        print(f"I don't understand {task}")


if __name__=="__main__":
    main()
