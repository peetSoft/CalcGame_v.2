from numeral_system import NumeralSystem
from exercises import SimpleExercises, RandomExercises
from time_prototype import time_limit, TimeoutException
import termcolor

NUMERAL_SYSTEMS = {
    "b": NumeralSystem("01", "bin"),
    "d": NumeralSystem("0123456789", "dec")
}

MODE_DEFINITIONS = {
    "primitiv": [["+"], 1000],
    "easy": [["+", "-"], 1000],
    "normal": [["*", "-", "+", "/"], 8],
    "hard": [["*", "-", "+", "/"], 5]
}

BASE_PIC = ''' 
              |                                  
              |____                     
          / ~~| \\%/                      \\ 
          |                               \\O
          |                                |
          |                                /|
       ~~~~~~                             |  \\ '''

BALL_POSITIONS = (
    (0, 21),
    (0, 17),
    (0, 13),
    (1, 9),
    (2, 3),
)

START_COLOR = "yellow"
SUCCESS_COLOR = "green"
FAILED_COLOR = "red"


def print_basketball(position: tuple, color: str = "white") -> None:
    """
    Inserts the sign of a ball ("o") in the BASEPIC and prints the result
    @param position: Index of vertical bar and offset
    @param color: Color of the ball
    @return None
    """
    vertical_bar_index, ball_offset = position
    pic_as_list[index_list[vertical_bar_index] + ball_offset] \
        = termcolor.colored('o', color)  # Sign of ball inserted
    pic_as_string = "".join(pic_as_list)  # List converted back to the string
    print(pic_as_string)
    print("\n")


def user_input(exercise):
    """
    Taking input from user, checking for correctness.
    If input is not a legitimate expression, or the result is incorrect
    the user is asked again for input.
    @param exercise: [Task for the user: str, the true answer: int] (list)
    @return: None
    """
    question, true_answer = exercise
    while True:

        user_answer = input("Rechnen sie die Aufgabe: " + question + "=")
        # user_answer = true_answer ## Für Testzwecke
        try:
            user_answer_as_int = answer_numeral_system.decode(user_answer)
        except ValueError:
            print("Falsch ! Bitte geben sie eine ganze Zahl ein.")
            continue
        if user_answer_as_int == true_answer:
            break
        else:
            print("Falsch ! Bitte nochmal")



############ main program ##############

# List of places of vertical bars ('|') in BASE_PIC
index_list = []
for i in range(len(BASE_PIC)):
    if BASE_PIC[i] == '|':
        index_list.append(i)


print(termcolor.colored
      ("\nVersenke den Ball im Korb, indem du Matheaufgaben rechnest\n", "magenta", None, ["bold"]))
modes = MODE_DEFINITIONS.keys()
modes_as_string = "/".join(modes)
mode = input("Wählen sie den Spielmodus -- " + modes_as_string + ": ").lower()
while mode not in modes:
    print("Falsche Eingabe")
    mode = input("Wählen sie den Spielmodus -- " + modes_as_string + ": ")
numeral_system_names = NUMERAL_SYSTEMS.keys()
numeral_system_names_as_string = "/".join(numeral_system_names)
question_numeral_system_name = input("Wählen sie ihr Zahlensystem für die Aufgaben --  "
                                     + numeral_system_names_as_string + ": ")
answer_numeral_system_name = input("Wählen sie ihr Zahlensystem für das Ergebnis --  "
                                     + numeral_system_names_as_string + ": ")


question_numeral_system = NUMERAL_SYSTEMS[question_numeral_system_name]
answer_numeral_system = NUMERAL_SYSTEMS[answer_numeral_system_name]
n_exercises = len(BALL_POSITIONS)
exercises = RandomExercises(MODE_DEFINITIONS[mode], question_numeral_system)
max_time = exercises.max_time
while True:
    pic_as_list = list(BASE_PIC)  # String will be converted to a list (because of immutability of string)
    print_basketball((1, 24), START_COLOR)

    counter = 0

    for ball_position in BALL_POSITIONS:
        try:
            with time_limit(max_time):
                user_input(exercises.next_exercise())
        except TimeoutException as e:
            print(termcolor.colored("\n Time out!", "red"))
            color = FAILED_COLOR
        else:
            counter += 1
            print("Exercise solved!")
            color = SUCCESS_COLOR
        print_basketball(ball_position, color)

    print(termcolor.colored(f" Sie haben{counter}Aufgaben "
                            f"von{n_exercises}richtig", "red", "on_grey", {"bold"}))
    game_repeat = input("Nochmal spielen? (j/n) ")
    if game_repeat == "n":
        break

print("Bis zum nächsten mal. Adios !!")
