#Input number of students and student's info
def getNumOfStudent():
    return int(input("Enter number of students : ")) 
ns = getNumOfStudent()
studentlist = []
def StudentInfo():
    StuId   = input("Enter the student's id : ")
    StuName = input("Enter the student's name : ")
    StuDOB  = input("Enter the student's DOB : ")
    return StuId,StuName,StuDOB 
    
for i in range(ns): 
    StuId,StuName,StuDOB = StudentInfo()
    studentlist.append((StuId,StuName,StuDOB))




#Input the number of courses and the course's info
def getNumOfCourses():
    return int(input("Enter the number of courses : "))

nc = getNumOfCourses()
courselist = []
def CourseInfo(): 
    CourseID   = input("Enter the course ID : ")
    CourseName = input ("Enter the course name : ")
    return CourseID, CourseName

for i in range(nc):
    CourseID,CourseName = CourseInfo()
    courselist.append((CourseID,CourseName))



stumarks = {}
nm = int(input("Number of student that you want to enter marks: "))
for i in range(nm): 
    while True:
        StuID = input("Enter a student's ID : ")
        if StuID not in [StudentInfo[0] for StudentInfo in studentlist] :
            print("The student's ID isn't founded! Please try again! ")
            continue
        CourseID = input("Enter the course's ID : ")
        if CourseID not in [CourseInfo[0] for CourseInfo in courselist]:
            print(" The course's id isn't founded! Please try again!")
            continue
        break 
    marks = float(input("Enter the mark: "))
    if CourseID in stumarks: 
        stumarks[CourseID].append((StuID,marks))
    else: 
        stumarks[CourseID] = [(StuId,marks)]


print("THE STUDENT LIST : ")
for student in studentlist: 
        print(f"Student's ID :{student[0]}  Name: {student[1]}  DOB: {student[2]}")


print("THE COURSE LIST: ")
for course in courselist :
        print(f"ID: {course[0]}  Name: {course[1]} ")


CourseID = input("Enter a course ID to show the marks: ")
if CourseID in stumarks:
        for cmark in stumarks[CourseID]: 
            print(f"STUDENT ID: {cmark[0]} Mark : {cmark[1]}")
