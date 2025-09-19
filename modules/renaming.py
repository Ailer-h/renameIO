from modules.filter import Filter

class Renamer():

    def __init__(self, filter_obj: Filter | None = None) -> None:
        self.filter = filter_obj

    def open_rename_pallete(self) -> None:
        pass

    def rename_files(self) -> None:
        pass

    def load_filter_obj(self, filter_obj: Filter) -> None:
        self.filter = filter_obj

    def clear_filter_obj(self) -> None:
        self.filter = None