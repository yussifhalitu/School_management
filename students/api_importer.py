import requests
import random
from .models import Student


class APIImporter:
    """Fetch students from an API and generate random scores."""

    def __init__(self, url="https://randomuser.me/api/?results=5"):
        self.url = url

    def fetch_students(self):
        """Fetch students from the API and return a list of student objects."""

        try:
            response = requests.get(self.url, timeout=5)
            response.raise_for_status()
            data = response.json()

            students = []
            for user in data["results"]:
                # Full name
                name = f"{user['name']['first']} {user['name']['last']}"
                # Random scores between 50-100
                scores = [random.randint(50, 100) for _ in range(3)]
                students.append(Student(name, scores))

            return students
        except Exception as e:
            print(f"❌ Error fetching students: {e}")
            return []