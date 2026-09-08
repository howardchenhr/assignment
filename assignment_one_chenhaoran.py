import turtle
from turtle import Terminator
import random


def simple_calculator():
    """Task1: Simple Calculator"""
    print("\n----- Simple Calculator -----")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please input valid numbers!")
        return

    print("Operators available: + , - , * , /")
    operator = input("Select operator: ")

    valid = True
    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            valid = False
        else:
            result = num1 / num2
    else:
        print("Error: Invalid operator")
        valid = False

    if valid:
        print(f"Calculation: {num1} {operator} {num2} = {result}")


def qa_bot():
    """Task2: QA Bot"""
    print("\n----- QA Bot -----")
    print("Supported keywords: hello, python, jetson, ai, name, github, robot, sensor, iot\n")
    user_input = input("Your question: ").strip().lower()

    if "hello" in user_input:
        print("Bot: Hello! Welcome to QA Bot.")
    elif "python" in user_input:
        print("Bot: Python is a high‑level interpreted programming language, widely used in AI and automation.")
    elif "jetson" in user_input:
        print("Bot: Jetson is NVIDIA embedded hardware for edge AI applications.")
    elif "ai" in user_input:
        print("Bot: AI is Artificial Intelligence, enabling machines to mimic human‑like reasoning.")
    elif "name" in user_input:
        print("Bot: My name is Interactive QA Bot.")
    elif "github" in user_input:
        print("Bot: GitHub is a platform for code hosting and version control using Git.")
    elif "robot" in user_input:
        print("Bot: Robots are programmable machines capable of completing physical tasks.")
    elif "sensor" in user_input:
        print("Bot: Sensors detect physical signals and convert them into readable digital data.")
    elif "iot" in user_input:
        print("Bot: IoT means Internet of Things, connecting physical devices to the internet.")
    else:
        print("Bot: Sorry, I do not know the answer to that question.")

    print("\nReturning to main menu...")


def turtle_drawing():
    """Task3 Bonus: Turtle Drawing"""
    print("\n----- Turtle Drawing -----")
    print("Options: 1‑Square | 2‑Triangle | 3‑Star")
    shape_choice = input("Please select shape to draw (1/2/3): ").strip()

    try:
        screen = turtle.Screen()
        screen.title("Turtle Drawing Bonus Task")
        t = turtle.Turtle()
        t.speed(0)
        colors = ["red", "green", "blue", "orange", "purple", "cyan", "yellow", "pink"]

        if shape_choice == "1":
            print("Drawing colourful square, random overall size, all sides equal")
            side_length = random.randint(100, 220)
            for i in range(4):
                t.color(random.choice(colors))
                t.forward(side_length)
                t.right(90)

        elif shape_choice == "2":
            print("Drawing colourful triangle, random overall size, all sides equal")
            side_length = random.randint(100, 220)
            for i in range(3):
                t.color(random.choice(colors))
                t.forward(side_length)
                t.right(120)

        elif shape_choice == "3":
            print("Drawing colourful star, random overall size, all sides equal")
            side_length = random.randint(120, 260)
            for i in range(5):
                t.color(random.choice(colors))
                t.forward(side_length)
                t.right(144)

        else:
            print("Invalid shape choice.")
            turtle.bye()
            return

        print("Drawing finished. Click anywhere on drawing window to close.")
        screen.exitonclick()

    except Terminator:
        print("\n[Info] Turtle window has been closed. Back to main menu.")
    except Exception as e:
        print(f"\n[Warning] Cannot open turtle graphics: {e}")
        print("Note: Turtle requires a local desktop environment.")
    finally:
        try:
            turtle.bye()
        except:
            pass


def main_menu():
    """Main menu: select function or exit"""
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Simple Calculator")
        print("2. QA Bot")
        print("3. Turtle Drawing (Bonus)")
        print("4. Exit program")
        choice = input("\nPlease select option (1/2/3/4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            qa_bot()
        elif choice == "3":
            turtle_drawing()
        elif choice == "4":
            print("Program exiting, goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main_menu()

