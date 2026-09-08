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
    """Task2: Enhanced QA Bot, more keywords"""
    print("\n----- QA Bot -----")
    print("Supported keywords: hello, python, jetson, ai, name, github, robot, sensor, iot")
    print("Type 'back' to return to main menu.\n")
    while True:
        user_input = input("Your question: ").strip().lower()
        # 修复：只要内容去掉空格等于back就返回主菜单
        if user_input == "back":
            print("Returning to main menu...")
            break

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


def main_menu():
    """Main menu: select function or exit"""
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Simple Calculator")
        print("2. QA Bot")
        print("3. Exit program")
        choice = input("\nPlease select option (1/2/3): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            qa_bot()
        elif choice == "3":
            print("Program exiting, goodbye!")
            break
        else:
            print("Invalid choice, please enter 1, 2 or 3.")


if __name__ == "__main__":
    main_menu()

