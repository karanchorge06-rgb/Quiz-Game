import random
import os
from typing import List, Dict


class Quiz:
       def __init__(self) -> None:
       
        # List of questions. Each question is a dictionary with:
        # "question": the question text
        # "options": a dictionary mapping A/B/C/D to option text
        # "answer": the correct option letter (A, B, C, or D)
        self.questions: List[Dict] = [
            {
                "question": "What is the capital of France?",
                "options": {
                    "A": "Berlin",
                    "B": "Madrid",
                    "C": "Paris",
                    "D": "Rome",
                },
                "answer": "C",
            },
            {
                "question": "Which language is primarily used for web styling?",
                "options": {
                    "A": "HTML",
                    "B": "CSS",
                    "C": "Python",
                    "D": "Java",
                },
                "answer": "B",
            },
            {
                "question": "What does 'CPU' stand for?",
                "options": {
                    "A": "Central Process Unit",
                    "B": "Central Processing Unit",
                    "C": "Computer Personal Unit",
                    "D": "Central Processor Utility",
                },
                "answer": "B",
            },
            {
                "question": "Which of these is a Python data type?",
                "options": {
                    "A": "list",
                    "B": "array",
                    "C": "vector",
                    "D": "stack",
                },
                "answer": "A",
            },
            {
                "question": "Who developed the theory of relativity?",
                "options": {
                    "A": "Isaac Newton",
                    "B": "Albert Einstein",
                    "C": "Nikola Tesla",
                    "D": "Galileo Galilei",
                },
                "answer": "B",
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": {
                    "A": "Earth",
                    "B": "Saturn",
                    "C": "Jupiter",
                    "D": "Neptune",
                },
                "answer": "C",
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": {
                    "A": "func",
                    "B": "def",
                    "C": "function",
                    "D": "lambda",
                },
                "answer": "B",
            },
            {
                "question": "What is the boiling point of water at sea level (Celsius)?",
                "options": {
                    "A": "90",
                    "B": "100",
                    "C": "110",
                    "D": "120",
                },
                "answer": "B",
            },
            {
                "question": "Which company developed the Python programming language?",
                "options": {
                    "A": "It was created by Guido van Rossum",
                    "B": "Microsoft",
                    "C": "Google",
                    "D": "Apple",
                },
                "answer": "A",
            },
            {
                "question": "Which data structure uses FIFO (First In First Out)?",
                "options": {
                    "A": "Stack",
                    "B": "Queue",
                    "C": "Tree",
                    "D": "Graph",
                },
                "answer": "B",
            },
        ]

        # Score for the current quiz attempt.
        self.score: int = 0

        # File used to store the highest score achieved so far.
        self.score_file: str = "score.txt"

    def start(self) -> int:
        """
        Start the quiz: shuffle questions, ask each one, and track the score.

        Returns:
            int: The final score achieved in this quiz attempt.
        """
        # Reset score at the start of every new attempt.
        self.score = 0

        # Create a shuffled copy of the questions so the original list
        # order is not modified between quiz attempts.
        shuffled_questions = self.questions.copy()
        random.shuffle(shuffled_questions)

        # Loop through each question and ask the user.
        for index, question_data in enumerate(shuffled_questions, start=1):
            self._ask_question(index, question_data)

        # Show the final score for this attempt.
        total_questions = len(self.questions)
        print("\n" + "=" * 40)
        print(f"Quiz Complete! Your Score: {self.score}/{total_questions}")
        print("=" * 40)

        # Update the high score file if this attempt beats the record.
        self._update_high_score()

        return self.score

    def _ask_question(self, index: int, question_data: Dict) -> None:
        """
        Display a single question, validate input, and update the score.

        Args:
            index (int): The question number to display (1-based).
            question_data (Dict): Dictionary containing the question,
                options, and correct answer.
        """
        print(f"\nQuestion {index}: {question_data['question']}")

        # Display each option on its own line, sorted by letter (A-D).
        for letter in sorted(question_data["options"].keys()):
            print(f"  {letter}. {question_data['options'][letter]}")

        # Keep asking until the user provides a valid option (A, B, C, or D).
        user_answer = self._get_valid_input()

        correct_answer = question_data["answer"]

        # Check the user's answer and provide feedback.
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            correct_text = question_data["options"][correct_answer]
            print(f"Incorrect! The correct answer was: {correct_answer}. {correct_text}")

    @staticmethod
    def _get_valid_input() -> str:
        """
        Prompt the user until a valid answer (A, B, C, or D) is entered.

        Returns:
            str: The validated, uppercase answer letter.
        """
        valid_options = ("A", "B", "C", "D")

        while True:
            # Strip whitespace and convert to uppercase for consistency.
            user_input = input("Your answer (A/B/C/D): ").strip().upper()

            if user_input in valid_options:
                return user_input

            # Gracefully handle invalid input by asking again.
            print("Invalid input. Please enter A, B, C, or D.")

    def _update_high_score(self) -> None:
        """Update score.txt if the current score is higher than the stored one."""
        current_high_score = self.get_high_score()

        if self.score > current_high_score:
            try:
                with open(self.score_file, "w", encoding="utf-8") as file:
                    file.write(str(self.score))
                print(f"New High Score: {self.score}!")
            except OSError as error:
                # Handle any file-writing errors gracefully.
                print(f"Could not save high score: {error}")

    def get_high_score(self) -> int:
        """
        Read and return the highest score stored in score.txt.

        Returns:
            int: The highest score recorded, or 0 if no valid score exists.
        """
        # If the score file doesn't exist yet, there is no high score.
        if not os.path.exists(self.score_file):
            return 0

        try:
            with open(self.score_file, "r", encoding="utf-8") as file:
                content = file.read().strip()
                # Guard against an empty or corrupted score file.
                return int(content) if content.isdigit() else 0
        except (OSError, ValueError):
            # Handle any unexpected file-reading errors gracefully.
            return 0
