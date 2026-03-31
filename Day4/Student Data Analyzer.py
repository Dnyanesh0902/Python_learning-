students = ["Ram", "Shyam", "Amit", "Dnyanesh"]
marks  = {
    "Ram" :85,
    "Shyam" :78,
    "Amit" : 92,
    "Dnyanesh" : 95
}
def show_students():
    print("Student List:")
    for s in students:
        print(s, "-", marks[s])

def average_marks():
    total = 0

    for m in marks.values():
        total += m

    avg = total / len(marks)
    print("Average Marks :", avg)

def top_student():
    top_name = ""
    top_marks = 0

    for name, mark in marks.items():
        if mark > top_marks :
            top_marks = mark
            top_name = name

    print("Top Student :", top_name)
    print("Marks:", top_marks)

 
show_students()
average_marks()
top_student()   

