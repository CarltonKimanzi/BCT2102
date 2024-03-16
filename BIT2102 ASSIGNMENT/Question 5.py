import random

def ask_question(num1, num2, operation):

    if operation == "+":
        symbol = "+"
        result = num1 + num2
    else:
        if num1 < num2:
            num1, num2 = num2, num1
        symbol = "-"
        result = num1 - num2

    user_answer = int(input(f"What is {num1} {symbol} {num2}? "))

    return user_answer == result

def main():
    num_questions = 5
    correct_answers = 0

    for _ in range(num_questions):

        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        operation = random.choice(["+", "-"])

        if ask_question(num1, num2, operation):
            correct_answers += 1
            print("Correct!")
        else:
            print("Incorrect.")

    print(f"You answered {correct_answers} out of {num_questions} questions correctly.")

if __name__ == "__main__":
    main()
