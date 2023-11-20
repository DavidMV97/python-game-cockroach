from colorama import Fore, Back
import random

def validate_players():
    while True:
        try:
            num_players = int(input("Ingrese el número de jugadores (2-7): "))
            if 2 <= num_players <= 15:
                game_start(num_players)
                break
            else:
                print(f"{Back.RED} {Fore.WHITE}Número de jugadores inválido. Debe estar entre 2 y 7.")
        except ValueError:
            print(f"{Back.RED} {Fore.WHITE}Por favor, ingrese un número válido.")

def game_start(num_players):
    scores = [0] * num_players  # Lista para almacenar los puntajes de cada jugador

    while True:
        for player in range(num_players):
            seguir_lanzando = True

            while seguir_lanzando:
                try:
                    print(f"{Fore.CYAN} Jugador {player + 1} : ")
                    launch = int(input(f"{Fore.YELLOW} Pulsa 1 para lanzar los dados: "))
                    if launch != 1:
                        print(f"{Back.RED} {Fore.WHITE} Opción inválida, intenta nuevamente")
                    else:
                        resultado = throw_dice()
                        scores[player] += resultado  # Suma la cantidad de "1" al puntaje del jugador
                        print(f"Puntaje actual de Jugador {player + 1}: {scores[player]}")
                        seguir_lanzando = False
                except ValueError:
                    print(f"{Back.RED} {Fore.WHITE} Ingresa un número válido")

        if input("¿Quieres continuar? (y/n): ").lower() != 'y':
            break

    print("Puntajes finales:")
    for i, score in enumerate(scores, start=1):
        print(f"Jugador {i}: {score}")

def throw_dice():
    count_amount_one = 0
    dados = [1, 2, 3, 4, 5, 6]
    resultado = [random.choice(dados) for _ in range(len(dados))]
    print_dados(resultado)
    
    count_amount_one += resultado.count(1)
    

    while 1 in resultado:
        input(f'{Fore.MAGENTA}Presiona Enter para lanzar nuevamente :')
        dados = [result for result in resultado if result != 1]
        resultado = [random.choice(dados) for _ in range(len(dados))]
        count_amount_one += resultado.count(1)
        print_dados(resultado)
        
    
    return count_amount_one

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


