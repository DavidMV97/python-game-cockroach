from colorama import Fore, Back, Style, init

init(autoreset=True)

def validate_players():
    error = True
    while error:  
        try:
            num_players = input()
            num_players = int(num_players)
            if num_players < 2 or num_players > 7:
                if num_players == 1:
                    print(Back.RED + Fore.WHITE + 'No es posible jugar un 1 jugador. Por favor intenta de nuevo.')
                elif num_players == -1:
                    print(Back.RED + Fore.WHITE + 'No es posible jugar un -1 jugador. Por favor intenta de nuevo.')

                else:
                    print(Back.RED + Fore.WHITE + f"No es posible jugar con {num_players} jugadores . Por Favor intenta de nuevo.")

            else:
                print('Logica del juego aqui')
                error = False

        except ValueError:
            print(Back.RED + Fore.WHITE + "Por Favor ingresa un número valido")
