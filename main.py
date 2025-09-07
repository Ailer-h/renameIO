import colorama
from colorama import Fore
import modules.json_tools as json_tools
from modules.commands import Renamer
from modules.logger import log_error

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
        args: list = []

        if " " in command:
            command, *args = command.split()


        if command not in options.keys():
            log_error("Choose a command from the list", log_id="Invalid command")
            continue

        elif command == "quit":
            print(f"{Fore.BLUE}Ending script...")
            break

        elif command not in ch.commands:
            log_error("Command module not found")
            continue
            
        print(f"Running {Fore.BLUE + command + Fore.WHITE}...")

        command_args: dict = ch.get_arguments_for_function(command, args)
        min_required_args = ch.get_minimum_required_args_for_function(command)

        if len(command_args) < min_required_args:
            log_error(f"The function {command} expects {min_required_args} arguments.")
            continue

        if len(command_args) == 0:
            ch.run_command(command)

        else:
            ch.run_command(command, command_args)


if __name__ == "__main__":
    main()
