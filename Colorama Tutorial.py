import colorama
from colorama import Fore, Back, Style

colorama.init()

# You have 3 Options to choose from:
# 1) Fore = Foreground (Characters)
# 2) Back = Background (Behind the Characters)
# 3) Style = Look of the Color (Bright, Dim, Normal)

#  Everytime you assign a color it continues to remain for the further strings untill it resets. To reset automatically choose 
#  colorama.init(autoreset = True)
#  or you can manually reset it using Fore.RESET.
print('Hello Jay')
print(Fore.RED + Style.BRIGHT + "I Love You")
print(Fore.BLUE + "I Love You")
print(Fore.GREEN + Back.BLUE + "I Love You" + Back.RESET)
print(Fore.LIGHTMAGENTA_EX + "I Love You")
print(Fore.LIGHTYELLOW_EX + "I Love You")
print("Avani")
print('Jay')
print(Style.BRIGHT + "JAY")
print(Fore.RESET, Back.RESET, Style.RESET_ALL)