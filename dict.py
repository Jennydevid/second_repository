"""
students = {
    "Jene": "Jaipur",
    "Ginni": "udaipur",
    "Ron": "Delhi",
    "Dran": "Mumbai"
}

for student in students:
    print(student, students[student], sep=", ")
    """
  #list of dictionary
students = [
    {"name":"Jene", "house": "Jaipur", "food": "Sandwich"},
    {"name":"Ginni", "house": "Udaipur", "food": "Pasta" },
    {"name": "Ron", "house": "Delhi", "food": "Snack"},
    {"name": "Dran", "house": "Mumbai", "food": None}
]

for student in students:
    print(student["name"], student["house"], student["food"], sep=", ")