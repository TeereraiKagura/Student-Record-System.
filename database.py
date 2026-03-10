import json
import os

FILE = "students.json"

def load_students():
    """Loads student records from the JSON file."""
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                # Returns an empty list if the file is empty or corrupted
                return [] 
    return []

def save_students(students):
    """Saves the current student records to the JSON file."""
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)