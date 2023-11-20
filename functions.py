from colorama import Fore, Back, init
import random

def validate_players():
    while True:
        try:
            num_players = int(input("Ingrese el número de jugadores (2-7): "))
            if 2 <= num_players <= 7:
                game_start(num_players)
                break
            else:
                print(f"{Back.RED} {Fore.WHITE}Número de jugadores no válido. Debe estar entre 2 y 7.")
        except ValueError:
            print(f"{Back.RED} {Fore.WHITE}Por favor, ingrese un número válido.")

def game_start(num_players):
    for player in range(num_players):
        seguir_lanzando = True

        while seguir_lanzando:
            try:
                print(f"{Fore.CYAN} Jugador {player + 1} : ")
                launch = int(input(f"{Fore.YELLOW} Pulsa 1 para lanzar los dados: "))
                if launch != 1:
                    print(f"{Back.RED} {Fore.WHITE} Opción inválida, intenta nuevamente")
                else:
                    throw_dice()
                    seguir_lanzando = False
                    # seguir_lanzando = input("¿Quieres lanzar de nuevo? (s/n): ").lower() == 's'
            except ValueError:
                print(f"{Back.RED} {Fore.WHITE} Ingresa un número válido")


def throw_dice():
    dados = [1, 2, 3, 4, 5, 6]
    resultado = [random.choice(dados) for _ in range(len(dados))]

    print_dados(resultado)

    while 1 in resultado:
        input(f'{Fore.MAGENTA}Presiona Enter para lanzar nuevamente :')
        dados = [result for result in resultado if result != 1]  # Eliminar un dado por cada 1 que saque
        resultado = [random.choice(dados) for _ in range(len(dados))]
        print_dados(resultado)

    return resultado



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

