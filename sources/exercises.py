import random

all_exercises = [
    "54-22",
    "81-29",
    "23+59",
    "77-44",
    "88+31"
]


class SimpleExercises:
    """
    Exercises generates arithmetic questions.
    There are 5 questions, they will be repeatedly presented
    """

    def __init__(self):
        """
        Initiates index of exercise
        """
        self.current_exercise_index = 0

    def next_exercise(self):
        """
        Returns one exercise
        Increases index of exercise

        :return: exercise as question and answer
        """
        current_exercise = all_exercises[self.current_exercise_index]
        self.current_exercise_index += 1
        self.current_exercise_index %= len(all_exercises)
        return current_exercise, eval(current_exercise)  # returns list


mode_definitions = {
    "primitiv": [["+"], 1000],
    "easy": [["+", "-"], 10],
    "normal": [["*", "-", "+", "/"], 8],
    "hard": [["*", "-", "+", "/"], 5]
}


class RandomExercises:
    def __init__(self, mode):
        self.operators, self.max_time = mode_definitions[mode]

    def next_exercise(self):
        """
        generates random exercise (random operator , random operands)
        :return: exercise as question (str) and answer (int)
        """
        i = random.randrange(len(self.operators))
        operator = self.operators[i]
        operand1, operand2 = self.generate_operands(operator)
        exercise_as_str = str(operand1) + operator + str(operand2)
        result = eval(exercise_as_str)
        return exercise_as_str, result  # Verpacken

    @staticmethod
    def generate_operands(operator):
        """

        """
        if operator == "+":
            operand1 = random.randrange(10, 100)
            operand2 = random.randrange(10, 100)
        elif operator == "-":
            operand1 = random.randrange(10, 100)
            operand2 = random.randrange(10, 100)
            if operand2 > operand1:
                temp = operand2
                operand2 = operand1
                operand1 = temp
        elif operator == "*":
            operand1 = random.randrange(5, 15)
            operand2 = random.randrange(5, 15)
        else:
            operand2 = random.randrange(5, 15)
            result = random.randrange(5, 15)
            operand1 = result * operand2
        return operand1, operand2
