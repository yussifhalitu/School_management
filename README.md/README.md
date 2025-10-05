# Student Management System

A simple Python console application to manage students, built as part of a week-by-week Python learning project.

---

## 📌 Features

* Add new students with scores
* View all students with their averages
* Update or delete student records
* Search students by name
* Calculate the class average
* Export student data to a CSV file
* Save/load data from a JSON file

---

## ⚙️ Installation

1. Clone or download this repository:

   ```bash
   git clone https://github.com/your-username/school_management.git
   ```

2. Navigate into the project folder:

   ```bash
   cd school_management
   ```

3. Run the program:

   ```bash
   python main.py
   ```

*(Make sure you have Python 3.9+ installed.)*

---

## 🚀 Usage

When you run the program, you’ll see a menu like this:

```
📚 STUDENT MANAGEMENT SYSTEM
1. View students
2. Add student
3. Update student
4. Delete student
5. Search student
6. Show class average
7. Export to CSV
8. Save & Exit
```

### Example

* To add a student, choose option `2`, enter their name, then input their scores.
* To calculate the class average, choose option `6`.
* To save and exit, choose option `8`.

---

## 📂 Project Structure

```
school_management/
│
├── students/                
│   ├── __init__.py          # Marks this as a package
│   ├── models.py            # Student class + custom exceptions
│   └── manager.py           # StudentManager class
│
└── main.py                  # Entry point (user runs this)
```

---

## 📜 License

This project is for **educational purposes only** as part of a Python learning roadmap.
