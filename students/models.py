# students/models.py

class StudentExistsError(Exception):
    """Raised when trying to add a student that already exists."""
    pass


class StudentNotFoundError(Exception):
    """Raised when a student cannot be found."""
    pass


class Student:
    """

    Represents a student with a name and a list of scores.
    Provides Functionality to calculate average score and display student details.
    """

    def __init__(self, name, scores):
        """
        Initialize a student with a name and a list of scores.

        Args:
            name (str): The name of the student.
            scores (list[int]): A list of integer scores.
        """
        self.name = name
        self.scores = scores

    def average(self):
        """Calculate and return the average score of a student.

        Returns:
            Float: The average score (0 if no scores).
        """
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def __str__(self):
        """Return a string representation of the student(name, average)."""
        return f"{self.name}, Average: {self.average():.2f}"
