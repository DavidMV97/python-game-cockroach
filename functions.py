from colorama import Fore, Back, Style, init
import random

num_players = 0

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
        while True:
            try:
                print(f"Jugador {player + 1 } : ")
                launch = int(input("Pulsa 1 para lanzar los dados : "))
                if launch != 1 :
                    print("Opcion inválida, intenta nuevamente")
                else:
                    throw_dice()
                    break
            except ValueError:
                print("Ingresa un número válido")
                


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

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    dado4 = random.randint(1, 6)
    dado5 = random.randint(1, 6)
    dado6 = random.randint(1, 6)

    # Obtiene las representaciones de los dados
    representacion_dado1 = dice_faces[dado1 - 1]
    representacion_dado2 = dice_faces[dado2 - 1]
    representacion_dado3 = dice_faces[dado3 - 1]
    representacion_dado4 = dice_faces[dado4 - 1]
    representacion_dado5 = dice_faces[dado5 - 1]
    representacion_dado6 = dice_faces[dado6 - 1]

    # Imprime los resultados uno al frente del otro
    for line1, line2, line3, line4, linea5, linea6 in zip(representacion_dado1, representacion_dado2, representacion_dado3, representacion_dado4, representacion_dado5, representacion_dado6 ):
        print(line1 + "   " + line2 + "   " + line3 + "   " + line4 + "   " + linea5 + "   " + linea6)
        