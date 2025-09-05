from colorama import Fore
import os

class Renamer():

    def __init__(self) -> None:
        self.commands = {
            "filter": self.dir_filter,
            "select": self.file_select,
            "rename": self.file_rename,
            "list_dir": self.list_dir,
            "set_dir": self.set_dir
        }

        self.curr_dir: str = os.getcwd()

    def run_command(self, command: str, args: list | None) -> None:
        if command not in self.commands:
            print(f"{Fore.RED}[Error]{Fore.WHITE} Command module not found")
            return
        
        self.commands[command](args)

    def dir_filter(self, args: list | None) -> None:
        """
        args: list = [file_type, on_filename]
        """
        
        print("Running dir_filter")

    def file_select(self) -> None:
        print("Running file_select")

    def file_rename(self) -> None:
        print("Running file_rename")
    
    def list_dir(self, args: list | None) -> None:
        """
        args: list = [order_by, ascending?]
        """

        order_by = None
        reversed_result = False
        
        if args:
            if args[0]:
                order_by = args[0]

            if len(args) > 1 and args[1]:
                reversed_result = bool(int(args[1]))

        self.list_all_files(order_by, reversed_result)
    
    def set_dir(self, args: list) -> None:
        """
        args: list = [new_directory]
        """

        if not os.path.isdir(args[0]):
            print(f"{Fore.RED}[Error]{Fore.WHITE} Directory not found")
            return
        
        self.curr_dir = args[0]
        print(f"[RenameIO] set current directory as {args[0]}")


    def list_all_files(self, order_by: str | None, reverse: bool = False) -> None:
        if not self.curr_dir or not os.path.isdir(self.curr_dir):
            print(f"{Fore.RED}[Error]{Fore.WHITE} The current directory is not available")
            return

        filenames = os.listdir(self.curr_dir)
        min_leading = len(str(len(filenames)))

        if min_leading < 1:
            min_leading = 1

        if str(order_by).lower() == "title":
            filenames = sorted(filenames)

        if reverse:
            filenames = reversed(filenames)

        for i, filename in enumerate(filenames, start=1):

            if os.path.isdir(os.path.abspath(os.path.join(self.curr_dir,filename))):
                filename = Fore.YELLOW + filename + "/" + Fore.WHITE
            
            print(f"{str(i).zfill(min_leading)}. {filename}")
