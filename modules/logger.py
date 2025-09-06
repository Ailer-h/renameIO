from colorama import Fore

def log_error(message: str, log_id: str = "Error"):
    print(f"{Fore.RED}[{log_id}]{Fore.WHITE} {message}")

def log_info(message: str, log_id: str = "RenameIO"):
    print(f"[{log_id}] {message}")