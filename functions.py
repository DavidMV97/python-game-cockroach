from colorama import Fore, Back, Style, init
import random

num_players = 0
dados = [1, 2, 3, 4, 5, 6]
seguir_lanzando = ''

def validate_players():
    error = True
    while error:  
        try:
            global num_players
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
                game_start()
                error = False

        except ValueError:
            print(Back.RED + Fore.WHITE + "Por Favor ingresa un número valido")


def game_start():
    for player in range(num_players):
        
        print(f'{Back.MAGENTA} Seguir lanzando ...' , seguir_lanzando)
        
        while True:
            try:
                print(f"{Fore.CYAN} Jugador {player + 1 } : ")
                launch = int(input(f"{Fore.YELLOW} Pulsa 1 para lanzar los dados : "))
                if launch != 1 :
                    print(f"{Back.RED} {Fore.WHITE} Opcion inválida, intenta nuevamente")
                else:
                    throw_dice()
                    if not seguir_lanzando:
                        break
    
            except ValueError:
                print(f"{Back.RED} {Fore.WHITE} Ingresa un número válido")
                
                          
def throw_dice():
       
    global dados
    global seguir_lanzando
    resultado = [random.choice(dados) for _ in range(len(dados))]
    dados = [dado for dado in resultado]
    
    # if not seguir_lanzando:
    #     print_dados(resultado)

    # Cantidad de unos sacados : 
    print(f'{Back.GREEN} {Fore.WHITE} Cantidad de unos sacados :: {resultado.count(1)}')
    
    print_dados(resultado)

    if 1 in resultado:
        seguir_lanzando = True

    else:
        seguir_lanzando = False
        
    
    while seguir_lanzando:
        print(f'{Back.CYAN} {Fore.WHITE}  Muy bien, puedes volver a lanzar.')
        
        try:
            print(f'{Fore.YELLOW} Pulsa 1 para lanzar otra vez : ')
            launch = int(input())
            if launch != 1 :
                print(f"{Back.RED} {Fore.WHITE} Opcion inválida, intenta nuevamente")
            else:
                resultado = [random.choice(dados) for _ in range(len(dados))]
                dados = [dado for dado in resultado]
                if 1 in resultado:
                    seguir_lanzando = True
                else:
                    seguir_lanzando = False
                    dados = [1, 2, 3, 4, 5, 6]
                print_dados(resultado)
                break
        except ValueError:
                print(f"{Back.RED} {Fore.WHITE} Ingresa un número válido")
    
        
def print_dados(resultado):
    dice_faces = [
        [
            "+-------+",
            "|       |",
            "|   *   |",
            "|       |",
            "+-------+"
        ],
        [
            "+-------+",
            "| *     |",
            "|       |",
            "|     * |",
            "+-------+"
        ],
        [
            "+-------+",
            "| *     |",
            "|   *   |",
            "|     * |",
            "+-------+"
        ],
        [
            "+-------+",
            "| *   * |",
            "|       |",
            "| *   * |",
            "+-------+"
        ],
        [
            "+-------+",
            "| *   * |",
            "|   *   |",
            "| *   * |",
            "+-------+"
        ],
        [
            "+-------+",
            "| *   * |",
            "| *   * |",
            "| *   * |",
            "+-------+"
        ]
    ]
    
    for i in range(5):
        for dado in resultado:
            print(Fore.LIGHTGREEN_EX + dice_faces[dado - 1][i], end="   ")
        print()
    