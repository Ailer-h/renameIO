from modules.filter import Filter
from modules.helper_tools import extract_from_brackets, get_now
from modules.logger import log_info, log_error
import os

class Renamer():

    def __init__(self, filter_obj: Filter | None = None) -> None:
        self.filter: Filter | None = filter_obj
        self.new_name: str = ""
        self.counter: int = 0
        self.curr_dir: str = ""

    def open_rename_pallete(self) -> None:
        print("Insert the command: ")
        self.new_name = input("> ")

        self.rename_files()

        log_info("Renamed files")

    def get_new_filename(self, text: str, txt_index: int) -> str:

        placeholders: list = extract_from_brackets(self.new_name)

        for placeholder in placeholders:

            replace_with: str = ""
            
            if "date-" in placeholder:
                replace_with = get_now(self.new_name.replace("date-", ""))

            elif "counter-" in placeholder:
                replace_with = str(self.counter + txt_index)

            text = self.new_name.replace(placeholder, replace_with)

        return text

    def rename_files(self) -> None:

        if not self.curr_dir or not os.path.isdir(self.curr_dir):
            log_error("The current directory is not available")
            return
        
        if not self.filter:
            log_error("The filter is not available. Set the filter object first.")
            return
        
        filenames = os.listdir(self.curr_dir)
        filenames = list(filter(self.filter.check_file, filenames))

        for i, filename in enumerate(filenames):
            new_filename: str = self.get_new_filename(filename, i)
            print(new_filename)

    def load_curr_dir(self, directory: str) -> None:
        if not os.path.isdir(directory):
            log_error("Directory not found")
            return
        
        self.curr_dir = directory

    def reset_curr_dir(self) -> None:
        self.curr_dir = os.getcwd()

    def load_filter_obj(self, filter_obj: Filter) -> None:
        self.filter = filter_obj

    def clear_filter_obj(self) -> None:
        self.filter = None