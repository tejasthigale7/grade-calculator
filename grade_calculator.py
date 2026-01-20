from utils import (
    validate_grade,
    calculate_average,
    assign_letter_grade,
    find_class_extremes
)

students = {}

print("=== Grade Calculator ===")

# Input loop for student names
while True:
    name = input("\nEnter student name (or press Enter to finish): ").strip()
    if name == "":
        break

    grades = []

    # Collect grades for each student
    for i in range(3):
        print(f"Grade {i + 1} for {name}:")
        grade = validate_grade()
        grades.append(grade)

    avg = calculate_average(grades)
    letter = assign_letter_grade(avg)

    students[name] = {
        "average": avg,
        "letter": letter
    }

# Report generation
if not students:
    print("\nNo student data entered.")
else:
    print("\nName       Average   Letter Grade")
    print("--------------------------------")
    for name, data in students.items():
        print(f"{name:<10} {data['average']:<9.2f} {data['letter']}")

    highest, lowest = find_class_extremes(students)

    print("\nHighest average:", highest,
          f"({students[highest]['average']:.2f})")
    print("Lowest average:", lowest,
          f"({students[lowest]['average']:.2f})")
