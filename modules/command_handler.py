from colorama import Fore
import os
from modules.json_tools import get_dict
from modules.helper_tools import is_pos_is_in_list
from modules.type_checker import TypeChecker
from modules.logger import log_error, log_info
from modules.filter import Filter
from modules.renaming import Renamer

class CommandHandler():

    def __init__(self) -> None:
        self.commands = {
            "clear_filter" : {
                "function" : self.clear_filter,
            },
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
                },
            "set_pressets_dir": {
                "function" : self.set_pressets_dir,
                },
            "list_press": {
                "function" : self.list_press,
                },
            "presset": {
                "function" : self.presset,
                },
        }

        self.filter = Filter()
        self.renamer = Renamer()

        self.commands_info: dict = get_dict("commands.json")
        self.user_preferences: dict = get_dict("preferences.json")

        self.curr_dir: str = os.getcwd()
        self.pressets_dir: str = os.path.join(os.getcwd(), "pressets")

        self.type_checker = TypeChecker()

        self.load_all_arguments()


    def load_all_arguments(self) -> None:
        for func in self.commands.keys():
            self.commands[func]['arguments'] = self.commands_info[func]['arguments']

    def get_arguments_for_function(self, command: str, arguments: list) -> dict:
        if command not in self.commands.keys():
            log_error("Command module not found")
            return {}

        new_args: dict = {}
        expected_arguments: list = self.commands[command]["arguments"]
        min_expected_args = self.get_minimum_required_args(expected_arguments)

        if len(expected_arguments) == 0 or len(arguments) < min_expected_args:
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
    
    def get_minimum_required_args_for_function(self, command: str) -> int:
        if command not in self.commands.keys():
            log_error("Command module not found")
            return -1
        
        return self.get_minimum_required_args(self.commands[command]["arguments"])

    def get_minimum_required_args(self, expected_args: list) -> int:
        min_required: int = 0

        for arg in expected_args:
            if not arg['optional']:
                min_required += 1

        return min_required

    def run_command(self, command: str, args: dict | None = None) -> None:
        if command not in self.commands.keys():
           log_error("Command module not found")
           return
        
        command_info: dict = self.commands[command]

        if len(command_info['arguments']) == 0:
            self.commands[command]['function']()
        
        else:
            self.commands[command]['function'](args)

    def dir_filter(self) -> None:
        if self.user_preferences.get("auto_reset_filter"):
            self.clear_filter(show_message=False)
        
        filtering_props: dict[str, str | list] = {}
        
        print("Creating a new filter: \n")
        
        for prop in vars(self.filter).keys():
            if prop == "in_title":
                print(f"Setting {prop} (separate by comma for multiple):")
            
            else:
                print(f"Setting {prop} (leave empty if not filtered):")

            prop_value = input("> ")

            if "," in prop_value:
                prop_value = prop_value.split(",")
            
            filtering_props[prop] = prop_value

        self.filter.set_filter(filtering_props)

    def file_select(self) -> None:
        print("Running file_select")

    def file_rename(self) -> None:
        print("Creating new renaming schema: \n")
        self.renamer.open_rename_pallete()

        self.renamer.load_filter_obj(self.filter)

        if self.user_preferences.get("auto_reset_filter"):
            self.clear_filter(show_message=False)
    
    def list_dir(self) -> None:
        self.list_all_files()

        if self.user_preferences.get("use_filter_once"):
            self.clear_filter()
    
    def set_dir(self, args: dict) -> None:
        if not os.path.isdir(args["directory"]):
            log_error("Directory not found")
            return
        
        self.curr_dir = args["directory"]
        log_info(f"set current directory as {args['directory']}")

    def set_pressets_dir(self) -> None:
        print("Running set_pressets_dir...")
    
    def list_press(self) -> None:
        print("Running list_press...")
    
    def presset(self) -> None:
        print("Running presset...")

    def clear_filter(self, show_message: bool = True) -> None:
        self.filter.clear_filter()

        if show_message:
            log_info("Filter reset")

    def list_all_files(self) -> None:
        if not self.curr_dir or not os.path.isdir(self.curr_dir):
            log_error("The current directory is not available")
            return

        filenames = os.listdir(self.curr_dir)
        
        filtering_behaviour: str = self.user_preferences.get("filtering_behaviour", "vanish")
        
        print(filtering_behaviour)

        if filtering_behaviour == "vanish":
            filenames = list(filter(self.filter.check_file, filenames))

        min_leading = len(str(len(filenames)))

        if min_leading < 1:
            min_leading = 1

        for i, filename in enumerate(filenames, start=1):

            passes_filter: bool = self.filter.check_file(filename)                    

            if os.path.isdir(os.path.abspath(os.path.join(self.curr_dir,filename))):
                filename = Fore.YELLOW + filename + "/" + Fore.WHITE
            
            if passes_filter:
                print(f"{str(i).zfill(min_leading)}. {filename}")

            else:
                if filtering_behaviour == "italics":
                    print(f"\x1B[3m{str(i).zfill(min_leading)}. {filename}")