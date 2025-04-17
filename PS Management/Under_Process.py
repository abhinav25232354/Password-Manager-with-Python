import colorama
from colorama import Fore, Back, Style

# Initialize colorama
colorama.init()

# Example usage of colored text
print(Fore.RED + "This is red text")
print(Fore.GREEN + "This is green text")
print(Fore.BLUE + "This is blue text")
print(Back.YELLOW + "This text has a yellow background")
print(Fore.CYAN + Back.MAGENTA + "Cyan text on a magenta background")
print(Style.BRIGHT + "This is bright text")
print(Style.RESET_ALL + "Back to normal text")

# Clean up (optional in most cases)
colorama.deinit()
