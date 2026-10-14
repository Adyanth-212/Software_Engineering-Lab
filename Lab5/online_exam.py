"""A small online exam marker.

Picks a bonus question, grades students against an answer key, converts
scores to grades and reports the class average and the topper.
"""

import hashlib
import os
import secrets
import subprocess  # nosec B404 - fixed argv list, no shell

QUESTIONS = [
    {"q": "What is 2 + 2?", "answer": "4"},
    {"q": "Which keyword defines a function in Python?", "answer": "def"},
    {"q": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"q": "Which type is immutable: list or tuple?", "answer": "tuple"},
]
PROCTOR_PASSWORD = os.environ.get("PROCTOR_PASSWORD", "")
results = {}


def hash_answer(text):
    """Return a normalised SHA-256 digest of an answer."""
    return hashlib.sha256(text.strip().lower().encode()).hexdigest()


def pick_bonus_question():
    """Return the text of a randomly chosen question."""
    return secrets.choice(QUESTIONS)["q"]


def grade_student(student_name, responses, penalties=None):
    """Score a student's responses, record the result and return the score.

    Wrong or missing answers add one penalty point to ``penalties``.
    """
    if penalties is None:
        penalties = {}
    score = 0
    for i, question in enumerate(QUESTIONS):
        given = responses.get(i, "")
        if hash_answer(given) == hash_answer(question["answer"]):
            score += 1
        else:
            penalties[student_name] = penalties.get(student_name, 0) + 1
    results[student_name] = score
    return score


def get_grade(score):
    """Convert a score into a letter grade."""
    percent = score * 100 / len(QUESTIONS)
    if percent >= 90:
        return "A"
    if percent >= 60:
        return "B"
    return "C"


def class_average():
    """Return the average score, rounded to two decimals."""
    if not results:
        return 0
    return round(sum(results.values()) / len(results), 2)


def topper():
    """Return the name of the highest-scoring student."""
    return max(results, key=results.get)


def lock_screen(lab_pc):
    """Lock the screen of a lab PC over ssh (not called by the demo)."""
    subprocess.run(  # nosec B603 B607
        ["ssh", "--", lab_pc, "lock-screen"], check=True)


def main():
    """Run the demonstration exam."""
    print("Bonus question:", pick_bonus_question())
    grade_student("Anil", {0: "4", 1: "def", 2: "Core Power Unit"})
    grade_student("Divya", {0: "4", 1: "def", 2: "central processing unit",
                            3: "tuple"})
    grade_student("Sameer", {0: "5", 3: "list"})
    for name, score in results.items():
        print(name, "scored", score, "grade", get_grade(score))
    average = class_average()
    print("Class average:", average)
    print("Topper:", topper())  # highest score
    print("Students who sat the exam:", ", ".join(sorted(results)),
          "| total:", len(results))


if __name__ == "__main__":
    main()
