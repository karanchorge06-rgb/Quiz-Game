"""
main.py

This is the entry point of the Quiz Application. It displays a welcome
message and a menu, and lets the user start the quiz, view the previous
(high) score, or exit the program.
"""

from quiz import Quiz


def display_welcome_message() -> None:
    """Print a welcome banner for the quiz application."""
    print("=" * 40)
    print("   Welcome to the Python Quiz App!")
    print("=" * 40)


def display_menu() -> None:
    """Print the main menu options."""
    print("\nMenu:")
    print("1. Start Quiz")
    print("2. View Previous Score")
    print("3. Exit")


def get_menu_choice() -> str:
    """
    Prompt the user for a menu choice and validate it.

    Returns:
        str: A validated menu choice ("1", "2", or "3").
    """
    valid_choices = ("1", "2", "3")

    while True:
        choice = input("Enter your choice (1-3): ").strip()

        if choice in valid_choices:
            return choice

        # Handle invalid menu input gracefully.
        print("Invalid choice. Please enter 1, 2, or 3.")


def ask_play_again() -> bool:
    """
    Ask the user if they want to play the quiz again.

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    while True:
        answer = input("Do you want to play again? (y/n): ").strip().lower()

        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False

        # Handle invalid yes/no input gracefully.
        print("Invalid input. Please enter 'y' or 'n'.")


def main() -> None:
    """Run the main program loop for the quiz application."""
    display_welcome_message()

    # Create a single Quiz instance to reuse across menu selections.
    quiz = Quiz()

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            # Start the quiz and display the score once finished.
            final_score = quiz.start()
            print(f"\nYour final score for this attempt: {final_score}")

            # Ask if the user wants to play again immediately.
            if not ask_play_again():
                print("\nThanks for playing! Goodbye.")
                break

        elif choice == "2":
            # Show the highest score recorded so far.
            high_score = quiz.get_high_score()
            print(f"\nHighest Score So Far: {high_score}")

        elif choice == "3":
            # Exit the program.
            print("\nThanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
