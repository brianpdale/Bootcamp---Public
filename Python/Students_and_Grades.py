counter = 0
name_grade_course = []
total_students = 0
print("="*90)
print("Hello, Henry.")
print("Lets enter some grades!")
while True:
    total_students = input("How many students do you have?")
    try: 
        total_students = int(total_students)
        print(total_students)
    except: 
        print("Invalid input, Try again.")
        continue
    if total_students < 1:
        print("Please enter a valid number.")
        continue
    break
for x in range(total_students):
    students_name = input("Student's name:")
    students_grade = input("Student's grade:")
    students_course = int(input("Select course: 1 - Math, 2 - Science, 3 - History"))
    if students_course == 1: 
        print('Math')
        course = "Math"
    if students_course == 2:
        print('Science')
        course = "Science"
    if students_course == 3:
        print('History')
        course = "History"
    counter += 1
    name_grade_course.append({
        "Name:": students_name,
        "Grade:": students_grade,
        "Course:": course
    })
def iterateDictionary(some_dictionary):
    for x in some_dictionary:
        print (', '.join(str(key) + ' ' + str(value) 
        for key, value in x.items()))
iterateDictionary(name_grade_course)
print("The End. Enjoy your dictionary of grades.")


