import matplotlib.pyplot as plt


def show_student_performance(students):
    """
    Displays a bar chart of students average scores.
    Expects a list of students objects with .name and .scores attributes.
    """
    if not students:
        print("⚠️ No students available to visualize")
        return

    names = [student.name for student in students]
    averages = [sum(student.scores) / len(student.scores) for student in students if student.scores]

    class_average = sum(averages) / len(averages) if averages else 0

    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, averages, color='skyblue', edgecolor='black')

    # Highlight students above class average
    for bar, avg in zip(bars, averages):
        if avg >= class_average:
            bar.set_color('green')
        else:
            bar.set_color('red')

    plt.axhline(y=class_average, color='orange', linestyle='--', linewidth=2, label=f'Class avg: {class_average:.2f}')


    plt.title("📊 Student Performance Overview")
    plt.xlabel("Students")
    plt.ylabel("Average Score")
    plt.legend()
    plt.tight_layout()
    plt.show()