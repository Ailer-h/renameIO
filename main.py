from colorama import Fore
import os
import modules.json_tools as json_tools

options: dict = json_tools.get_dict("commands.json")

def get_full_string(option: tuple) -> str:
    return " : ".join(option)

def show_commands(commands: dict) -> None:

    biggest_key: int = sorted(map(len, commands.keys()))[-1]
    biggest_value: int = sorted(map(len, commands.values()))[-1]

    for key, value in commands.items():
        curr_line = f"{key} : {value}"

        before = biggest_key - len(key)
        after = biggest_value - len(value)

        curr_line = f"{Fore.BLUE + key + Fore.WHITE}{' ' * before} : {' ' * after}{value}"

        print(curr_line)

def main():
    print(f"Running {Fore.BLUE}RenameIO{Fore.WHITE} v0.1")
    print("-" * 30)
    print("Commands:")
    show_commands(options)

if __name__ == "__main__":
    main()
