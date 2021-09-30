from exercises import SimpleExercises, RandomExercises, mode_definitions
from time_prototype import time_limit, TimeoutException


def print_basketball(position):
    """
    Diese Fun
    @param position:
    @return: None

    """
    """
    Inserts the sign of a ball ("o") in the BASEPIC and prints the result
    @param position: Index of vertical bar and offset
    @return None


    """

    vertical_bar_index, ball_offset = position
    pic_as_list[index_list[vertical_bar_index] + ball_offset] = 'o'  # Sign of ball inserted
    pic_as_string = "".join(pic_as_list)  # List converted back to the string
    print(pic_as_string)
    print("\n")


def user_input(exercise):
    question, true_answer = exercise
    while True:

        user_answer = input("Rechnen sie die Aufgabe: " + question + "=")
        # user_answer = true_answer ## Für Testzwecke
        try:
            user_answer_as_int = int(user_answer)
        except ValueError:
            print("Falsch ! Bitte geben sie eine ganze Zahl ein.")
            continue
        if user_answer_as_int == true_answer:
            break
        else:
            print("Falsch ! Bitte nochmal")


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

############ main program ##############

# List of places of vertical bars ('|') in BASE_PIC
index_list = []
for i in range(len(BASE_PIC)):
    if BASE_PIC[i] == '|':
        index_list.append(i)

print("Versenke den Ball im Korb, indem du Matheaufgaben rechnest:")
modes = mode_definitions.keys()
modes_as_string = "/".join(modes)
mode = input("Wählen sie den Spielmodus -- " + modes_as_string + ": ").lower()
while mode not in modes:
    print("Falsche Eingabe")
    mode = input("Wählen sie den Spielmodus -- " + modes_as_string + ": ")

exercises = RandomExercises(mode)
while True:
    pic_as_list = list(BASE_PIC)  # String will be converted to a list (because of immutability of string)
    print_basketball((1, 24))

    counter = 0
    for ball_position in BALL_POSITIONS:
        try:
            with time_limit(5):
                user_input(exercises.next_exercise())
        except TimeoutException as e:
            print("Time out!")
        else:
            counter += 1
            print("Exercise solved!")
        print_basketball(ball_position)

    print(f" Sie haben  {counter}  Aufgaben von  {len(BALL_POSITIONS)}  richtig")
    game_repeat = input("Nochmal spielen? (j/n) ")
    if game_repeat == "n":
        break

print("Bis zum nächsten mal. Adios !!")
