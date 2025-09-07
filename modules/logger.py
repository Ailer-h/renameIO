from colorama import Fore

def log(log_id: str, msg: str, id_colour: str | None = None):
    if id_colour == None:
        id_colour = Fore.WHITE
    
    print(f"{id_colour}[{log_id}]{Fore.WHITE} {msg}")

def log_error(message: str, log_id: str = "Error"):
    log(log_id, message, id_colour=Fore.RED)

def log_info(message: str, log_id: str = "RenameIO"):
    log(log_id, message)