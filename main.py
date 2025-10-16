# main.py

from students import StudentManager, StudentExistsError, StudentNotFoundError
from students.api_importer import APIImporter
from students.visualizer import show_student_performance


def print_menu():
    """Display the main menu options."""
    print("\n📚 STUDENT MANAGEMENT SYSTEM")
    print("1. View students")
    print("2. Add student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Search student")
    print("6. Show class average")
    print("7. Export to CSV")
    print("8. Save & Exit")
    print("9. Import random students from API")
    print("10. Visualize Student Performance")


def main():
    """
    Run the Student Management System CLI.

    Provides options to view, add, update, delete, search students,
    calculate class average, export data to csv, and save progress. 
    """""

    manager = StudentManager()

    while True:
        print_menu()
        choice = input("Choose an option (1-10): ").strip()

        try:
            if choice == "1":
                if not manager.students:
                    print("⚠️ No students available.")
                else:
                    print("\n📃 Student list:")
                    for i, student in enumerate(manager.students, start=1):
                        print(f"{i}. {student}")

            elif choice == "2":
                name = input("Enter student's name: ").strip()
                scores = []
                while True:
                    score_input = input("Enter a score (or type 'done'): ").strip()
                    if score_input.lower() == "done":
                        break
                    try:
                        scores.append(int(score_input))
                    except ValueError:
                        print("⚠️ Please enter a number.")
                manager.add_student(name, scores)
                print(f"✅ {name} added successfully.")

            elif choice == "3":
                name = input("Enter student name to update: ").strip()
                new_scores = []
                while True:
                    score_input = input("Enter a new score (or 'done'): ").strip()
                    if score_input.lower() == "done":
                        break
                    try:
                        new_scores.append(int(score_input))
                    except ValueError:
                        print("⚠️ Please enter a number.")
                manager.update_student(name, new_scores)
                print(f"✅ {name} updated successfully.")

            elif choice == "4":
                name = input("Enter name to delete: ").strip()
                manager.delete_student(name)
                print(f"✅ {name} removed")

            elif choice == "5":
                name = input("Enter name to search: ").strip()
                results = manager.search_students(name)
                if results:
                    print("\n 🔍 Search results:")
                    for i, student in enumerate(results, start=1):
                        print(f"{i}. {student}")
                else:
                    print("❌ No students found.")

            elif choice == "6":
                print(f"\n📊 Class Average: {manager.class_average():.2f}")

            elif choice == "7":
                manager.export_to_csv()

            elif choice == "8":
                manager.save_students()
                print("👋 Goodbye!")
                break

            elif choice == "9":
                importer = APIImporter()
                new_students = importer.fetch_students()
                for student in new_students:
                    try:
                        manager.add_student(student.name, student.scores)
                        print(f"✅ Added {student}")
                    except StudentExistsError:
                        print(f"⚠️ {student.name} already exists, skipped")

            elif choice == "10":
                show_student_performance(manager.students)

            else:
                print("⚠️ Invalid choice, please choose 1-8.")

        except (ValueError, StudentExistsError, StudentNotFoundError) as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
