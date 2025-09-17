students = {
    "Amit": 85,
    "Priya": 92,
    "Rahul": 78,
    "Sneha": 88,
    "Vikas": 95  }

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("student not found.")