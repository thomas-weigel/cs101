#!/usr/bin/env python3

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
    print(f"Performed {request}")


if __name__=='__main__':
    main()
