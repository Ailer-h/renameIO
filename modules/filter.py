from modules.helper_tools import getIndex

class Filter():
    '''
    Class responsible for handling filtering for the search
    '''
    
    def __init__(self) -> None:
        self.filetype: str = ""
        self.title: str = ""
        self.in_title: list[str] = []

    def check_file(self, filename: str) -> bool:
        if self.filetype:
            if not filename.endswith(self.filetype):
                return False
            
        if self.title:
            if filename.split(".")[0] != self.title:
                return False
            
        if self.in_title:
            for string in self.in_title:
                if string not in filename:
                    return False
                
        return True

    def clear_filter(self) -> None:
        self.filetype: str = ""
        self.title: str = ""
        self.in_title.clear()

    def set_filter(self, filter_props: dict[str, str | list]) -> None:
        self.filetype = str(filter_props.get("filetype", ""))
        self.title = str(filter_props.get("title", ""))
        self.add_to_in_title(filter_props.get("in_title", ""))


    def set_filetype(self, filetype: str) -> None:
        if filetype and filetype.startswith("."):
            self.filetype = filetype

    def set_title(self, title: str) -> None:
        if title:
            self.title = title

    def add_to_in_title(self, add_to: str | list[str]) -> None:
        if add_to:

            if isinstance(add_to, list) and all(add_to):
                self.in_title += add_to
                return
            
            elif isinstance(add_to, str):
                self.in_title.append(add_to)

    def remove_from_in_title(self, remove_from: str | list[str]) -> None:
        if remove_from:

            if isinstance(remove_from, str):

                remove_ix: int | None = getIndex(remove_from, self.in_title)

                if remove_ix:
                    self.in_title.pop(remove_ix)

            else:

                for item in remove_from:
                    remove_ix: int | None = getIndex(item, self.in_title)

                    if remove_ix:
                        self.in_title.pop(remove_ix)
