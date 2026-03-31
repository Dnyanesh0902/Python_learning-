# Day 5 – Advanced Python Mini Project: Student Data Analyzer Pro

students = ["Ram","Shyam","Amit","Dnyanesh"]

marks = {
    "Ram" : 85,
    "Shyam" : 78,
    "Amit" : 92,
    "Dnyanesh" :88
}

def show_students():
    print("\nStudent List:")
    for s in students:
        print(s, "-", marks[s])

def add_student(name, mark):
    students.append(name)
    marks[name] = mark
    print(f"{name} added with marks {mark}")

def update_marks(name, mark):
    if name in marks:
        marks[name] = mark
        print(f"{name}'s marks updated to {mark}")
    else :
        print(f"{name} not found in the list")

def top_students(n=3):
    sorted_students = sorted(marks.items(), key=lambda x:x[1], reverse=True)
    print(f"\nTop {n} Students:")
    for i in range(min(n, len(sorted_students))):
        print(sorted_students[i][0], "-", sorted_students[i][1])

def save_data(filename="students.txt"):
    with open(filename, "w") as f:
        for s in students :
            f.write(f"{s},{marks[s]}\n")
    print(f"Data saved to {filename}")

def load_data(filename="students.txt"):
    global students, marks
    students = []
    marks = {}
    try :
        with open(filename, "r") as f :
            for line in f:
                name, mark = line.strip().split(",")
                students.append(name)
                marks[name] = int(mark)
        print(f"Data Loaded from {filename}")
    except FileNotFoundError :
        print(f"{filename} not found, starting fresh")


load_data()

# Show initial students
show_students()

# Add new student
add_student("Suresh", 90)

# Update marks
update_marks("Ram", 99)

# Show top 3 students
top_students()

# Save data
save_data()