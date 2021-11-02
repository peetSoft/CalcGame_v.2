from numeral_system import NumeralSystem
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


class RandomExercises:
    def __init__(self, mode_definition, numeral_system):
        self.operators, self.max_time = mode_definition
        self.numeral_system = numeral_system

    def next_exercise(self):
        """
        generates random exercise (random operator , random operands)
        :return: exercise as question (str) and answer (int)
        """
        i = random.randrange(len(self.operators))
        operator = self.operators[i]
        operand1, operand2 = self.generate_operands(operator)
        exercise_dec_as_str = str(operand1) + operator
        exercise_ns_as_str = self.numeral_system.code(operand1) + operator
        if operand2 is not None:
            exercise_dec_as_str += operand2
            exercise_ns_as_str += operand2
        result = eval(exercise_dec_as_str)
        return exercise_ns_as_str, result  # Verpacken

    @staticmethod
    def generate_operands(operator):
        """
        generates two none-negative integers. If operator = <empty> Second operand = None.
        @param operator: +|-|*|/|<empty>
        @return: list of two operands
        """

        if operator == "+":
            operand1 = random.randrange(0, 10)
            operand2 = random.randrange(0, 10)
        elif operator == "-":
            operand1 = random.randrange(0, 10)
            operand2 = random.randrange(0, 10)
            if operand2 > operand1:
                temp = operand2
                operand2 = operand1
                operand1 = temp
        elif operator == "*":
            operand1 = random.randrange(5, 15)
            operand2 = random.randrange(5, 15)
        elif operator == "/":
            operand2 = random.randrange(5, 15)
            result = random.randrange(5, 15)
            operand1 = result * operand2
        else:
            operand1 = random.randrange(4,16)
            operand2 = None
        return operand1, operand2
