from modules.filter import Filter
from modules.helper_tools import extract_from_brackets, get_now
from datetime import datetime
from re import sub

class Renamer():

    def __init__(self, filter_obj: Filter | None = None) -> None:
        self.filter: Filter | None = filter_obj
        self.new_name: str = ""
        self.counter_start = 0

    def open_rename_pallete(self) -> None:
        print("Insert the command: ")
        self.new_name = input("> ")

    def get_new_filename(self, text: str, txt_index: int) -> str:
        now: datetime = datetime.now()

        placeholders: list = extract_from_brackets(text)

        for placeholder in placeholders:
            replace_with: str = ""
            
            if "date-" in placeholder:
                replace_with = get_now(placeholder.replace("date-", ""))

            elif "counter-" in placeholder:
                pass

            text = text.replace(placeholder, replace_with)
            

        return ""

    def rename_files(self) -> None:
        pass

    def load_filter_obj(self, filter_obj: Filter) -> None:
        self.filter = filter_obj

    def clear_filter_obj(self) -> None:
        self.filter = None