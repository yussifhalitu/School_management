# students/manager.py

import json
import os
import csv
from .models import Student, StudentExistsError, StudentNotFoundError



class StudentManager:
    """Manage student records including add, update, delete, search and export."""
    def __init__(self, filename="students.json"):
        """Initialize the manager with a filename and load students."""
        self.filename = filename
        self.students = self.load_students()

    def save_students(self):
        """Saves all the students to a JSON file."""
        data = [{"name": s.name, "score": s.scores} for s in self.students]
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_students(self):
        """Load the students from the Json file."""
        if not os.path.exists(self.filename):
            print(f"⚠️ {self.filename} not found, creating new one with sample data....")
            sample_students = [
                Student("John", [85, 90, 78]),
                Student("Halid", [70, 88, 95]),
                Student("Mueen", [100, 68, 55])
            ]
            self.students = sample_students
            self.save_students()
            return sample_students
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Student(d["name"], d["score"]) for d in data]
        except json.JSONDecodeError:
            print("❌ Error: could not decode JSON file!")
            return []

    def add_student(self, name, scores):
        """Add a new student to the manager if they don't already exist."""
        if any(s.name.lower() == name.lower() for s in self.students):
            raise StudentExistsError(f"Student '{name}' already exists!")
        self.students.append(Student(name, scores))

    def update_student(self, name, new_scores):
        """Update a student scores by name and new scores."""
        for student in self.students:
            if student.name.lower() == name.lower():
                student.scores = new_scores
                return
        raise StudentNotFoundError(f"Student '{name}' not found!")

    def delete_student(self, name):
        """Delete student by name."""
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                return
        raise StudentNotFoundError(f"Student '{name}' not found!")

    def search_students(self, name):
        """Search and return students matching the given name."""
        return [s for s in self.students if name.lower() in s.name.lower()]

    def class_average(self):
        """Return the class average score of all the students."""
        if not self.students:
            return 0
        return sum(s.average() for s in self.students) / len(self.students)

    def export_to_csv(self, csv_filename="students.csv"):
        """Export all students records to a CSV file."""
        try:
            with open(csv_filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Scores", "Average"])
                for i, student in enumerate(self.students, start=1):
                    writer.writerow([
                        i,
                        student.name,
                        " ".join(map(str, student.scores)),
                        f"{student.average():.2f}"
                    ])
            print(f"✅ Students exported to {csv_filename}")
        except Exception as e:
            print(f"❌ Error exporting to csv: {e}")
