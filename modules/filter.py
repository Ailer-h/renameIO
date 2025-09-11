from modules.helper_tools import getIndex

class Filter():
    '''
    Class responsible for handling filtering for the search
    '''
    
    def __init__(self) -> None:
        self.filetype: str = ""
        self.title: str = ""
        self.inTitle: list[str] = []

    def clear_filter(self) -> None:
        self.filetype: str = ""
        self.title: str = ""
        self.inTitle.clear()

    def set_filter(self, filter_props: dict[str, str | list]) -> None:
        self.filetype = str(filter_props.get("filetype", ""))
        self.title = str(filter_props.get("title", ""))
        self.addToInTitle(filter_props.get("inTitle", ""))


    def setFiletype(self, filetype: str) -> None:
        if filetype and filetype.startswith("."):
            self.filetype = filetype

    def setTitle(self, title: str) -> None:
        if title:
            self.title = title

    def addToInTitle(self, add_to: str | list[str]) -> None:
        if add_to:

            if isinstance(add_to, list) and all(add_to):
                self.inTitle += add_to
                return
            
            elif isinstance(add_to, str):
                self.inTitle.append(add_to)

    def removeFromInTitle(self, remove_from: str | list[str]) -> None:
        if remove_from:

            if isinstance(remove_from, str):

                remove_ix: int | None = getIndex(remove_from, self.inTitle)

                if remove_ix:
                    self.inTitle.pop(remove_ix)

            else:

                for item in remove_from:
                    remove_ix: int | None = getIndex(item, self.inTitle)

                    if remove_ix:
                        self.inTitle.pop(remove_ix)
