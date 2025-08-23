import colorama
from colorama import Fore
import os
import modules.json_tools as json_tools
from modules.commands import Renamer

options: dict = json_tools.get_dict("commands.json")
ch = Renamer()

colorama.init(autoreset=True)

def show_commands(commands: dict) -> None:

    biggest_key: int = sorted(map(len, commands.keys()))[-1]

    for key, value in commands.items():

        before = biggest_key - len(key)

        curr_line = f"{Fore.BLUE + key + Fore.WHITE}{' ' * before} : {value['description']}"

        print(curr_line)

def main():
    print(f"Running {Fore.BLUE}RenameIO{Fore.WHITE} v0.1")
    print("-" * 30)
    print("Commands:")
    show_commands(options)

    while True:
        
        command = input("> ")
        args: list | None = None

        if " " in command:
            command, *args = command.split()

        if command not in options.keys():
            print(f"{Fore.RED}[Invalid command]{Fore.WHITE} Choose a command from the list")
            continue

        elif command == "quit":
            print(f"{Fore.BLUE}Ending script...")
            break

        elif command not in ch.commands:
            print(f"{Fore.RED}[Error]{Fore.WHITE} Command module not found")
            continue
            
        print(f"Running {Fore.BLUE + command + Fore.WHITE}...")

        ch.run_command(command, args)

if __name__ == "__main__":
    main()
