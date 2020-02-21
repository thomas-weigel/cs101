#!/usr/bin/env python3

def main():
    while True:
        task = input("> ")
        if task == "quit":
            break

        print(f"Performed {task}")


if __name__=='__main__':
    main()
