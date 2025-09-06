from colorama import Fore
import os
from modules.json_tools import get_dict
from modules.helper_tools import is_pos_is_in_list
from modules.type_checker import TypeChecker

class Renamer():

    def __init__(self) -> None:
        self.commands = {
            "filter": {
                "function" : self.dir_filter,
                },
            "select": {
                "function" : self.file_select,
                },
            "rename": {
                "function" : self.file_rename,
                },
            "list_dir": {
                "function" : self.list_dir,
                },
            "set_dir": {
                "function" : self.set_dir,
                }
        }

        self.commands_info: dict = get_dict("commands.json")

        self.curr_dir: str = os.getcwd()

        self.type_checker = TypeChecker()

        self.load_all_arguments()


    def load_all_arguments(self) -> None:
        for func in self.commands.keys():
            self.commands[func]['arguments'] = self.commands_info[func]['arguments']

    def get_arguments_for_function(self, command: str, arguments: list) -> dict:
        if command not in self.commands.keys():
            print(f"{Fore.RED}[Error]{Fore.WHITE} Command module not found")
            return {}

        new_args: dict = {}
        expected_arguments: list = self.commands[command]["arguments"]

        if len(expected_arguments) == 0:
            return {}

        for i, arg_info in enumerate(expected_arguments):
            optional_arg: bool = arg_info.get("optional", True)

            if not optional_arg and not is_pos_is_in_list(i, arguments):
                return {}

            if optional_arg:
                if is_pos_is_in_list(i, arguments):
                    new_args[arg_info['arg']] = arguments[i]

                else:
                    new_args[arg_info['arg']] = arg_info['default']
            
            else:
                new_args[arg_info['arg']] = arguments[i]

        return new_args

    def run_command(self, command: str, args: dict | None = None) -> None:
        if command not in self.commands.keys():
            print(f"{Fore.RED}[Error]{Fore.WHITE} Command module not found")
            return
        
        command_info: dict = self.commands[command]

        if len(command_info['arguments']) == 0:
            self.commands[command]['function']()
        
        else:
            self.commands[command]['function'](args)

    def dir_filter(self, args: list | None) -> None:
        print("Running dir_filter")

    def file_select(self) -> None:
        print("Running file_select")

    def file_rename(self) -> None:
        print("Running file_rename")
    
    def list_dir(self, args: dict) -> None:
        self.list_all_files()
    
    def set_dir(self, args: dict) -> None:
        if not os.path.isdir(args["directory"]):
            print(f"{Fore.RED}[Error]{Fore.WHITE} Directory not found")
            return
        
        self.curr_dir = args["directory"]
        print(f"[RenameIO] set current directory as {args['directory']}")


    def list_all_files(self) -> None:
        if not self.curr_dir or not os.path.isdir(self.curr_dir):
            print(f"{Fore.RED}[Error]{Fore.WHITE} The current directory is not available")
            return

        filenames = os.listdir(self.curr_dir)
        min_leading = len(str(len(filenames)))

        if min_leading < 1:
            min_leading = 1

        for i, filename in enumerate(filenames, start=1):

            if os.path.isdir(os.path.abspath(os.path.join(self.curr_dir,filename))):
                filename = Fore.YELLOW + filename + "/" + Fore.WHITE
            
            print(f"{str(i).zfill(min_leading)}. {filename}")