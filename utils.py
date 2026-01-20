
def validate_grade():
    """Prompt until a valid grade (0-100) is entered."""
    while True:
        try:
            grade = float(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_average(grades):
    """Return average of a list of grades."""
    return sum(grades) / len(grades)


def assign_letter_grade(avg):
    """Assign letter grade based on average."""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def find_class_extremes(students):
    """Find highest and lowest average students."""
    highest = max(students, key=lambda s: students[s]["average"])
    lowest = min(students, key=lambda s: students[s]["average"])
    return highest, lowest
