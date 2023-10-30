from colorama import Fore, Back, Style, init
import random

num_players = 0
dados = [1, 2, 3, 4, 5, 6]


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
        error = True
        while error:
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
    
    
    global dados
    global seguir_lanzando
    resultado = [random.choice(dados) for _ in range(len(dados))]
    dados = [dado for dado in resultado]
    
    # print(f"resultado:: {resultado}")

    for i in range(5):
        for dado in resultado:
            print(Fore.LIGHTGREEN_EX + dice_faces[dado - 1][i], end="   ")
        print()

    # print([1,2,3,2,3,4,5,3,3,3,3,6].count(3))
    

    if 2 in resultado:
        seguir_lanzando = True
        dados.pop(-1)
    else:
        seguir_lanzando = False
        dados = [1, 2, 3, 4, 5, 6]
        
    
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
                    dados.pop(-1)
                else:
                    seguir_lanzando = False
                    dados = [1, 2, 3, 4, 5, 6]
                for i in range(5):
                    for dado in resultado:
                        print(Fore.LIGHTGREEN_EX + dice_faces[dado - 1][i], end="   ")
                    print()
                break
        except ValueError:
                print(f"{Back.RED} {Fore.WHITE} Ingresa un número válido")
    
        