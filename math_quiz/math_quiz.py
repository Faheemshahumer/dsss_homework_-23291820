import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between the specified range.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generates a random arithmetic operator: +, -, or *.
    """
    return random.choice(['+', '-', '*'])

def perform_operation(number1, number2, operator):
    """
    Performs the arithmetic operation based on the provided numbers and operator.
    Returns a tuple containing the problem string and the correct answer.
    """
    problem_expression = f"{number1} {operator} {number2}"

    if operator == '+':
        correct_answer = number1 + number2
    elif operator == '-':
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2

    return problem_expression, correct_answer

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = perform_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
