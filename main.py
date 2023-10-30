from colorama import Fore, Back, Style, init
from functions import *

def main():
    init(autoreset=True)
    print("\n")
    print(Back.CYAN + Fore.WHITE + "********** Bienvenido **********\n")
    print(Fore.YELLOW + "Por favor ingresa el número de jugadores  (2 - 7) : ")
    validate_players()

    # restablecer los colores y el estilo al final para evitar efectos no deseados en la consola
    print(Style.RESET_ALL)


main()
